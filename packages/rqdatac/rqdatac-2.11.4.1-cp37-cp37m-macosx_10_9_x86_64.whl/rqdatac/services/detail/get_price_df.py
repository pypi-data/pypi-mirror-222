# -*- coding: utf-8 -*-
import datetime
import warnings

import numpy as np
import pandas as pd

from rqdatac.services.detail.resample_helper import resample_week_df
from rqdatac.services.get_price import (
    _ensure_fields,
    get_current_trading_date
)
from rqdatac.services.calendar import is_trading_date, get_next_trading_date
from rqdatac.utils import (
    int14_to_datetime_v,
    int8_to_datetime_v,
    today_int,
    date_to_int8,
)
from rqdatac.client import get_client
from rqdatac.services.future import get_dominant, current_real_contract
from rqdatac.services.basic import instruments
from rqdatac.services.stock_status import is_suspended
from rqdatac.share.errors import PermissionDenied, MarketNotSupportError, NoSuchService

DAYBAR_FIELDS = {
    "future": ["settlement", "prev_settlement", "open_interest", "limit_up", "limit_down",
               "day_session_open"],
    "common": ["open", "close", "high", "low", "total_turnover", "volume", "prev_close"],
    "stock": ["limit_up", "limit_down", "num_trades"],
    "fund": ["limit_up", "limit_down", "num_trades", "iopv"],
    "spot": ["settlement", "prev_settlement", "open_interest", "limit_up", "limit_down"],
    "option": ["open_interest", "strike_price", "contract_multiplier", "prev_settlement", "settlement", "limit_up",
               "limit_down", "day_session_open"],
    "convertible": ["num_trades"],
    "index": [],
    "repo": ["num_trades"],
}

WEEKBAR_FIELDS = {
    "future": ["settlement", "prev_settlement", "open_interest", "day_session_open"],
    "common": ["open", "close", "high", "low", "total_turnover", "volume"],
    "stock": ["num_trades"],
    "fund": ["num_trades", "iopv"],
    "spot": ["settlement", "prev_settlement", "open_interest"],
    "option": ["open_interest", "strike_price", "contract_multiplier", "settlement", "day_session_open"],
    "convertible": ["num_trades"],
    "index": [],
    "repo": ["num_trades"],
}

MINBAR_FIELDS = {
    "future": ["trading_date", "open_interest"],
    "common": ["open", "close", "high", "low", "total_turnover", "volume"],
    "stock": ["num_trades"],
    "fund": ["num_trades", "iopv"],
    "spot": ["trading_date", "open_interest"],
    "option": ["trading_date", "open_interest"],
    "convertible": [],
    "index": [],
    "repo": [],
}


ZERO_FILL_FIELDS = frozenset({"total_turnover", "open_interest", "volume"})

SPOT_DIRECTION_MAP = {0: "null", 1: "多支付空", 2: "空支付多", 3: "交收平衡"}


def get_price_df(
        order_book_ids,
        start_date,
        end_date,
        frequency,
        duration,
        fields,
        adjust_type,
        skip_suspended,
        stocks,
        funds,
        indexes,
        futures,
        futures888,
        spots,
        options,
        convertibles,
        repos,
        market
):
    if frequency == "d":
        fields, has_dominant_id = _ensure_fields(fields, DAYBAR_FIELDS, stocks, funds, futures, futures888, spots, options, convertibles, indexes, repos)
        pf, obid_slice_map = get_daybar(order_book_ids, start_date, end_date, fields, duration, market)
        if pf is None:
            return
    else:
        fields, has_dominant_id = _ensure_fields(fields, MINBAR_FIELDS, stocks, funds, futures, futures888, spots, options, convertibles, indexes, repos)
        history_permission_denied, today_permission_denied = False, False
        try:
            pf, obid_slice_map = get_minbar(order_book_ids, start_date, end_date, fields, duration, market)
        except (PermissionDenied, MarketNotSupportError, NoSuchService):
            pf = obid_slice_map = None
            history_permission_denied = True

        history_latest_day = 0 if pf is None else date_to_int8(pf.index.levels[1].max())
        today = today_int()

        next_trading_date = date_to_int8(get_next_trading_date(today, market=market))
        if end_date >= next_trading_date and (start_date > today or history_latest_day >= today):
            live_date = next_trading_date
        else:
            live_date = today

        live_obs = None
        if end_date >= today_int():
            today_str = datetime.date.today().strftime('%Y-%m-%d')
            all_live_obs = set(ins.order_book_id for ins in instruments(order_book_ids)
                               if ins.de_listed_date == '0000-00-00' or ins.de_listed_date >= today_str)
            if pf is not None:
                lv1_dts = pf.index.get_level_values(1)
                lv1_dts = lv1_dts.year * 10000 + lv1_dts.month * 100 + lv1_dts.day
                lv0_obs = pf.index.get_level_values(0)
                ob_dts = {ins.order_book_id: (
                    live_date if (
                            ins.type == 'Future' or (ins.type == 'Option' and ins.exchange not in ('XSHG', 'XSHE'))
                    ) else today) for ins in instruments(lv0_obs.unique())}
                history_obs = pf.index[lv1_dts == lv0_obs.map(ob_dts)].get_level_values(0).unique()
                live_obs = list(set(all_live_obs) - set(history_obs))
            else:
                live_obs = list(all_live_obs)

        if live_obs:
            try:
                today_pf, today_obid_slice_map = get_today_minbar(live_obs, fields, duration, market)
            except (PermissionDenied, MarketNotSupportError, NoSuchService):
                today_permission_denied = True
            else:
                if pf is None:
                    pf = today_pf
                    obid_slice_map = today_obid_slice_map
                elif today_pf is not None:
                    # sort_index 后 obid 为字典序
                    pf = pd.concat([pf, today_pf]).sort_index()
                    line_no, obid_slice_map = 0, {}
                    # np.unique 默认顺序也为字典序，因此不需要再调整
                    obids, counts = np.unique(pf.index.get_level_values(0), return_counts=True)
                    for obid, ct in zip(obids, counts):
                        obid_slice_map[obid] = slice(line_no, line_no + ct, None)
                        line_no += ct
        if pf is None:
            if history_permission_denied and today_permission_denied:
                raise PermissionDenied("Not permit to get minbar price ")
            elif history_permission_denied:
                warnings.warn("Not permit to get history minbar price")
            elif today_permission_denied:
                warnings.warn("Not permit to get realtime minbar price")
            return

    result = _adjust_pf(
        pf,
        order_book_ids,
        stocks,
        funds,
        convertibles,
        futures888,
        start_date,
        end_date,
        has_dominant_id,
        adjust_type,
        skip_suspended,
        obid_slice_map,
        market,
    )
    return result


def get_daybar(order_book_ids, start_date, end_date, fields, duration, market):
    data = get_client().execute(
        "get_daybar_v", order_book_ids, start_date, end_date, fields, duration, market
    )
    data = [(obid, {k: np.frombuffer(*v) for k, v in d.items()}) for obid, d in data]
    return convert_bar_to_multi_df(data, 'date', fields, int8_to_datetime_v)


def get_future_indx_daybar(order_book_ids, start_date, end_date, fields, duration=1, market="cn"):
    data = get_client().execute(
        "futures.get_future_indx_daybar_v", order_book_ids, start_date, end_date, fields, duration, market
    )
    data = [(obid, {k: np.frombuffer(*v) for k, v in d.items()}) for obid, d in data]
    multi_df, _ = convert_bar_to_multi_df(data, 'date', fields, int8_to_datetime_v)
    if multi_df is not None:
        return multi_df


def get_minbar(order_book_ids, start_date, end_date, fields, duration, market):
    data = get_client().execute(
        "get_minbar_v", order_book_ids, start_date, end_date, fields, duration, market
    )
    data = [(obid, {k: np.frombuffer(*v) for k, v in d.items()}) for obid, d in data]
    return convert_bar_to_multi_df(data, "datetime", fields, int14_to_datetime_v)


def get_today_minbar(order_book_ids, fields, duration, market="cn"):
    futures_88 = [i for i in instruments(order_book_ids) if i.order_book_id.endswith('88') and i.type == 'Future']
    real_contracts = {
        i.order_book_id: current_real_contract(i.underlying_symbol, market)
        for i in futures_88
    }
    real_contracts = {k: v for k, v in real_contracts.items() if v is not None}
    order_book_ids = set(order_book_ids)
    obs = list(order_book_ids.union(set(real_contracts.values())))
    data = get_client().execute("get_today_minbar", obs, fields, duration, market)
    data = dict(data)
    data.update((ob, data.get(c)) for ob, c in real_contracts.items())
    data = [(k, v) for k, v in data.items() if k in order_book_ids]
    return convert_bar_to_multi_df(data, "datetime", fields, int14_to_datetime_v)


def convert_bar_to_multi_df(data, dt_name, fields, convert_dt):
    line_no = 0
    dt_set = set()
    obid_level = []
    obid_slice_map = {}
    for obid, d in data:
        dts = d[dt_name]
        dts_len = len(dts)
        if dts_len == 0:
            continue
        obid_slice_map[obid] = slice(line_no, line_no + dts_len, None)
        dt_set.update(dts)
        line_no += dts_len

        obid_level.append(obid)

    if line_no == 0:
        return None, obid_slice_map

    obid_idx_map = {o: i for i, o in enumerate(obid_level)}
    obid_label = np.empty(line_no, dtype=object)
    dt_label = np.empty(line_no, dtype=object)
    arr = np.full((line_no, len(fields)), np.nan)
    r_map_fields = {f: i for i, f in enumerate(fields)}
    for f in ZERO_FILL_FIELDS:
        if f in fields:
            arr[:, r_map_fields[f]] = 0

    dt_arr_sorted = np.array(sorted(dt_set), dtype=np.int64)
    dt_level = convert_dt(dt_arr_sorted)

    for obid, d in data:
        dts = d[dt_name]
        if len(dts) == 0:
            continue
        slice_ = obid_slice_map[obid]
        for f, value in d.items():
            if f == dt_name:
                dt_label[slice_] = dt_arr_sorted.searchsorted(dts, side='left')
            else:
                arr[slice_, r_map_fields[f]] = value
        obid_label[slice_] = [obid_idx_map[obid]] * len(dts)

    try:
        func_is_singletz = getattr(pd._libs.lib, 'is_datetime_with_singletz_array')
        setattr(pd._libs.lib, 'is_datetime_with_singletz_array', lambda *args: True)
    except AttributeError:
        func_is_singletz = None
    multi_idx = pd.MultiIndex(
        [obid_level, dt_level],
        [obid_label, dt_label],
        names=('order_book_id', dt_name)
    )
    if func_is_singletz is not None:
        setattr(pd._libs.lib, 'is_datetime_with_singletz_array', func_is_singletz)

    df = pd.DataFrame(data=arr, index=multi_idx, columns=fields)
    return df, obid_slice_map


def _adjust_pf(
        pf,
        order_book_ids,
        stocks,
        funds,
        convertibles,
        futures888,
        start_date,
        end_date,
        has_dominant_id,
        adjust_type,
        skip_suspended,
        obid_slice_map,
        market,
):
    adjust = (stocks or funds) and adjust_type in {"pre", "post", "pre_volume", "post_volume"}
    if adjust:
        from rqdatac.services.detail.adjust_price import adjust_price_multi_df
        adjust_price_multi_df(pf, stocks + funds, adjust_type, obid_slice_map, market)
    if has_dominant_id:
        # 1.全为非正常合约 2.有期货类型合约并且指定dominant_id字段
        # 只有满足其中一种才在返回字段中增加dominant_id
        add_dominant_id(pf, futures888, obid_slice_map)
    if skip_suspended and len(order_book_ids) == 1 and (stocks or convertibles):
        pf = filter_suspended(pf, order_book_ids[0], start_date, end_date, len(convertibles) > 0, market)

    if "trading_date" in pf:

        def convert_to_timestamp(v):
            if np.isnan(v):
                return pd.NaT
            return pd.Timestamp(str(int(v)))

        if hasattr(pf.trading_date, "applymap"):
            pf.trading_date = pf.trading_date.applymap(convert_to_timestamp)
        else:
            pf.trading_date = pf.trading_date.apply(convert_to_timestamp)

    if "settlement_direction" in pf:

        def convert_direction(key):
            if np.isnan(key):
                return key
            return SPOT_DIRECTION_MAP[key]

        if hasattr(pf.settlement_direction, "applymap"):
            pf.settlement_direction = pf.settlement_direction.applymap(convert_direction)
        else:
            pf.settlement_direction = pf.settlement_direction.apply(convert_direction)

    return pf


def add_dominant_id(result, futures888, obid_slice_map):
    from rqdatac.services.calendar import get_next_trading_date
    def _may_shift_date(d):
        # 夜盘的开始时间是晚上9点, 这时候对应的 dominant_id 应该是下一个交易日的 dominant_id
        if d.hour >= 21 or not is_trading_date(d):
            return pd.Timestamp(get_next_trading_date(d))
        return d

    for order_book_id, underlying in futures888.items():
        if order_book_id in obid_slice_map:
            slice_ = obid_slice_map[order_book_id]
            dts = result.index.get_level_values(1)[slice_].map(_may_shift_date)
            dominants = get_dominant(
                underlying, dts[0].date(), dts[-1].date())
            if dominants is not None:
                result.loc[result.index[slice_], "dominant_id"] = np.take(
                    dominants.values, dominants.index.searchsorted(dts, side="right") - 1)


def filter_suspended(ret, order_book_id, start_date, end_date, is_convertible, market):
    if is_convertible:
        from rqdatac.services.convertible import is_suspended as is_convertible_suspend
        s = is_convertible_suspend(order_book_id, start_date, end_date)
    else:
        s = is_suspended(order_book_id, start_date, end_date, market)
    ret_date_index = ret.index.get_level_values(1)
    index = s.index.union(ret_date_index)
    s = s.reindex(index)
    s = s.fillna(method="ffill")
    s = s.loc[ret_date_index]
    s = s[order_book_id] == False
    return ret[s.values]


def get_week_df(order_book_ids, start_date, end_date, fields, adjust_type, market, stocks, funds, indexes, futures,
                futures888, spots, options, convertibles, repos):
    fields, has_dominant_id = _ensure_fields(fields, WEEKBAR_FIELDS, stocks, funds, futures, futures888, spots,
                                             options, convertibles, indexes, repos)
    has_volume_field = 'volume' in fields
    if not has_volume_field:
        fields.append('volume')
    df = get_price_df(
        order_book_ids, start_date, end_date, 'd', 1, fields, adjust_type, False,
        stocks, funds, indexes, futures, futures888, spots, options, convertibles, repos, market
    )
    if df is None:
        return
    res = resample_week_df(df, fields)
    if not has_volume_field:
        res.drop(columns=['volume'], inplace=True)
    return res
