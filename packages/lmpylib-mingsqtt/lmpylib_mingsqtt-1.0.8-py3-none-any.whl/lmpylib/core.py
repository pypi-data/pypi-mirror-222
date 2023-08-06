import numpy as np
import pandas as pd
import scipy.stats as stats
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import seaborn as sns
import itertools
import math
from datetime import date
from datetime import datetime
from datetime import timedelta
import time
import threading
import pytz
import re


pd.set_option("display.width", 250)
pd.set_option('display.max_rows', 500)
pd.set_option('display.min_rows', 200)
pd.set_option('display.max_columns', 500)


def _summarize_categorical(data, include_na_only_if_exist=False, sort_by="count", ascending=True):
    na_count = sum([1 for val in data if pd.isna(val)])
    group = pd.DataFrame({"Value": data, "Count": [1] * len(data)}).groupby(by="Value", sort=False).count()
    if sort_by == "count":
        group = group.sort_values(by="Count", ascending=ascending)
    elif (sort_by == "label") or (sort_by == "index") or (sort_by == "text"):
        group = group.sort_index(ascending=ascending)
    group.index = group.index.astype("str")
    if (not include_na_only_if_exist) or (na_count > 0):
        group = pd.concat([group, pd.DataFrame({"Count": np.array([na_count], dtype=int)}, index=["NA"])], ignore_index=False)
    return group


def _summarize_numeric(data, as_rows=False, outlier_iqr_multiplier=None, outlier_std_multiplier=None):
    without_na = np.array([val for val in data if (val is not None) and (not pd.isna(val))])

    if len(without_na) == 0:
        if as_rows:
            return pd.DataFrame({
                "Stats": [None, None, None, None, None, None, len(data), len(data) - len(without_na)]},
                index=["Min", "Q1", "Median", "Mean", "Q3", "Max", "Len", "NA"])
        else:
            return pd.DataFrame({
                "Min": [None],
                "Q1": [None],
                "Median": [None],
                "Mean": [None],
                "Q3": [None],
                "Max": [None],
                "Len": [len(data)],
                "NA": [len(data) - len(without_na)]
            }, index=[""])

    if as_rows:
        return pd.DataFrame({
            "Stats": [np.min(without_na), np.quantile(without_na, 0.25), np.median(without_na), np.mean(without_na),
                      np.quantile(without_na, 0.75), np.max(without_na), len(data), len(data) - len(without_na)]},
            index=["Min", "Q1", "Median", "Mean", "Q3", "Max", "Len", "NA"])
    else:
        return pd.DataFrame({
            "Min": [np.min(without_na)],
            "Q1": [np.quantile(without_na, 0.25)],
            "Median": [np.median(without_na)],
            "Mean": [np.mean(without_na)],
            "Q3": [np.quantile(without_na, 0.75)],
            "Max": [np.max(without_na)],
            "Len": [len(data)],
            "NA": [len(data) - len(without_na)]
        }, index=[""])


def _round_for_print(num):
    if abs(num) >= 1000:
        return np.round(num, 0)
    elif abs(num) >= 10:
        return np.round(num, 1)
    elif abs(num) >= 1:
        return np.round(num, 2)
    else:
        return num


def _summarize_outlier(data, iqr_multiplier, std_multiplier, one_sided, as_rows=False):
    without_na = np.array([val for val in data if (val is not None) and (not pd.isna(val))])

    if len(without_na) == 0:
        if as_rows:
            return pd.DataFrame({
                "Stats": [None, None, None, None, None, None, len(data), len(data) - len(without_na)]},
                index=["Min", "Q1", "Median", "Mean", "Q3", "Max", "Len", "NA"])
        else:
            return pd.DataFrame({
                "Min": [None],
                "Q1": [None],
                "Median": [None],
                "Mean": [None],
                "Q3": [None],
                "Max": [None],
                "Len": [len(data)],
                "NA": [len(data) - len(without_na)]
            }, index=[""])

    mu = np.mean(without_na)
    std = np.std(without_na)
    q1 = np.quantile(without_na, 0.25)
    q3 = np.quantile(without_na, 0.75)
    ma = np.max(without_na)
    mi = np.min(without_na)
    med = np.median(without_na)
    iqr = q3 - q1
    std_upper = mu + std * std_multiplier
    std_lower = mu - std * std_multiplier
    iqr_upper = q3 + iqr * iqr_multiplier
    iqr_lower = q1 - iqr * iqr_multiplier
    n_data = len(data)
    n_nonna = len(without_na)
    n_iqr_greater = np.sum(without_na > iqr_upper)
    n_iqr_less = np.sum(without_na < iqr_lower)
    n_std_greater = np.sum(without_na > std_upper)
    n_std_less = np.sum(without_na < std_lower)

    iqr_upper = _round_for_print(iqr_upper)
    iqr_lower = _round_for_print(iqr_lower)
    std_upper = _round_for_print(std_upper)
    std_lower = _round_for_print(std_lower)
    mu = _round_for_print(mu)
    med = _round_for_print(med)
    q1 = _round_for_print(q1)
    q3 = _round_for_print(q3)

    if not one_sided:
        if as_rows:
            return pd.DataFrame({
                "Stats": [mi, iqr_lower, q1, med, q3, iqr_upper, ma, n_iqr_less, n_iqr_greater, n_data, n_data - n_nonna,
                          std_lower, mu, std_upper, n_std_less, n_std_greater]},
                index=["Min", "-IQR", "Q1", "Median", "Q3", "+IQR", "Max", "Out(-IQR)", "Out(+IQR)", "Len", "NA",
                       "-Std", "Mean", "+Std", "Out(-Std)", "Out(+Std)"])
        else:
            return pd.DataFrame({
                "Min": [mi],
                "-IQR": [iqr_lower],
                "Q1": [q1],
                "Median": [med],
                "Q3": [q3],
                "+IQR": [iqr_upper],
                "Max": [ma],
                "Out(-IQR)": [n_iqr_less],
                "Out(+IQR)": [n_iqr_greater],
                "Len": [n_data],
                "NA": [n_data - n_nonna],
                "-Std": [std_lower],
                "Mean": [mu],
                "+Std": [std_upper],
                "Out(-Std)": [n_std_less],
                "Out(+Std)": [n_std_greater]
            }, index=[""])
    else:
        if as_rows:
            return pd.DataFrame({
                "Stats": [mi, q1, med, q3, iqr_upper, ma, n_iqr_greater, n_data, n_data - n_nonna,
                          mu, std_upper, n_std_greater]},
                index=["Min", "Q1", "Median", "Q3", "+IQR", "Max", "Out(+IQR)", "Len", "NA",
                       "Mean", "+Std", "Out(+Std)"])
        else:
            return pd.DataFrame({
                "Min": [mi],
                "Q1": [q1],
                "Median": [med],
                "Q3": [q3],
                "+IQR": [iqr_upper],
                "Max": [ma],
                "Out(+IQR)": [n_iqr_greater],
                "Len": [n_data],
                "NA": [n_data - n_nonna],
                "Mean": [mu],
                "+Std": [std_upper],
                "Out(+Std)": [n_std_greater]
            }, index=[""])


def _summarize_datetime(data, as_rows=False):
    without_na = np.array([val for val in data if (val is not None) and (not pd.isna(val))])

    tz_info = None
    if (type(data) == pd.Series) and (data.dt.tz is not None):
        tz_info = data.dt.tz.localize(datetime.now()).tzinfo
    elif (len(without_na) > 0) and (str(type(without_na[0])) == "<class 'datetime.datetime'>") and (without_na[0].tzinfo is not None):
        tz_info = without_na[0].tzinfo.localize(datetime.now()).tzinfo

    if len(without_na) == 0:
        if as_rows:
            return pd.DataFrame({
                "Stats": [None, None, None, None, None, None, len(data), len(data) - len(without_na)]},
                index=["Min", "Q1", "Median", "Mean", "Q3", "Max", "Len", "NA"])
        else:
            return pd.DataFrame({
                "Min": [None],
                "Q1": [None],
                "Median": [None],
                "Mean": [None],
                "Q3": [None],
                "Max": [None],
                "Len": [len(data)],
                "NA": [len(data) - len(without_na)]
            }, index=[""])

    without_na = without_na.astype("datetime64[ns]").astype(np.int64)
    if tz_info is not None:
        without_na = without_na + np.int64(tz_info._utcoffset.seconds*1e9)
    if as_rows:
        return pd.DataFrame({
            "Stats": [np.min(without_na).astype('datetime64[ns]'),
                      np.quantile(without_na, 0.25).astype('datetime64[ns]'),
                      np.median(without_na).astype('datetime64[ns]'),
                      np.mean(without_na).astype('datetime64[ns]'),
                      np.quantile(without_na, 0.75).astype('datetime64[ns]'),
                      np.max(without_na).astype('datetime64[ns]'),
                      len(data),
                      len(data) - len(without_na)]},
            index=["Min", "Q1", "Median", "Mean", "Q3", "Max", "Len", "NA"])
    else:
        return pd.DataFrame({
            "Min": [np.min(without_na).astype('datetime64[ns]')],
            "Q1": [np.quantile(without_na, 0.25).astype('datetime64[ns]')],
            "Median": [np.median(without_na).astype('datetime64[ns]')],
            "Mean": [np.mean(without_na).astype('datetime64[ns]')],
            "Q3": [np.quantile(without_na, 0.75).astype('datetime64[ns]')],
            "Max": [np.max(without_na).astype('datetime64[ns]')],
            "Len": [len(data)],
            "NA": [len(data) - len(without_na)]
        }, index=[""])


def _is_categorical(val):
    return isinstance(val, bool) | ((not pd.isna(val)) & (not isinstance(val, (int, float))))


def _is_datetime(val):
    return (str(type(val)) == "<class 'datetime.datetime'>") | (str(type(val)) == "<class 'datetime.date'>")


def _is_numeric(val, consider_datetime=False):
    if consider_datetime:
        return _is_datetime(val) or (not _is_categorical(val))
    else:
        return (not _is_datetime(val)) and (not _is_categorical(val))


def _is_numeric_array(arr, consider_datetime=False):
    if type(arr) == np.ndarray:
        type_name = str(arr.dtype)
        if consider_datetime:
            return (type_name.find("int") >= 0) or (type_name.find("float") >= 0) or (type_name.find("datetime") >= 0)
        else:
            return (type_name.find("int") >= 0) or (type_name.find("float") >= 0)
    elif type(arr) == list:
        if len(arr) > 0:
            return _is_numeric(arr[0], consider_datetime) and _is_numeric(arr[-1], consider_datetime)
        else:
            return False
    elif type(arr) == pd.core.arrays.categorical.Categorical:
        return _is_numeric_array(arr.categories.values, consider_datetime=consider_datetime)
    else:
        raise Exception("Only ndarray is allowed")


def _try_get_cat_levels(arr, return_new_type=False):
    if type(arr) == pd.core.arrays.categorical.Categorical:
        if return_new_type:
            return arr.categories.values, type(arr.categories.values)
        else:
            return arr.categories.values
    else:
        if return_new_type:
            return arr, type(arr)
        else:
            return arr


def summary(data, is_numeric=None, print_only=None, auto_combine_result=True, _numeric_as_rows=False):
    is_datetime = False
    data, type_data = _try_get_cat_levels(data, True)
    if (type_data == list) or (type_data == np.ndarray) or (type_data == pd.Series):
        if is_numeric is None:
            if type_data == list:
                if np.any([_is_datetime(val) for val in data]):
                    is_datetime = True
                else:
                    is_numeric = not np.any([_is_categorical(val) for val in data])
            elif str(data.dtype).find("date") >= 0:
                is_datetime = True
            elif str(data.dtype) == "category":
                is_numeric = False
            elif (str(data.dtype).find("int") >= 0) or (str(data.dtype).find("float") >= 0):
                is_numeric = True
            else:
                is_numeric = not np.any([_is_categorical(val) for val in data])

        if is_datetime:
            sum_return = _summarize_datetime(data, _numeric_as_rows)
        elif is_numeric:
            sum_return = _summarize_numeric(data, _numeric_as_rows)
        else:
            sum_return = _summarize_categorical(data)

        if (print_only is not None) and print_only:
            print(sum_return, "\n")
        else:
            return sum_return
    elif type_data == pd.DataFrame:
        sum_return = {}
        numeric_summaries = None
        datetime_summaries = None
        for colname in data.columns:
            summ = summary(data[colname])
            if auto_combine_result and (type(summ) == pd.DataFrame) and (
            np.all(summ.columns.to_list() == ["Min", "Q1", "Median", "Mean", "Q3", "Max", "Len", "NA"])):
                summ.index = [colname]
                if str(summ.dtypes[0]).find("date") >= 0:
                    if datetime_summaries is None:
                        datetime_summaries = summ
                    else:
                        datetime_summaries = pd.concat([datetime_summaries, summ], ignore_index=False)
                else:
                    if numeric_summaries is None:
                        numeric_summaries = summ
                    else:
                        numeric_summaries = pd.concat([numeric_summaries, summ], ignore_index=False)
            else:
                sum_return[colname] = summ

        if numeric_summaries is not None:
            if numeric_summaries.shape[0] > 1:
                sum_return["NumericColumns"] = numeric_summaries
            else:
                sum_return[numeric_summaries.index[0]] = numeric_summaries
                numeric_summaries.index = [""]
        if datetime_summaries is not None:
            if datetime_summaries.shape[0] > 1:
                sum_return["DatetimeColumns"] = datetime_summaries
            else:
                sum_return[datetime_summaries.index[0]] = datetime_summaries
                datetime_summaries.index = [""]

        if ((print_only is None) and (len(sum_return) > 1)) or print_only:
            for key in sum_return:
                print("<< {} >>".format(key))
                print(sum_return[key], "\n")
        elif len(sum_return) == 1:
            return list(sum_return.values())[0]
        else:
            return sum_return
    else:
        print("Unsupported type {}".format(type_data))


def outlier_summary(data, print_only=None, iqr_multiplier=1.5, std_multiplier=2, one_sided=True):
    if pd.get_option('display.max_columns') < 16:
        pd.set_option('display.max_columns', 16)

    if pd.get_option("display.width") < 140:
        pd.set_option("display.width", 140)

    type_data = type(data)
    if (type_data == list) or (type_data == np.ndarray) or (type_data == pd.Series):
        sum_return = _summarize_outlier(data, iqr_multiplier, std_multiplier, one_sided)

        if (print_only is not None) and print_only:
            print(sum_return, "\n")
        else:
            return sum_return
    elif type_data == pd.DataFrame:
        outlier_summaries = None
        for colname in data.columns:
            summ = outlier_summary(data[colname], iqr_multiplier=iqr_multiplier, std_multiplier=std_multiplier, one_sided=one_sided)
            summ.index = [colname]
            if outlier_summaries is None:
                outlier_summaries = summ
            else:
                outlier_summaries = pd.concat([outlier_summaries, summ], ignore_index=False)

        if (print_only is not None) and print_only:
            print(outlier_summaries, "\n")
        else:
            return outlier_summaries
    else:
        print("Unsupported type {}".format(type_data))


def structure(data_frame, group_by_type=False, sort_by_type=False, print_only=True):
    if group_by_type or sort_by_type:
        if print_only and group_by_type:
            summ = pd.DataFrame({"column": data_frame.columns.to_list(), "type": [str(t) for t in data_frame.dtypes]})
            for tp in summ.groupby(by="type").indices:
                print("{}:".format(tp))
                print(summ.column.loc[summ.type == tp].to_list(), "\n")
        elif print_only and sort_by_type:
            summ = pd.DataFrame({"column": data_frame.columns.to_list(), "type": [str(t) for t in data_frame.dtypes], "index": range(len(data_frame.dtypes))}).sort_values(["type", "index"])
            names = summ.column.to_list()
            max_len = max([len(n) for n in names])
            for i, row in summ.iterrows():
                print("{}  {}  {}".format(str(row["index"]).ljust(int(np.log10(len(names))) + 1), row["column"].ljust(max_len), row["type"]))
        else:
            return pd.DataFrame(
                {"column": data_frame.columns.to_list(), "type": [str(t) for t in data_frame.dtypes], "index": range(len(data_frame.dtypes))}).sort_values(
                by=["type", "index"])
    else:
        if print_only:
            names = data_frame.columns.to_list()
            max_len = max([len(n) for n in names])
            for i, tup in enumerate(zip(names, [str(t) for t in data_frame.dtypes])):
                print("{}  {}  {}".format(str(i).ljust(int(np.log10(len(names))) + 1), tup[0].ljust(max_len), tup[1]))
        else:
            return pd.DataFrame({"column": data_frame.columns.to_list(), "type": [str(t) for t in data_frame.dtypes]})


def hist(*x, bins=None, density=False, range=None, color=None, barwidth=1, xlab=None, ylab=None, title=None, figure_inches=None, show=True):
    plt.style.use("ggplot")
    if len(x) == 1:
        if density:
            n, v, _ = plt.hist(x, bins=bins, density=density, color=color, range=range, histtype='step')
            density = stats.gaussian_kde(v)
            plt.plot(v, density(v))
        else:
            plt.hist(x, bins=bins, density=density, color=color, range=range, rwidth=barwidth)
    elif len(x) > 1:
        for grp, grp_val in enumerate(x):
            clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
            if density:
                n, v, _ = plt.hist(grp_val, bins=bins, density=density, color=clr, range=range, histtype='step')
                density = stats.gaussian_kde(grp_val)
                plt.plot(v, density(v), color=clr)
            else:
                plt.hist(grp_val, bins=bins, density=density, color=clr, range=range, rwidth=barwidth)
    if figure_inches is not None:
        plt.figure().set_size_inches(figure_inches[0], figure_inches[1])
    if xlab is not None:
        plt.xlabel(xlab)
    if ylab is not None:
        plt.ylabel(ylab)
    if title is not None:
        plt.title(title)
    if show:
        plt.show()
    else:
        return plt.figure()


def auto_figure_size(ncol, nrow, adjust_top=1.0, adjust_bottom=0.0, adjust_hspace=0.2, adjust_wspace=0.2, title_height=None, horizontal=False, print=False):
    fig_width = None
    if ncol == 1:
        fig_width = 6
    elif ncol == 2:
        fig_width = 13
    elif ncol > 2:
        fig_width = 17

    ax_width = np.round((fig_width - 0.5) / (ncol + adjust_wspace * (ncol)), 3)
    if horizontal:
        ax_height = np.round(ax_width * (5 / 7.5), 1)
    else:
        ax_height = np.round(ax_width * (5 / 8.5), 1)
    calc_top = None
    if title_height is None:
        fig_height = np.round(
            (nrow * ax_height + adjust_hspace * ax_height * (nrow - 1)) / (adjust_top - adjust_bottom), 1)
    else:
        fig_height = np.round(
            (nrow * ax_height + adjust_hspace * ax_height * (nrow - 1) + title_height) / (1 - adjust_bottom), 1)
        calc_top = (fig_height - title_height) / fig_height

    if print:
        print("ax size: {} at ratio {}".format((ax_width, ax_height), ax_width / ax_height))
        print("figure_inches={}".format((fig_width, fig_height)))
        print("subplots_adjust_top={}".format(calc_top))
    return (fig_width, fig_height), calc_top


def _try_map(keys_or_indices, mapper, default_map_to_str=True):
    if (type(mapper) == list) or (type(mapper) == np.ndarray) or (type(mapper) == dict):
        if type(keys_or_indices) == pd.Series:
            return ["None" if k is None else mapper[k] for k in keys_or_indices.values]
        else:
            return ["None" if k is None else mapper[k] for k in keys_or_indices]
    elif default_map_to_str:
        return [str(k) for k in keys_or_indices]
    else:
        return keys_or_indices


def _bar_ticks(n, bar_width, n_subbar=1, i_subbar=None):
    if n_subbar == 1:
        if bar_width <= 1:
            return np.linspace(0, (n - 1), n, dtype=int)
        else:
            adjust_width = bar_width + np.round(np.log(bar_width), 1)
            return np.linspace(0, (n-1)*adjust_width, n)
    else:
        if bar_width*n_subbar <= 1:
            adjust_width = bar_width*n_subbar
        else:
            adjust_width = bar_width*n_subbar + np.round(np.log(bar_width*n_subbar), 1)

        if i_subbar is not None:
            return np.linspace(bar_width*i_subbar, bar_width*i_subbar + (n - 1) * adjust_width, n)
        else:
            return np.linspace(0, (n-1)*adjust_width, n) + np.round(bar_width*n_subbar/2 - bar_width/2, 1)


def _get_group_index_of_index(x, group_by):
    if type(group_by) == str:
        group_col = np.argwhere(np.array(x.index.names) == group_by)
        if (len(group_col) != 1) or (group_col[0][0] == -1):
            raise Exception("group_by index '{}' doesn't exist".format(group_by))
        else:
            return group_col[0][0]
    elif type(group_by) == int:
        if group_by >= len(x.index.names):
            raise Exception("Invalid group_by index '{}'".format(group_by))
        return group_by
    else:
        raise Exception("group_by must be a DataFrame's index name or DataFrame's index number")


def _get_group_index_of_columns(x, group_by):
    if type(group_by) == str:
        group_col = np.argwhere(np.array(x.columns.values) == group_by)
        if (len(group_col) != 1) or (group_col[0][0] == -1):
            raise Exception("group_by column '{}' doesn't exist".format(group_by))
        else:
            return group_col[0][0]
    elif type(group_by) == int:
        if group_by >= len(x.columns):
            raise Exception("Invalid group_by index '{}'".format(group_by))
        return group_by
    else:
        raise Exception("group_by must be a DataFrame's column name or DataFrame's column index")


def _continuous_color_map(z_arr, base_color):
    hue = 0.8
    if base_color is not None:
        rgb = colors.to_rgb(base_color)
        hue = colors.rgb_to_hsv(rgb)[0]
    vmin = np.nanmin(z_arr)
    vmax = np.nanmax(z_arr)
    if (vmax > 255) or (vmax < 200) or (vmin < 0) or (vmin > 150):
        return ScalarMappable(norm=Normalize(vmin=vmin, vmax=vmax),
                        cmap=sns.cubehelix_palette(as_cmap=True, hue=hue))
    else:
        return ScalarMappable(cmap=sns.cubehelix_palette(as_cmap=True, hue=hue))


def _auto_ylim1(val):
    upper = val if val > 0 else 0
    lower = val if val < 0 else 0
    return [lower, upper]


def _auto_ylim2(min_val, max_val, plot_type):
    if (plot_type == "bar") or (plot_type == "area") or (plot_type == "stackarea"):
        markup = max_val * 0.05 if max_val > 0 else 0
        markdown = min_val * 0.05 if min_val < 0 else 0

        upper = np.maximum(max_val * 1.05, max_val - markdown) if max_val > 0 else 0
        lower = np.minimum(min_val * 1.05, min_val - markup) if min_val < 0 else 0
    else:
        markup = np.abs(max_val * 0.05)
        markdown = np.abs(min_val * 0.05)

        upper = np.maximum(max_val * 1.05 if max_val > 0 else max_val * 0.95, max_val + markdown)
        lower = np.minimum(min_val * 1.05 if min_val < 0 else min_val * 0.95, min_val - markup)
    return [lower, upper]


# supported x examples:
# df index: (facet, x_numeric) {col0: y_numeric}
# df index: (facet, x_numeric) {col0: y_numeric, col1: z_numeric}
# df index: (facet, group, x_numeric) {col0: y_numeric}
# df index: (facet, group, x_numeric) {col0: y_numeric, col1: z_numeric}
def _facet_plot(x, plot_type, style=None, width=0.5, color=None, marker=None, marker_size=None, alpha=None, xlab=None,
                ylab=None, title=None, sort_by="", ascending=False,
                horizontal=False, figure_inches=None, y_scale_range=None, x_scale_ticks=None, x_scale_rotation=0,
                standardize_x_ticks_for_grouped_line_plots=False,
                x_scale_label_mapper=None, facet_label_mapper=None, subplots_ncol=4, subplots_adjust=None,
                subplots_adjust_top=None, subplots_adjust_bottom=0.0, subplots_adjust_hspace=0.2,
                subplots_adjust_wspace=0.2,
                facets_sort_by_value=None, facets_ascending=False,
                groups_sort_by_value=True, groups_ascending=False,
                group_label_mapper=None,
                legend_title=None, legend_loc="upper right", show=False):
    if (sort_by != "") and (sort_by != "count") and (sort_by != "label") and (sort_by != "x") and (sort_by != "y"):
        raise Exception("sort_by must be either 'count' or 'label' or 'x' or 'y'")
    if sort_by == "x":
        sort_by = "label"
    if sort_by == "y":
        sort_by = "count"

    if horizontal:
        ascending = not ascending

    plt.style.use("ggplot")

    if (type(x) == pd.DataFrame) and (type(x.index[0]) == tuple) and \
            ((len(x.index[0]) == 2) or (len(x.index[0]) == 3)) and \
            (((len(x.dtypes) == 1) and (
                    (str(x.dtypes[0]).find("float") >= 0) or (str(x.dtypes[0]).find("int") >= 0))) or (
                     (len(x.dtypes) == 2) and (
                     (str(x.dtypes[0]).find("float") >= 0) or (str(x.dtypes[0]).find("int") >= 0)) and (
                             (str(x.dtypes[1]).find("float") >= 0) or (str(x.dtypes[1]).find("int") >= 0)))):

        facet_index = 0
        x_index = 1 if len(x.index[0]) == 2 else 2
        group_index = 1 if len(x.index[0]) == 3 else None

        standardize_x_ticks = False
        if (plot_type == "stackarea") or (plot_type == "bar"):
            standardize_x_ticks = True
        elif plot_type == "area":
            standardize_x_ticks = True
            if (group_index is not None) and ((alpha is None) or (alpha == 1)):
                plot_type = "stackarea"
                print(
                    "Automatically changed plot type to 'stackarea'. Suppress this message by explicitly specifying the plot type as 'stackarea' or using <1 alpha value.")
        elif (plot_type == "line"):
            standardize_x_ticks = standardize_x_ticks_for_grouped_line_plots

        df_indices = x.index.values

        all_x_vals = [tup[x_index] for tup in df_indices]
        x_vals = pd.Series(all_x_vals).unique()

        all_y_vals = x.iloc[:, 0].values
        global_max_accum_y, global_min_accum_y = None, None
        global_max_y = np.max(np.nanmax(all_y_vals), 0)
        global_min_y = np.min(np.nanmin(all_y_vals), 0)

        all_facet_vals = [tup[facet_index] for tup in df_indices]
        facet_vals = None
        if facets_sort_by_value is not None:
            if (type(facets_sort_by_value) == bool) and (facets_sort_by_value == True):
                # 0:group, 2:f
                temp = pd.DataFrame({"f": all_facet_vals, "y": all_y_vals})
                temp.loc[: "y"] = temp.loc[: "y"].fillna(0)
                temp = temp.groupby(by="f").sum().sort_values(by="y", ascending=facets_ascending)
                facet_vals = temp.index.values
            elif type(facets_sort_by_value) == str:
                # 0:group, 2:f
                temp = pd.DataFrame({"f": all_facet_vals, "y": all_y_vals})
                temp.loc[: "y"] = temp.loc[: "y"].fillna(0)
                if facets_sort_by_value == "sum":
                    temp = temp.groupby(by="f").sum().sort_values(by="y", ascending=facets_ascending)
                elif facets_sort_by_value == "mean":
                    temp = temp.groupby(by="f").mean().sort_values(by="y", ascending=facets_ascending)
                elif facets_sort_by_value == "median":
                    temp = temp.groupby(by="f").median().sort_values(by="y", ascending=facets_ascending)
                elif (facets_sort_by_value == "sd") or (facets_sort_by_value == "std"):
                    temp = temp.groupby(by="f").std().sort_values(by="y", ascending=facets_ascending)
                facet_vals = temp.index.values
            else:
                facet_vals = pd.Series(all_facet_vals).sort_values(ascending=facets_ascending).unique()
        else:
            facet_vals = pd.Series(all_facet_vals).unique()

        group_vals = None
        if group_index is not None:
            group_vals = pd.Series([tup[group_index] for tup in df_indices]).unique()
            if (plot_type == "bar") or (plot_type == "stackarea"):
                temp = pd.DataFrame({
                    "f": all_facet_vals,
                    "x": all_x_vals,
                    "y": x.iloc[:, 0]}).groupby(["f", "x"]).sum()["y"]
                global_max_accum_y = np.max(np.nanmax(temp), 0)
                global_min_accum_y = np.min(np.nanmin(temp), 0)

        if subplots_ncol > len(facet_vals):
            subplots_ncol = len(facet_vals)
        subplot_nrow = int(math.ceil(len(facet_vals) / subplots_ncol))

        if group_vals is None:
            df_facet_spread = pd.DataFrame({"x": x_vals})
            for i, facet in enumerate(facet_vals):
                df_facet_spread = df_facet_spread.merge(x.loc[facet, :], how="left", left_on="x", right_index=True)
            if len(x.dtypes) == 1:
                df_facet_spread.columns = ["x"] + ["y_{}".format(i) for i in range(len(facet_vals))]
            else:
                df_facet_spread.columns = ["x"] + list(np.array([["y_{}".format(i), "z_{}".format(i)] for i in range(len(facet_vals))]).flatten())

            if standardize_x_ticks:
                df_facet_spread.iloc[:, 1:] = df_facet_spread.iloc[:, 1:].fillna(0).values
        else:
            df_facet_spread = cartesian_dataframe(pd.DataFrame({"group": group_vals}), pd.DataFrame({"x": x_vals}))
            for i, facet in enumerate(facet_vals):
                df_facet_spread = df_facet_spread.merge(x.loc[facet, :], how="left", left_on=["group", "x"],
                                                        right_index=True)
            if len(x.dtypes) == 1:
                df_facet_spread.columns = ["group", "x"] + ["f_{}".format(i) for i in range(len(facet_vals))]
            else:
                df_facet_spread.columns = ["group", "x"] + list(np.array([["f_{}".format(i), "fz_{}".format(i)] for i in range(len(facet_vals))]).flatten())

            if standardize_x_ticks:
                df_facet_spread.iloc[:, 2:] = df_facet_spread.iloc[:, 2:].fillna(0).values

        fig, axes = plt.subplots(subplot_nrow, subplots_ncol)
        n_hidden_axes = subplot_nrow * subplots_ncol % len(facet_vals)
        if (n_hidden_axes > 0) and (subplot_nrow > 1):
            for hid in range(subplots_ncol - n_hidden_axes, subplots_ncol):
                axes[-1, hid].axis("off")

        if subplots_adjust is not None:
            plt.subplots_adjust(top=subplots_adjust[0], bottom=subplots_adjust[1], hspace=subplots_adjust[2],
                                wspace=subplots_adjust[3])
            subplots_adjust_top = subplots_adjust[0]
            subplots_adjust_bottom = subplots_adjust[1]
            subplots_adjust_hspace = subplots_adjust[2]
            subplots_adjust_wspace = subplots_adjust[3]
        else:
            if subplots_adjust_top is not None:
                plt.subplots_adjust(top=subplots_adjust_top)
            if subplots_adjust_bottom is not None:
                plt.subplots_adjust(bottom=subplots_adjust_bottom)
            if subplots_adjust_hspace is not None:
                plt.subplots_adjust(hspace=subplots_adjust_hspace)
            if subplots_adjust_wspace is not None:
                plt.subplots_adjust(wspace=subplots_adjust_wspace)

        if figure_inches is not None:
            fig.set_size_inches(figure_inches[0], figure_inches[1])
        else:
            if (title is not None) and (title != ""):
                auto_size, new_top = auto_figure_size(subplots_ncol, subplot_nrow,
                                                      1,
                                                      subplots_adjust_bottom,
                                                      subplots_adjust_hspace,
                                                      subplots_adjust_wspace,
                                                      title_height=0.5, horizontal=horizontal)
                if subplots_adjust_top is None:
                    plt.subplots_adjust(top=new_top)
            else:
                auto_size, _ = auto_figure_size(subplots_ncol, subplot_nrow,
                                                1 if subplots_adjust_top is None else subplots_adjust_top,
                                                subplots_adjust_bottom,
                                                subplots_adjust_hspace,
                                                subplots_adjust_wspace, horizontal=horizontal)
            fig.set_size_inches(auto_size[0], auto_size[1])

        plots = list()
        group_lbls = None
        for i, facet in enumerate(facet_vals):
            # i, facet = 0, facet_vals[0]
            ax_row = int(i / subplots_ncol)
            ax_col = i % subplots_ncol
            ax = None
            if (subplot_nrow > 1) and (subplots_ncol > 1):
                ax = axes[ax_row, ax_col]
            elif subplot_nrow == 1:
                ax = axes[ax_col]
            elif subplots_ncol == 1:
                ax = axes[ax_row]

            # no grouping
            if group_index is None:
                y_col_name = "y_{}".format(i)
                z_col_name = "z_{}".format(i)

                if plot_type == "bar":
                    df = df_facet_spread.loc[:, ["x", y_col_name]]
                    if sort_by != "":
                        df = df.sort_values(by=y_col_name if sort_by == "count" else "x", ascending=ascending)

                    x_labels = _try_map(df.x, x_scale_label_mapper)
                    x_ticks = list(range(len(x_labels)))
                    clr = color[i] if (type(color) == list) or (type(color) == np.ndarray) else color
                    if horizontal:
                        ax.barh(x_labels, df.loc[:, y_col_name], width, color=clr)
                    else:
                        ax.bar(x_labels, df.loc[:, y_col_name], width, color=clr)
                else:
                    if len(x.dtypes) == 1:
                        df = df_facet_spread.loc[:, ["x", y_col_name]]
                    else:
                        df = df_facet_spread.loc[:, ["x", y_col_name, z_col_name]]

                    filt = pd.isna(df_facet_spread.loc[:, y_col_name]) == False
                    df = df.sort_values(by="x", ascending=True)
                    facet_x_vals = df.loc[filt, "x"].values
                    facet_y_vals = df.loc[filt, y_col_name].values
                    facet_z_vals = df.loc[filt, z_col_name].values if len(x.dtypes) == 2 else None

                    if (plot_type == "point") or (plot_type == "scatter"):
                        if facet_z_vals is not None:
                            if (color is not None) and (color != ""):
                                cmap = _continuous_color_map(facet_z_vals, color).get_cmap()
                                ax.scatter(facet_x_vals, facet_y_vals, c=facet_z_vals, cmap=cmap, marker=marker, s=marker_size,
                                       alpha=1 if alpha is None else alpha)
                            else:
                                ax.scatter(facet_x_vals, facet_y_vals, marker=marker, s=facet_z_vals,
                                           alpha=0.3 if alpha is None else alpha)
                        elif (type(color) == str) and (color != ""):
                            ax.scatter(facet_x_vals, facet_y_vals, c=np.repeat(color, len(facet_x_vals)), marker=marker,
                                   s=marker_size,
                                   alpha=1 if alpha is None else alpha)
                        elif (type(color) == list) or (type(color) == np.ndarray):
                            ax.scatter(facet_x_vals, facet_y_vals, c=np.repeat(color[i], len(facet_x_vals)),
                                       marker=marker,
                                       s=marker_size,
                                       alpha=1 if alpha is None else alpha)
                        else:
                            ax.scatter(facet_x_vals, facet_y_vals, marker=marker, s=marker_size,
                                       alpha=1 if alpha is None else alpha)

                    elif plot_type == "line":
                        clr = color[i] if (type(color) == list) or (type(color) == np.ndarray) else color
                        ax.plot(facet_x_vals, facet_y_vals, linewidth=width, linestyle=style, color=clr,
                                marker=marker,
                                markersize=marker_size, alpha=1 if alpha is None else alpha)
                    elif plot_type == "area":
                        clr = color[i] if (type(color) == list) or (type(color) == np.ndarray) else color
                        ax.fill_between(facet_x_vals.astype(float), facet_y_vals, color=clr, alpha=1 if alpha is None else alpha)
                    else:
                        raise Exception("plot type '{}' not supported".format(plot_type))

                    x_ticks = ax.get_xticks()
                    x_labels = x_ticks

                facet_label = _try_map([facet], facet_label_mapper)[0]
                if (facet_label is not None) and (facet_label != ""):
                    ax.set_xlabel(facet_label)

                if y_scale_range is not None:
                    if type(y_scale_range) == dict:
                        scale_range = y_scale_range[facet]
                    else:
                        scale_range = y_scale_range
                    if horizontal:
                        if (type(scale_range) == tuple) or (type(scale_range) == list):
                            ax.set_xlim([scale_range[0], scale_range[1]])
                        elif (type(scale_range) == str) and (scale_range == "fixed"):
                            ax.set_xlim(_auto_ylim2(global_min_y, global_max_y, plot_type))
                        elif (type(scale_range) == int) or (type(scale_range) == float):
                            ax.set_xlim(_auto_ylim1(scale_range))
                    else:
                        if (type(scale_range) == tuple) or (type(scale_range) == list):
                            ax.set_ylim([scale_range[0], scale_range[1]])
                        elif (type(scale_range) == str) and (scale_range == "fixed"):
                            ax.set_ylim(_auto_ylim2(global_min_y, global_max_y, plot_type))
                        elif (type(scale_range) == int) or (type(scale_range) == float):
                            ax.set_ylim(_auto_ylim1(scale_range))

                if (type(x_scale_ticks) == list) or (type(x_scale_ticks) == np.ndarray):
                    if _is_numeric_array(x_scale_ticks, consider_datetime=True):
                        x_ticks = x_scale_ticks
                        x_labels = x_scale_ticks
                    else:
                        x_ticks = np.linspace(np.nanmin(facet_x_vals), np.nanmax(facet_x_vals), len(x_scale_ticks),
                                              dtype=facet_x_vals.dtype)
                        x_labels = x_scale_ticks
                elif type(x_scale_ticks) == dict:
                    x_ticks = list(x_scale_ticks.keys())
                    x_labels = list(x_scale_ticks.values())

                if horizontal:
                    ax.set_yticks(x_ticks)
                    if (ax_col == 0) or (sort_by == "count"):
                        if (x_scale_rotation is not None) and (x_scale_rotation > 0):
                            ax.set_yticklabels(x_labels, rotation=x_scale_rotation)
                        else:
                            ax.set_yticklabels(x_labels)
                    else:
                        ax.set_yticklabels([])
                else:
                    ax.set_xticks(x_ticks)
                    if (ax_row == subplot_nrow - 1) or (
                            (ax_row == subplot_nrow - 2) and (ax_col >= (subplots_ncol - n_hidden_axes))) or \
                            (sort_by == "count"):
                        if (x_scale_rotation is not None) and (x_scale_rotation > 0):
                            ax.set_xticklabels(x_labels, rotation=x_scale_rotation)
                        else:
                            ax.set_xticklabels(x_labels)
                    else:
                        ax.set_xticklabels([])

            # with group
            else:
                f_col_name = "f_{}".format(i)
                fz_col_name = "fz_{}".format(i)
                if len(x.dtypes) == 1:
                    df_current_facet = df_facet_spread.loc[:, ["group", "x", f_col_name]]
                else:
                    df_current_facet = df_facet_spread.loc[:, ["group", "x", f_col_name, fz_col_name]]

                if groups_sort_by_value is not None:
                    if (type(groups_sort_by_value) == bool) and (groups_sort_by_value == True):
                        temp = df_current_facet.loc[:, ["group", f_col_name]]
                        temp.loc[:, f_col_name] = temp.loc[:, f_col_name].fillna(0)
                        temp = temp.groupby(by="group").sum().sort_values(by=f_col_name,
                                                                          ascending=groups_ascending)
                        group_vals = temp.index.values
                    elif type(groups_sort_by_value) == str:
                        temp = df_current_facet.loc[:, ["group", f_col_name]]
                        temp.loc[:, f_col_name] = temp.loc[:, f_col_name].fillna(0)
                        if groups_sort_by_value == "sum":
                            temp = temp.groupby(by="group").sum().sort_values(by=f_col_name,
                                                                              ascending=groups_ascending)
                        elif groups_sort_by_value == "mean":
                            temp = temp.groupby(by="group").mean().sort_values(by=f_col_name,
                                                                              ascending=groups_ascending)
                        elif groups_sort_by_value == "median":
                            temp = temp.groupby(by="group").median().sort_values(by=f_col_name,
                                                                              ascending=groups_ascending)
                        elif (groups_sort_by_value == "sd") or (groups_sort_by_value == "std"):
                            temp = temp.groupby(by="group").std().sort_values(by=f_col_name,
                                                                              ascending=groups_ascending)
                        group_vals = temp.index.values
                    else:
                        group_vals = df_current_facet.loc[:, "group"].sort_values(ascending=groups_ascending).unique()
                else:
                    group_vals = df_current_facet.loc[:, "group"].unique()
                group_lbls = _try_map(group_vals, group_label_mapper)

                df = pd.DataFrame({"x": x_vals})
                if len(x.dtypes) == 1:
                    for group_val in group_vals:
                        df = df.merge(df_current_facet.loc[df_current_facet["group"] == group_val, ["x", f_col_name]],
                                  how="left", left_on="x", right_on="x")
                    df.columns = ["x"] + ["y_{}".format(g) for g in range(len(group_vals))]
                else:
                    for group_val in group_vals:
                        df = df.merge(df_current_facet.loc[
                                          df_current_facet["group"] == group_val, ["x", f_col_name, fz_col_name]],
                                      how="left", left_on="x", right_on="x")
                    df.columns = ["x"] + list(
                        np.array([["y_{}".format(g), "z_{}".format(g)] for g in range(len(group_vals))]).flatten())
                if standardize_x_ticks:
                    df.iloc[:, 1:] = df.iloc[:, 1:].fillna(0)
                df["accum_y"] = df.apply(lambda r: np.nansum(r[1::len(x.dtypes)]), axis=1).values

                facet_max_y, facet_min_y = None, None

                if plot_type == "bar":
                    if len(x.dtypes) > 1:
                        raise Exception("z value is not supported for bar plot.")

                    if sort_by != "":
                        df = df.sort_values(by="accum_y" if sort_by == "count" else "x", ascending=ascending)
                        x_vals = df.x.values

                    x_labels = _try_map(x_vals, x_scale_label_mapper)

                    if style == "stack":
                        x_ticks = _bar_ticks(len(x_vals), width)
                        bottom = np.zeros(len(x_vals))
                        for grp, group_val in enumerate(group_vals):
                            # grp, group_val = 1, group_vals[1]
                            grp_y_vals = df.iloc[:, grp + 1].values
                            clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
                            if horizontal:
                                plots.append(ax.barh(x_ticks, grp_y_vals, width, left=bottom, color=clr))
                            else:
                                plots.append(ax.bar(x_ticks, grp_y_vals, width, bottom=bottom, color=clr))
                            bottom = bottom + grp_y_vals
                        facet_max_y, facet_min_y = np.max(np.nanmax(df.accum_y.values), 0), np.min(
                            np.nanmin(df.accum_y.values), 0)

                    elif style == "dodge":
                        for grp, group_val in enumerate(group_vals):
                            x_ticks = _bar_ticks(len(x_vals), width, n_subbar=len(group_vals), i_subbar=grp)
                            grp_y_vals = df.iloc[:, grp + 1].values
                            clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
                            if horizontal:
                                plots.append(ax.barh(x_ticks, grp_y_vals, width, color=clr))
                            else:
                                plots.append(ax.bar(x_ticks, grp_y_vals, width, color=clr))
                        x_ticks = _bar_ticks(len(x_vals), width, n_subbar=len(group_vals))
                        facet_max_y, facet_min_y = np.max(np.nanmax(df.iloc[:, 1:-1]), 0), np.min(
                            np.nanmin(df.iloc[:, 1:-1]), 0)

                elif plot_type == "stackarea":
                    if len(x.dtypes) > 1:
                        raise Exception("z value is not supported for stackarea plot.")

                    grp_x_vals = df.x.values
                    grp_y_vals = df.iloc[:, 1:-1].values.transpose()

                    if color is not None:
                        if type(color) == str:
                            ax.stackplot(grp_x_vals.astype(float), grp_y_vals, alpha=1 if alpha is None else alpha)
                            ax.plot(grp_x_vals, df.accum_y.values, color=color, linewidth=width, linestyle="dotted",
                                    marker=marker,
                                    markersize=marker_size, alpha=1 if alpha is None else alpha)
                        elif (type(color) == list) or (type(color) == np.ndarray):
                            ax.stackplot(grp_x_vals.astype(float), grp_y_vals, colors=color, alpha=1 if alpha is None else alpha)
                    else:
                        ax.stackplot(grp_x_vals.astype(float), grp_y_vals, alpha=1 if alpha is None else alpha)

                    x_ticks = ax.get_xticks()
                    x_labels = x_ticks
                    facet_max_y, facet_min_y = np.max(np.nanmax(df.accum_y.values), 0), np.min(
                        np.nanmin(df.accum_y.values), 0)

                else:
                    df = df.sort_values(by="x", ascending=True)
                    for grp, group_val in enumerate(group_vals):
                        y_col_name = "y_{}".format(grp)
                        z_col_name = "z_{}".format(grp)
                        filt = pd.isna(df.loc[:, y_col_name]) == False
                        grp_x_vals = df.loc[filt, "x"].values
                        grp_y_vals = df.loc[filt, y_col_name].values
                        grp_z_vals = df.loc[filt, z_col_name].values if len(x.dtypes) == 2 else None
                        clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None

                        if (plot_type == "point") or (plot_type == "scatter"):
                            if grp_z_vals is not None:
                                plots.append(ax.scatter(grp_x_vals, grp_y_vals, marker=marker, s=grp_z_vals, c=clr,
                                           alpha=0.3 if alpha is None else alpha))
                            else:
                                plots.append(ax.scatter(grp_x_vals, grp_y_vals, marker=marker, s=marker_size, c=clr,
                                           alpha=1 if alpha is None else alpha))
                        elif plot_type == "line":
                            ax.plot(grp_x_vals, grp_y_vals, linewidth=width, linestyle=style, color=clr,
                                    marker=marker,
                                    markersize=marker_size, alpha=1 if alpha is None else alpha)
                        elif plot_type == "area":
                            ax.fill_between(grp_x_vals.astype(float), grp_y_vals, color=clr, alpha=1 if alpha is None else alpha)
                        else:
                            raise Exception("plot type '{}' is not supported.".format(plot_type))

                    x_ticks = ax.get_xticks()
                    x_labels = x_ticks
                    facet_max_y, facet_min_y = np.max(np.nanmax(df.iloc[:, 1:-1:len(x.dtypes)]), 0), np.min(
                        np.nanmin(df.iloc[:, 1:-1:len(x.dtypes)]), 0)

                facet_label = _try_map([facet], facet_label_mapper)[0]
                if (facet_label is not None) and (facet_label != ""):
                    ax.set_xlabel(facet_label)

                if y_scale_range is not None:
                    if type(y_scale_range) == dict:
                        scale_range = y_scale_range[facet]
                    else:
                        scale_range = y_scale_range
                    if horizontal:
                        if (type(scale_range) == tuple) or (type(scale_range) == list):
                            ax.set_xlim([scale_range[0], scale_range[1]])
                        elif (type(scale_range) == str) and (scale_range == "fixed"):
                            if global_min_accum_y is not None:
                                ax.set_xlim(_auto_ylim2(global_min_accum_y, global_max_accum_y, plot_type))
                            else:
                                ax.set_xlim(_auto_ylim2(global_min_y, global_max_y, plot_type))
                        elif (type(scale_range) == int) or (type(scale_range) == float):
                            ax.set_xlim(_auto_ylim1(scale_range))
                    else:
                        if (type(scale_range) == tuple) or (type(scale_range) == list):
                            ax.set_ylim([scale_range[0], scale_range[1]])
                        elif (type(scale_range) == str) and (scale_range == "fixed"):
                            if global_min_accum_y is not None:
                                ax.set_ylim(_auto_ylim2(global_min_accum_y, global_max_accum_y, plot_type))
                            else:
                                ax.set_ylim(_auto_ylim2(global_min_y, global_max_y, plot_type))
                        elif (type(scale_range) == int) or (type(scale_range) == float):
                            ax.set_ylim(_auto_ylim1(scale_range))
                else:
                    if horizontal:
                        ax.set_xlim(_auto_ylim2(facet_min_y, facet_max_y, plot_type))
                    else:
                        ax.set_ylim(_auto_ylim2(facet_min_y, facet_max_y, plot_type))

                if (type(x_scale_ticks) == list) or (type(x_scale_ticks) == np.ndarray):
                    if _is_numeric_array(x_scale_ticks, consider_datetime=True):
                        x_ticks = x_scale_ticks
                        x_labels = x_scale_ticks
                    else:
                        filt = pd.isna(df_facet_spread.iloc[:, 1]) == False
                        facet_x_vals = df_facet_spread.loc[filt, "x"].values

                        x_ticks = np.linspace(np.nanmin(facet_x_vals), np.nanmax(facet_x_vals), len(x_scale_ticks),
                                              dtype=facet_x_vals.dtype)
                        x_labels = x_scale_ticks
                elif type(x_scale_ticks) == dict:
                    x_ticks = list(x_scale_ticks.keys())
                    x_labels = list(x_scale_ticks.values())

                if horizontal:
                    ax.set_yticks(x_ticks)
                    if (ax_col == 0) or (sort_by == "count"):
                        if (x_scale_rotation is not None) and (x_scale_rotation > 0):
                            ax.set_yticklabels(x_labels, rotation=x_scale_rotation)
                        else:
                            ax.set_yticklabels(x_labels)
                    else:
                        ax.set_yticklabels([])
                else:
                    ax.set_xticks(x_ticks)
                    if (ax_row == subplot_nrow - 1) or (
                            (ax_row == subplot_nrow - 2) and (ax_col >= (subplots_ncol - n_hidden_axes))) or \
                            (sort_by == "count"):
                        if (x_scale_rotation is not None) and (x_scale_rotation > 0):
                            ax.set_xticklabels(x_labels, rotation=x_scale_rotation)
                        else:
                            ax.set_xticklabels(x_labels)
                    else:
                        ax.set_xticklabels([])

        if (group_index is not None) and (legend_loc is not None):
            if len(plots) > 0:
                fig.legend(tuple(plots), tuple(group_lbls), title=legend_title, facecolor="white", loc=legend_loc,
                       prop={'size': 10}, fontsize=8,
                       ncol=1)
            else:
                fig.legend(tuple(group_lbls), title=legend_title, facecolor="white", loc=legend_loc,
                           prop={'size': 10}, fontsize=8,
                           ncol=1)

        if xlab is not None:
            if horizontal:
                fig.text(0.04, 0.5, xlab, va='center', rotation='vertical')
            else:
                fig.text(0.5, 0.04, xlab, ha='center')
        if ylab is not None:
            if horizontal:
                fig.text(0.5, 0.04, ylab, ha='center')
            else:
                fig.text(0.04, 0.5, ylab, va='center', rotation='vertical')
        if title is not None:
            fig.suptitle(title, size=16)
        if show:
            fig.show()
        else:
            return fig, axes, plots
    else:
        raise Exception(
            "x must be a DataFrame with 1 numeric column, 2 indices (without group_by) or 3 indices (with group_by).")


def _barplot_grouped(x, x_col, y_col, group_col, group_position, width, color, x_scale_label_mapper,
                     groups_sort_by_value, groups_ascending, sort_by, ascending, group_label_mapper, horizontal,
                         legend_loc, legend_title):
    x_labels = []
    x_ticks = []

    x_vals = x.iloc[:, x_col].unique()
    if groups_sort_by_value is not None:
        if (type(groups_sort_by_value) == bool) and (groups_sort_by_value == True):
            temp = x.iloc[:, [y_col, group_col]].groupby(
                by=x.columns.values[group_col]).sum().sort_values(by=x.columns.values[y_col],
                                                                  ascending=groups_ascending)
            group_vals = temp.index.values
        elif type(groups_sort_by_value) == str:
            if groups_sort_by_value == "sum":
                temp = x.iloc[:, [y_col, group_col]].groupby(
                    by=x.columns.values[group_col]).sum().sort_values(by=x.columns.values[y_col],
                                                                      ascending=groups_ascending)
            elif groups_sort_by_value == "mean":
                temp = x.iloc[:, [y_col, group_col]].groupby(
                    by=x.columns.values[group_col]).mean().sort_values(by=x.columns.values[y_col],
                                                                      ascending=groups_ascending)
            elif groups_sort_by_value == "median":
                temp = x.iloc[:, [y_col, group_col]].groupby(
                    by=x.columns.values[group_col]).median().sort_values(by=x.columns.values[y_col],
                                                                      ascending=groups_ascending)
            elif (groups_sort_by_value == "sd") or (groups_sort_by_value == "std"):
                temp = x.iloc[:, [y_col, group_col]].groupby(
                    by=x.columns.values[group_col]).std().sort_values(by=x.columns.values[y_col],
                                                                      ascending=groups_ascending)
            group_vals = temp.index.values
        else:
            group_vals = x.iloc[:, group_col].sort_values(ascending=groups_ascending).unique()
    else:
        group_vals = x.iloc[:, group_col].unique()
    group_lbls = _try_map(group_vals, group_label_mapper)

    aggregated = x.iloc[:, [x_col, y_col, group_col]].groupby(
        by=[x.columns[group_col], x.columns[x_col]]).sum()

    df = pd.DataFrame({"x": x_vals})
    for group_val in group_vals:
        df = df.merge(aggregated.loc[group_val, :], how="left", left_on="x", right_index=True)
    df.columns = ["x"] + ["y_{}".format(g) for g in range(len(group_vals))]
    df.iloc[:, 1:] = df.iloc[:, 1:].fillna(0)
    df["y"] = df.apply(lambda r: np.sum(r[1:]), axis=1).values

    if sort_by != "":
        df = df.sort_values(by="y" if sort_by == "count" else "x", ascending=ascending)
        x_vals = df.x.values

    x_labels = _try_map(x_vals, x_scale_label_mapper)
    max_y = None

    if group_position == "stack":
        x_ticks = _bar_ticks(len(x_vals), width)
        bottom = np.zeros(len(x_vals))
        for grp, group_val in enumerate(group_vals):
            y_vals = df.iloc[:, grp + 1].values
            clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
            if horizontal:
                plt.barh(x_ticks, y_vals, width, left=bottom, label=group_lbls[grp], color=clr)
            else:
                plt.bar(x_ticks, y_vals, width, bottom=bottom, label=group_lbls[grp], color=clr)
            bottom = bottom + y_vals
        max_y = np.nanmax(df.y.values)

    elif group_position == "dodge":
        for grp, group_val in enumerate(group_vals):
            x_ticks = _bar_ticks(len(x_vals), width, n_subbar=len(group_vals), i_subbar=grp)
            y_vals = df.iloc[:, grp + 1].values
            clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
            if horizontal:
                plt.barh(x_ticks, y_vals, width, label=group_lbls[grp], color=clr)
            else:
                plt.bar(x_ticks, y_vals, width, label=group_lbls[grp], color=clr)
        x_ticks = _bar_ticks(len(x_vals), width, n_subbar=len(group_vals))
        max_y = np.nanmax(df.iloc[:, 1:-1])

    if horizontal:
        plt.xlim([0, max_y * 1.05])
    else:
        plt.ylim([0, max_y * 1.05])

    if legend_loc is not None:
        plt.legend(title=legend_title, facecolor="white", loc=legend_loc, prop={'size': 10}, fontsize=8, ncol=1)

    return x_ticks, x_labels


def barplot(x, y=None, width=0.5, color=None, xlab=None, ylab=None, title=None, sort_by="", ascending=False,
            horizontal=False,  x_scale_rotation=0, x_scale_label_mapper=None,
            group_by=None, group_position="stack", groups_sort_by_value=True, groups_ascending=False, group_label_mapper=None,
            legend_title=None, legend_loc="upper right", figure_inches=None, show=True):
    """
    Supported x, y examples:
    x_categorical_arr
    x_categorical_arr, y_numeric_arr
    DataFrame: {col0: x_categorical, col1: y_numeric, ...}
    DataFrame: {col0: x_categorical, col1: y_numeric, col2: group_by, ...}
    DataFrame index: (x_categorical) {col0: y_numeric}
    DataFrame index: (group_by, x_categorical) {col0: y_numeric}, if group_by is set
    DataFrame index: (facet_by, x_categorical) {col0: y_numeric}, if group_by is not set
    DataFrame index: (facet_by, group_by, x_categorical) {col0: y_numeric}
    :param x: array or DataFrame.
    :param y: numeric array for y-axis, or None. when y is set, x must not be a DataFrame
    :param width: width of the bar
    :param color: color of the bar
    :param xlab: x-axis's label
    :param ylab: y-axis's label
    :param title: plot's title
    :param sort_by: 'count', 'label', 'x', 'y', or empty.
    :param ascending:
    :param horizontal:
    :param x_scale_rotation:
    :param x_scale_label_mapper:
    :param group_by:
    :param group_position: 'stack', 'dodged' or empty
    :param groups_sort_by_value:
    :param groups_ascending:
    :param group_label_mapper:
    :param legend_title:
    :param legend_loc:
    :param show:
    :return: return None when show=True, return the Figure object when show=False
    """

    if (sort_by != "") and (sort_by != "count") and (sort_by != "label") and (sort_by != "x") and (sort_by != "y"):
        raise Exception("sort_by must be either 'count' or 'label' or 'x' or 'y'")
    if sort_by == "x":
        sort_by = "label"
    if sort_by == "y":
        sort_by = "count"

    if horizontal:
        ascending = not ascending

    plt.style.use("ggplot")

    x_labels = []
    x_ticks = []

    if y is None:
        # if x is 1-D categorical data
        if (type(x) == list) or (type(x) == np.ndarray) or (type(x) == pd.Series):
            grouped = _summarize_categorical(x, include_na_only_if_exist=True, sort_by=sort_by, ascending=ascending)
            x_labels = _try_map(grouped.index, x_scale_label_mapper)
            x_ticks = _bar_ticks(len(x_labels), width)
            if horizontal:
                plt.barh(x_ticks, grouped.Count, width, color=color)
            else:
                plt.bar(x_ticks, grouped.Count, width, color=color)

        # if x is a DataFrame
        elif type(x) == pd.DataFrame:
            # if x is a normal unaggregated DataFrame with 2 or more columns
            # (col_1 will be the category, col_2 will be aggregated as count)
            # if group_by is specified, it has to be specified as column index or column name
            if len(x.dtypes) > 1:
                group_col = None
                x_col = 0
                y_col = 1

                if (group_by is not None) and (group_by != ""):
                    group_col = _get_group_index_of_columns(x, group_by)
                    if group_col == 0:
                        x_col = 1
                        y_col = 2
                    elif group_col == 1:
                        y_col = 2

                if group_col is None:
                    aggregated = x.iloc[:, [x_col, y_col]].groupby(by=x.columns[x_col]).sum()
                    x_vals = aggregated.index.values
                    y_vals = aggregated.iloc[:, x_col].values

                    x_ticks = _bar_ticks(len(x_vals), width)

                    if sort_by != "":
                        df = pd.DataFrame({"x": x_vals, "y": y_vals}).sort_values(
                            by="y" if sort_by == "count" else "x", ascending=ascending)
                        x_labels = _try_map(df.x, x_scale_label_mapper)
                        if horizontal:
                            plt.barh(x_ticks, df.y, width, color=color)
                        else:
                            plt.bar(x_ticks, df.y, width, color=color)
                    elif horizontal:
                        x_labels = _try_map(x_vals, x_scale_label_mapper)
                        plt.barh(x_ticks, y_vals, width, color=color)
                    else:
                        x_labels = _try_map(x_vals, x_scale_label_mapper)
                        plt.bar(x_ticks, y_vals, width, color=color)

                else:
                    x_ticks, x_labels = _barplot_grouped(x, x_col, y_col, group_col, group_position, width, color,
                                                         x_scale_label_mapper,
                                                         groups_sort_by_value, groups_ascending, sort_by, ascending,
                                                         group_label_mapper,
                                                         horizontal, legend_loc, legend_title)

            # if x is a group_by DataFrame with only 1 aggregated numeric column
            elif (str(x.dtypes[0]).find("float") >= 0) or (str(x.dtypes[0]).find("int") >= 0):
                # dual-indices
                # if group_col exists, one index will be used for grouping, the other index is used as x
                # if no group_col, the first index will be used for facet, the 2nd index is used as x
                if (type(x.index[0]) == tuple) and (len(x.index[0]) == 2):
                    if (group_by is not None) and (group_by != ""):
                        group_col = _get_group_index_of_index(x, group_by)
                        df = pd.DataFrame({
                            "group": [tup[group_col] for tup in x.index],
                            "x": [tup[1 if group_col == 0 else 0] for tup in x.index],
                            "y": x.iloc[:, 0]})

                        x_ticks, x_labels = _barplot_grouped(df, 1, 2, 0, group_position, width, color,
                                                             x_scale_label_mapper,
                                                             groups_sort_by_value, groups_ascending, sort_by, ascending,
                                                             group_label_mapper,
                                                             horizontal, legend_loc, legend_title)
                    else:
                        barplot2(x, width=width, color=color, xlab=xlab, ylab=ylab, title=title,
                                                      sort_by=sort_by, ascending=ascending, horizontal=horizontal,
                                                      y_scale_range="fixed",
                                                      x_scale_rotation=x_scale_rotation,
                                                      x_scale_label_mapper=x_scale_label_mapper, figure_inches=figure_inches, show=show)
                        return

                # tri-indices with group_by
                # one index will be used for grouping, one for facet, the last index is used as x
                elif (type(x.index[0]) == tuple) and (len(x.index[0]) == 3) and (group_by is not None) and (
                                group_by != ""):
                    group_col = _get_group_index_of_index(x, group_by)
                    if group_col != 1:
                        raise Exception("group_by must be the 2nd index of the DataFrame's index.")
                    barplot2(x, width=width, color=color, xlab=xlab, ylab=ylab, title=title,
                             sort_by=sort_by, ascending=ascending, horizontal=horizontal,
                             y_scale_range="fixed",
                             x_scale_rotation=x_scale_rotation,
                             x_scale_label_mapper=x_scale_label_mapper,
                             group_position=group_position, groups_sort_by_value=groups_sort_by_value,
                             groups_ascending=groups_ascending,
                             group_label_mapper=group_label_mapper,
                             legend_title=legend_title, legend_loc=legend_loc, figure_inches=figure_inches, show=show)
                    return

                # single-index or multiple-indices
                else:
                    labels = [""] * len(x.index)
                    x_ticks = _bar_ticks(len(labels), width)
                    for i, indices in enumerate(x.index):
                        # multiple-indices
                        if type(indices) == tuple:
                            labels[i] = "/".join([str(v) for v in indices])
                        # single-index
                        else:
                            labels[i] = indices

                    if sort_by != "":
                        df = pd.DataFrame({"x": labels, "y": x.iloc[:, 0]}).sort_values(
                            by="y" if sort_by == "count" else "x", ascending=ascending)
                        x_labels = _try_map(df.x, x_scale_label_mapper)
                        if horizontal:
                            plt.barh(x_ticks, df.y, width, color=color)
                        else:
                            plt.bar(x_ticks, df.y, width, color=color)
                    elif horizontal:
                        x_labels = _try_map(labels, x_scale_label_mapper)
                        plt.barh(x_ticks, x.iloc[:, 0], width, color=color)
                    else:
                        x_labels = _try_map(labels, x_scale_label_mapper)
                        plt.bar(x_ticks, x.iloc[:, 0], width, color=color)

            else:
                raise Exception(
                    "Supported DataFrame formats: "
                    "{col0: x_label, col1: y_numeric, ...}, "
                    "{col0: x_label, col1: y_numeric, col2: group_by, ...}, "
                    "index: (x_label) {col0: y_numeric}, "
                    "index: (group, x_label) {col0: y_numeric}, "
                    "index: (facet, x_label) {col0: y_numeric}, "
                    "index: (facet, group, x_label) {col0: y_numeric}")
        else:
            raise Exception("Unsupported type {} for x".format(type(x)))

    # if x is 1-D categorical data, and y is 1-D numeric
    elif ((type(x) == list) or (type(x) == np.ndarray) or (type(x) == pd.Series) or (type(x) == pd.core.arrays.categorical.Categorical)) and \
            ((type(y) == list) or (type(y) == np.ndarray) or (type(y) == pd.Series)):
        df = pd.DataFrame({"x": x, "y": y})
        x_labels = _try_map(df.x, x_scale_label_mapper)
        x_ticks = _bar_ticks(len(x_labels), width)

        if sort_by != "":
            df = df.sort_values(by="y" if sort_by == "count" else "x", ascending=ascending)
            x_labels = _try_map(df.x, x_scale_label_mapper)
            if horizontal:
                plt.barh(x_ticks, df.y, width, color=color)
            else:
                plt.bar(x_ticks, df.y, width, color=color)
        elif horizontal:
            plt.barh(x_ticks, df.y, width, color=color)
        else:
            plt.bar(x_ticks, df.y, width, color=color)

    else:
        raise Exception("Unsupported type {} for x, or {} for y".format(type(x), type(y)))

    if horizontal:
        plt.yticks(x_ticks, x_labels, rotation=x_scale_rotation)
    else:
        plt.xticks(x_ticks, x_labels, rotation=x_scale_rotation)

    if figure_inches is not None:
        plt.figure().set_size_inches(figure_inches[0], figure_inches[1])
    if xlab is not None:
        plt.xlabel(xlab)
    if ylab is not None:
        plt.ylabel(ylab)
    if title is not None:
        plt.title(title)
    if show:
        plt.show()
    else:
        return plt.figure()


def barplot2(x, width=0.5, color=None, xlab=None, ylab=None, title=None, sort_by="", ascending=False,
                 horizontal=False, figure_inches=None, y_scale_range=None, x_scale_rotation=0,
                 x_scale_label_mapper=None, facet_label_mapper=None, subplots_ncol=4, subplots_adjust=None,
                 subplots_adjust_top=None, subplots_adjust_bottom=0.0, subplots_adjust_hspace=0.2,
                 subplots_adjust_wspace=0.2, facets_sort_by_value=None, facets_ascending=False,
                 group_position="stack", groups_sort_by_value=True, groups_ascending=False,
                 group_label_mapper=None,
                 legend_title=None, legend_loc="upper right", show=False):
    """
    Supported x examples:
    DataFrame index: (facet_by, x_categorical) {col0: y_numeric}
    DataFrame index: (facet_by, group_by, x_categorical) {col0: y_numeric}
    :param x: DataFrame
    :param width:
    :param color:
    :param xlab:
    :param ylab:
    :param title:
    :param sort_by:
    :param ascending:
    :param horizontal:
    :param figure_inches:
    :param y_scale_range:
    :param x_scale_rotation:
    :param x_scale_label_mapper:
    :param facet_label_mapper:
    :param subplots_ncol:
    :param subplots_adjust:
    :param subplots_adjust_top:
    :param subplots_adjust_bottom:
    :param subplots_adjust_hspace:
    :param subplots_adjust_wspace:
    :param facets_sort_by_value:
    :param facets_ascending:
    :param group_position:
    :param groups_sort_by_value:
    :param groups_ascending:
    :param group_label_mapper:
    :param legend_title:
    :param legend_loc:
    :param show:
    :return:
    """
    return _facet_plot(x, plot_type="bar", style=group_position, width=width, color=color, xlab=xlab,
                ylab=ylab, title=title, sort_by=sort_by, ascending=ascending,
                horizontal=horizontal, figure_inches=figure_inches, y_scale_range=y_scale_range,
                x_scale_rotation=x_scale_rotation,
                x_scale_label_mapper=x_scale_label_mapper, facet_label_mapper=facet_label_mapper,
                subplots_ncol=subplots_ncol, subplots_adjust=subplots_adjust,
                subplots_adjust_top=subplots_adjust_top, subplots_adjust_bottom=subplots_adjust_bottom,
                subplots_adjust_hspace=subplots_adjust_hspace,
                subplots_adjust_wspace=subplots_adjust_wspace,
                facets_sort_by_value=facets_sort_by_value, facets_ascending=facets_ascending,
                groups_sort_by_value=groups_sort_by_value, groups_ascending=groups_ascending,
                group_label_mapper=group_label_mapper,
                legend_title=legend_title, legend_loc=legend_loc, show=show)


def plot(x, y=None, z=None, style="solid", width=1.5, color=None, marker=None, marker_size=None, alpha=None, xlab=None, ylab=None,
             title=None,
             x_scale_ticks=None, x_scale_rotation=0, y_scale_ticks=None,
             group_by=None, standardize_x_ticks_for_grouped_line_plots=False,
             group_label_mapper=None, legend_title=None,
             legend_loc="upper right", figure_inches=None, show=True):
    """
    Supported x, y, z examples:
    x_numeric_arr
    x_numeric_arr/datetime_arr, y_numeric_arr
    x_numeric_arr, z_numeric_arr
    x_numeric_arr/datetime_arr, y_numeric_arr, z_numeric_arr
    DataFrame: {col0: x_numeric/datetime, col1: y_numeric, ...}, z: z_numeric_arr
    DataFrame: {col0: x_numeric/datetime, col1: y_numeric, col2: group_by, ...}, z: z_numeric_arr
    DataFrame index: (x_numeric/datetime) {col0: y_numeric}, z: z_numeric_arr
    DataFrame index: (group_by, x_numeric/datetime) {col0: y_numeric}, z: z_numeric_arr, if group_by is set
    DataFrame index: (facet_by, x_numeric/datetime) {col0: y_numeric}, z: z_numeric_arr, if group_by is not set
    DataFrame index: (facet_by, group_by, x_numeric/datetime) {col0: y_numeric}, z: z_numeric_arr
    :param x: numeric array, datetime array, or DataFrame.
    :param y: numeric array for y-axis, or None. when y is set, x must not be a DataFrame
    :param z: numeric array for z-axis, or None
    :param style: plot's style, e.g 'point', 'scatter', 'line'
    :param width: width of the line
    :param color: color of the line/marker
    :param marker: marker style
    :param marker_size: marker size
    :param alpha: alpha value
    :param xlab: x-axis's label
    :param ylab: y-axis's label
    :param title: plot's title
    :param x_scale_ticks: ticks displayed on x-asix, numeric array, string array, or dictionary
    :param x_scale_rotation: degree of rotation
    :param y_scale_ticks: ticks displayed on y-asix, numeric array, string array, or dictionary
    :param group_by: the column name for color grouping, the x must be a DataFrame
    :param standardize_x_ticks_for_grouped_line_plots:
    :param group_label_mapper: index array, text array, or dictionary
    :param legend_title: legend's title
    :param legend_loc: legend's location
    :param show: show the plot
    :return: return None if show=True, return the Figure object if show=False
    """
    
    plt.style.use("ggplot")

    x_vals = None
    y_vals = None
    group_vals = None
    
    if (y is not None) and (len(y) != len(x)):
        raise Exception("x and y must have the same length, but got {} and {}.".format(len(x), len(y)))
    if (z is not None) and (len(z) != len(x)):
        raise Exception("x and z must have the same length, but got {} and {}.".format(len(x), len(z)))

    standardize_x_ticks = False
    if (group_by is not None) and (group_by != ""):
        if style == "stackarea":
            standardize_x_ticks = True
        elif style == "area":
            standardize_x_ticks = True
            if (alpha is None) or (alpha == 1):
                style = "stackarea"
                print("Automatically changed plot type to 'stackarea'. Suppress this message by explicitly specifying the plot type as 'stackarea' or using <1 alpha value.")
        elif (style != "scatter") and (style != "point"):
            standardize_x_ticks = standardize_x_ticks_for_grouped_line_plots

    if y is None:
        # if x is 1-D numeric data, (ignore grouping)
        if (type(x) == list) or (type(x) == np.ndarray) or (type(x) == pd.Series) or (type(x) == pd.core.arrays.categorical.Categorical):
            x_vals = np.array(range(len(x)), dtype=int)
            if type(x) == list:
                y_vals = np.array(x)
            elif type(x) == pd.Series:
                y_vals = x.values
            else:
                y_vals = _try_get_cat_levels(x)

        # if x is a DataFrame
        elif type(x) == pd.DataFrame:
            # if x is a normal unaggregated DataFrame with 2 or more columns
            # (col_1 and col_2 will be numeric or datetime)
            # if group_by is specified, it has to be specified as column index or column name
            if len(x.dtypes) >= 2:
                group_col = None
                x_col = 0
                y_col = 1

                if (group_by is not None) and (group_by != ""):
                    group_col = _get_group_index_of_columns(x, group_by)
                    if group_col == 0:
                        x_col = 1
                        y_col = 2
                    elif group_col == 1:
                        y_col = 2

                x_vals = _try_get_cat_levels(x.iloc[:, x_col].values)
                y_vals = x.iloc[:, y_col].values

                if (not _is_numeric_array(x_vals, True)) or (not _is_numeric_array(y_vals, True)):
                    raise Exception("Column '{}' and '{}' must be numeric or datetime".format(x.columns[x_col], x.columns[y_col]))

                if group_col is not None:
                    group_vals = _try_get_cat_levels(x.iloc[:, group_col].values)

            # if x is a group_by DataFrame with only 1 aggregated numeric column
            elif (str(x.dtypes[0]).find("float") >= 0) or (str(x.dtypes[0]).find("int") >= 0):
                y_vals = x.iloc[:, 0].values

                # dual-indices
                # if group_col exists, one index will be used for grouping, the other index is used as x
                # if no group_col, the first index will be used for facet, the 2nd index is used as x
                if (type(x.index[0]) == tuple) and (len(x.index[0]) == 2):
                    if (group_by is not None) and (group_by != ""):
                        group_col = _get_group_index_of_index(x, group_by)
                        group_vals = np.array([tup[group_col] for tup in x.index])
                        x_vals = np.array([tup[1 if group_col == 0 else 0] for tup in x.index])
                    else:
                        x2 = x
                        if z is not None:
                            if len(x.dtypes) == 1:
                                x2 = x.copy()
                                x2["__z"] = z
                            else:
                                x2 = x.copy()
                                x2.iloc[: 1] = z
                        plot2(x2, style=style, width=width, color=color, marker=marker, marker_size=marker_size,
                              alpha=alpha,
                              xlab=xlab, ylab=ylab,
                              title=title,
                              y_scale_range="fixed",
                              x_scale_ticks=x_scale_ticks, x_scale_rotation=x_scale_rotation,
                              standardize_x_ticks_for_grouped_line_plots=standardize_x_ticks_for_grouped_line_plots,
                              group_label_mapper=group_label_mapper,
                              legend_title=legend_title,
                              figure_inches=figure_inches,
                              show=show)
                        return

                # tri-indices with group_by
                # one index will be used for grouping, one for facet, the last index is used as x
                elif (type(x.index[0]) == tuple) and (len(x.index[0]) == 3) and (group_by is not None) and (
                                group_by != ""):
                    group_col = _get_group_index_of_index(x, group_by)
                    if group_col != 1:
                        raise Exception("group_by must be the 2nd index of the DataFrame's index.")
                    x2 = x
                    if z is not None:
                        if len(x.dtypes) == 1:
                            x2 = x.copy()
                            x2["__z"] = z
                        else:
                            x2 = x.copy()
                            x2.iloc[: 1] = z
                    plot2(x2, style=style, width=width, color=color, marker=marker, marker_size=marker_size,
                          alpha=alpha,
                          xlab=xlab, ylab=ylab,
                          title=title,
                          y_scale_range="fixed",
                          x_scale_ticks=x_scale_ticks, x_scale_rotation=x_scale_rotation,
                          standardize_x_ticks_for_grouped_line_plots=standardize_x_ticks_for_grouped_line_plots,
                          group_label_mapper=group_label_mapper,
                          legend_title=legend_title,
                          figure_inches=figure_inches,
                          show=show)
                    return

                # single-index or multiple-indices, (ignore grouping)
                else:
                    # if the index is also numeric, then it will be treated as x
                    if _is_numeric_array(x.index.values, True):
                        x_vals = _try_get_cat_levels(x.index.values)
                    else:
                        x_vals = np.array(range(len(x)), dtype=int)

            else:
                raise Exception(
                    "Supported DataFrame formats: "
                    "{col0: x_numeric, col1: y_numeric, ...}, "
                    "{col0: x_numeric, col1: y_numeric, col2: group_by, ...}, "
                    "index: (x_numeric) {col0: y_numeric}, "
                    "index: (group, x_numeric) {col0: y_numeric}, "
                    "index: (facet, x_numeric) {col0: y_numeric}, "
                    "index: (facet, group, x_numeric) {col0: y_numeric}")
        else:
            raise Exception("Unsupported type {} for x".format(type(x)))

    # if both x and y are 1-D numeric, (ignore grouping)
    elif ((type(x) == list) or (type(x) == np.ndarray) or (type(x) == pd.Series) or (type(x) == pd.core.arrays.categorical.Categorical)) and \
        ((type(y) == list) or (type(y) == np.ndarray) or (type(y) == pd.Series)):
        x_vals = x.values if type(x) == pd.Series else np.array(_try_get_cat_levels(x))
        y_vals = y.values if type(y) == pd.Series else np.array(y)

    else:
        raise Exception("Unsupported type {} for x, or {} for y".format(type(x), type(y)))

    # no grouping
    if group_vals is None:
        if (style == "point") or (style == "scatter"):
            if z is not None:
                if (color is not None) and (color != ""):
                    cmap = _continuous_color_map(z, color).get_cmap()
                    plt.scatter(x_vals, y_vals, c=z, cmap=cmap, marker=marker, s=marker_size, alpha=1 if alpha is None else alpha)
                else:
                    plt.scatter(x_vals, y_vals, marker=marker, s=z, alpha=0.3 if alpha is None else alpha)
            elif (color is not None) and (color != ""):
                plt.scatter(x_vals, y_vals, c=np.repeat(color, len(x_vals)), marker=marker, s=marker_size, alpha=1 if alpha is None else alpha)
            else:
                plt.scatter(x_vals, y_vals, marker=marker, s=marker_size, alpha=1 if alpha is None else alpha)
        elif style == "area":
            if z is not None:
                print("z value is not supported.")

            plt.fill_between(x_vals, y_vals, color=color, alpha=1 if alpha is None else alpha)
        else:
            if z is not None:
                plt.plot(x_vals, y_vals, linewidth=z, linestyle=style, color=color, marker=marker,
                         markersize=marker_size, alpha=1 if alpha is None else alpha)
            else:
                plt.plot(x_vals, y_vals, linewidth=width, linestyle=style, color=color, marker=marker,
                         markersize=marker_size, alpha=1 if alpha is None else alpha)

    # grouping with standardize_x_ticks (line, area, stackedarea)
    elif standardize_x_ticks:
        spread_df, unique_group_vals = spread(pd.DataFrame({"x": x_vals, "y": y_vals, "grp": group_vals}), "grp", "y", return_group_values=True)
        x_vals = spread_df.x.values
        group_lbls = _try_map(unique_group_vals, group_label_mapper)

        if style == "stackarea":
            if z is not None:
                print("z value is not supported.")

            if color is not None:
                if type(color) == str:
                    plt.stackplot(x_vals, spread_df.iloc[:, 1:].values.transpose(), labels=group_lbls,
                                  alpha=1 if alpha is None else alpha)
                    accumulated = spread_df.apply(lambda r: np.nansum(r[1:]), axis=1).values
                    plt.plot(x_vals, accumulated, linewidth=width, linestyle="dotted", marker=marker,
                             markersize=marker_size, color=color)
                elif (type(color) == list) or (type(color) == np.ndarray):
                    plt.stackplot(x_vals, spread_df.iloc[:, 1:].values.transpose(), colors=color, labels=group_lbls,
                                  alpha=1 if alpha is None else alpha)
            else:
                plt.stackplot(x_vals, spread_df.iloc[:, 1:].values.transpose(), labels=group_lbls,
                              alpha=1 if alpha is None else alpha)

        elif style == "area":
            if z is not None:
                print("z value is not supported.")

            for grp, grp_col in enumerate(spread_df.columns.to_list()[1:]):
                clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
                plt.fill_between(x_vals, spread_df[grp_col], color=clr, label=group_lbls[grp], alpha=1 if alpha is None else alpha)
        else:
            if z is None:
                for grp, grp_col in enumerate(spread_df.columns.to_list()[1:]):
                    clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
                    plt.plot(x_vals, spread_df[grp_col], linewidth=width, linestyle=style, marker=marker, color=clr,
                             markersize=marker_size, label=group_lbls[grp], alpha=1 if alpha is None else alpha)
            else:
                spread_df_z = spread(pd.DataFrame({"x": x_vals, "z": z, "grp": group_vals}), "grp", "z")
                for grp, grp_col in enumerate(spread_df.columns.to_list()[1:]):
                    clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
                    plt.plot(x_vals, spread_df[grp_col], linewidth=spread_df_z.iloc[: grp + 1], linestyle=style, color=clr,
                             marker=marker,
                             markersize=marker_size, label=group_lbls[grp], alpha=1 if alpha is None else alpha)

    # grouping without standardize_x_ticks (line, point)
    else:
        unique_group_vals = pd.Series(group_vals).unique()
        group_lbls = _try_map(unique_group_vals, group_label_mapper)
        for grp, grp_val in enumerate(unique_group_vals):
            grp_filter = group_vals == grp_val
            clr = color[grp] if (type(color) == list) or (type(color) == np.ndarray) else None
            if (style == "point") or (style == "scatter"):
                if type(z) == list:
                    plt.scatter(x_vals[grp_filter], y_vals[grp_filter], marker=marker, s=np.array(z)[grp_filter], c=clr,
                                label=group_lbls[grp], alpha=0.3 if alpha is None else alpha)
                elif type(z) == np.ndarray:
                    plt.scatter(x_vals[grp_filter], y_vals[grp_filter], marker=marker, s=z[grp_filter], c=clr,
                                label=group_lbls[grp], alpha=0.3 if alpha is None else alpha)
                elif type(z) == pd.Series:
                    plt.scatter(x_vals[grp_filter], y_vals[grp_filter], marker=marker, s=z.values[grp_filter], c=clr,
                                label=group_lbls[grp], alpha=0.3 if alpha is None else alpha)
                else:
                    plt.scatter(x_vals[grp_filter], y_vals[grp_filter], marker=marker, s=marker_size, c=clr,
                                label=group_lbls[grp], alpha=1 if alpha is None else alpha)
            else:
                if type(z) == list:
                    plt.plot(x_vals[grp_filter], y_vals[grp_filter], linewidth=np.array(z)[grp_filter], linestyle=style,
                             color=clr, marker=marker,
                             markersize=marker_size, label=group_lbls[grp], alpha=1 if alpha is None else alpha)
                elif type(z) == np.ndarray:
                    plt.plot(x_vals[grp_filter], y_vals[grp_filter], linewidth=z[grp_filter], linestyle=style,
                             color=clr, marker=marker,
                             markersize=marker_size, label=group_lbls[grp], alpha=1 if alpha is None else alpha)
                elif type(z) == pd.Series:
                    plt.plot(x_vals[grp_filter], y_vals[grp_filter], linewidth=z.values[grp_filter], linestyle=style,
                             color=clr, marker=marker,
                             markersize=marker_size, label=group_lbls[grp], alpha=1 if alpha is None else alpha)
                else:
                    plt.plot(x_vals[grp_filter], y_vals[grp_filter], linewidth=width, linestyle=style, color=clr, marker=marker,
                             markersize=marker_size, label=group_lbls[grp], alpha=1 if alpha is None else alpha)

    if (type(x_scale_ticks) == list) or (type(x_scale_ticks) == np.ndarray):
        if _is_numeric_array(x_scale_ticks, consider_datetime=True):
            plt.xticks(x_scale_ticks, x_scale_ticks)
        else:
            tick_vals = np.linspace(np.min(x_vals), np.max(x_vals), len(x_scale_ticks), dtype=x_vals.dtype)
            plt.xticks(tick_vals, x_scale_ticks)
    elif type(x_scale_ticks) == dict:
        plt.xticks(list(x_scale_ticks.keys()), list(x_scale_ticks.values()))

    if (type(y_scale_ticks) == list) or (type(y_scale_ticks) == np.ndarray):
        if _is_numeric_array(y_scale_ticks, consider_datetime=True):
            plt.yticks(y_scale_ticks, y_scale_ticks)
        else:
            tick_vals = np.linspace(np.min(y_vals), np.max(y_vals), len(y_scale_ticks), dtype=y_vals.dtype)
            plt.yticks(tick_vals, y_scale_ticks)
    elif type(y_scale_ticks) == dict:
        plt.yticks(list(y_scale_ticks.keys()), list(y_scale_ticks.values()))

    if x_scale_rotation > 0:
        plt.xticks(rotation=x_scale_rotation)

    if (group_vals is not None) and (legend_loc is not None):
        plt.legend(title=legend_title, facecolor="white", loc=legend_loc, prop={'size': 10}, fontsize=8, ncol=1)

    if figure_inches is not None:
        plt.figure().set_size_inches(figure_inches[0], figure_inches[1])
    if xlab is not None:
        plt.xlabel(xlab)
    if ylab is not None:
        plt.ylabel(ylab)
    if title is not None:
        plt.title(title)
    if show:
        plt.show()
    else:
        return plt.figure()


def get_time_series_ticks(datetime_arr, datetime_format="auto", snap_to_major_tick=True, tick_interval="auto", n_x_ticks=10):
    """ Get a dictionary for time-series x-axis ticks. The dictionary key is the time value. The dictionary value is the tick label.
    :param datetime_arr: time-series x-axis values
    :param datetime_format: datetime format, or 'auto'
    :param snap_to_major_tick: If True, the first/last tick is set to a reasonable nearby major time point, otherwise, it is set to the min/max value of datatime_arr.
    :param tick_interval: e.g. '1 sec', '2s', '3 min', '4m', '5 hour', '6h', '7 day', '8d', 'auto'
    :param n_x_ticks: the number of ticks to generate
    :return: Dictionary of tick value of tick label
    """
    tz_name = None
    if ((type(datetime_arr) == list) or (type(datetime_arr) == np.ndarray)) and (len(datetime_arr) > 0) and (
            str(type(datetime_arr[0])) == "<class 'datetime.datetime'>"):
        if datetime_arr[0].tzinfo is not None:
            tz_name = datetime_arr[0].tzinfo.zone
    elif (type(datetime_arr) == pd.Series) and (str(datetime_arr.dtype) != "datetime64[D]") and (datetime_arr.dt is not None) and (datetime_arr.dt.tz is not None):
        tz_name = datetime_arr.dt.tz.zone

    min_date_time, max_date_time = np.min(datetime_arr), np.max(datetime_arr)
    if type(min_date_time) == np.datetime64:
        min_date_time = datetime.fromtimestamp(min_date_time.astype(float) / 1e9)
        if tz_name is not None:
            min_date_time = localize_datetime(min_date_time, tz_name)
        max_date_time = datetime.fromtimestamp(max_date_time.astype(float) / 1e9)
        if tz_name is not None:
            max_date_time = localize_datetime(max_date_time, tz_name)
    ori_min_date_time, ori_max_date_time = min_date_time, max_date_time
    n_sec_diff = (max_date_time - min_date_time).total_seconds()

    if snap_to_major_tick:
        if n_sec_diff <= 10 * 60:
            # snap to 1 min
            min_date_time = min_date_time + timedelta(seconds=-min_date_time.second)
            max_date_time = max_date_time + timedelta(seconds=(60 - max_date_time.second) % 60)
        elif 10 * 60 < n_sec_diff <= 60 * 60:
            # snap to 5 min
            min_date_time = min_date_time + timedelta(seconds=-min_date_time.second) + timedelta(minutes=-(min_date_time.minute % 5))
            max_date_time = max_date_time + timedelta(seconds=(60 - max_date_time.second) % 60)
            max_date_time = max_date_time + timedelta(minutes=(5 - (max_date_time.minute % 5)) % 5)
        elif 60 * 60 < n_sec_diff <= 2 * 60 * 60:
            # snap to 10 min
            min_date_time = min_date_time + timedelta(seconds=-min_date_time.second) + timedelta(minutes=-(min_date_time.minute % 10))
            max_date_time = max_date_time + timedelta(seconds=(60 - max_date_time.second) % 60)
            max_date_time = max_date_time + timedelta(minutes=(10 - (max_date_time.minute % 10)) % 10)
        elif 2 * 60 * 60 < n_sec_diff <= 6 * 60 * 60:
            # snap to 30 min
            min_date_time = min_date_time + timedelta(seconds=-min_date_time.second) + timedelta(minutes=-(min_date_time.minute % 30))
            max_date_time = max_date_time + timedelta(seconds=(60 - max_date_time.second) % 60)
            max_date_time = max_date_time + timedelta(minutes=(30 - (max_date_time.minute % 30)) % 30)
        elif 6 * 60 * 60 < n_sec_diff <= 2 * 24 * 60 * 60:
            # snap to 1 hr
            min_date_time = min_date_time + timedelta(seconds=-min_date_time.second) + timedelta(minutes=-min_date_time.minute)
            max_date_time = max_date_time + timedelta(seconds=(60 - max_date_time.second) % 60)
            max_date_time = max_date_time + timedelta(minutes=(60 - max_date_time.minute) % 60)
        else:
            # snap to 1 day
            min_date_time = min_date_time + timedelta(seconds=-min_date_time.second) + timedelta(minutes=-min_date_time.minute) + timedelta(
                minutes=-min_date_time.hour)
            max_date_time = max_date_time + timedelta(seconds=(60 - max_date_time.second) % 60)
            max_date_time = max_date_time + timedelta(minutes=(60 - max_date_time.minute) % 60)
            max_date_time = max_date_time + timedelta(minutes=(24 - max_date_time.hour) % 24)
        n_sec_diff = (max_date_time - min_date_time).total_seconds()

    if datetime_format == "auto":
        if n_sec_diff <= 60 * 60:
            datetime_format = "%M:%S s"
        elif 60 * 60 < n_sec_diff <= 24 * 60 * 60:
            datetime_format = "%H:%M %p"
        elif 24 * 60 * 60 < n_sec_diff <= 28 * 24 * 60 * 60:
            datetime_format = "%m-%d %H%p"
        elif 28 * 24 * 60 * 60 < n_sec_diff <= 365 * 24 * 60 * 60:
            datetime_format = "%h-%d"
        else:
            datetime_format = "%y-%h-%d"

    if snap_to_major_tick:
        if (tick_interval is None) or (tick_interval == "auto"):
            n_sec_per_tick = int(round(n_sec_diff / n_x_ticks, 0))
        else:
            match = re.search("(\d+)\s*(s|m|h|d)", str(tick_interval))
            assert match is not None, "invalid tick_interval, e.g. are 5 sec, 10 min, 3 hour"
            if match[2] == "s":
                n_sec_per_tick = int(match[1])
            elif match[2] == "m":
                n_sec_per_tick = int(match[1]) * 60
            elif match[2] == "h":
                n_sec_per_tick = int(match[1]) * 60 * 60
            elif match[2] == "d":
                n_sec_per_tick = int(match[1]) * 60 * 60 * 24
            n_x_ticks = int(np.ceil(n_sec_diff / n_sec_per_tick))

        x_ticks = {}
        for t in range(n_x_ticks + 1):
            tick_date_time = min_date_time + timedelta(seconds=n_sec_per_tick * t)
            if tz_name is not None:
                tick_date_time = localize_datetime(tick_date_time, tz_name)
            x_ticks[tick_date_time] = tick_date_time.strftime(datetime_format)
            if t > 0:
                prev_date_time = min_date_time + timedelta(seconds=n_sec_per_tick * (t - 1))
                if prev_date_time < ori_min_date_time < tick_date_time:
                    x_ticks[ori_min_date_time] = " "
                if prev_date_time < ori_max_date_time < tick_date_time:
                    x_ticks[ori_max_date_time] = " "
    else:
        n_sec_per_tick = int(n_sec_diff / (n_x_ticks - 1))
        x_ticks = {}
        for t in range(n_x_ticks):
            date_time = min_date_time + timedelta(seconds=n_sec_per_tick * t)
            if tz_name is not None:
                date_time = localize_datetime(date_time, tz_name)
            x_ticks[date_time] = date_time.strftime(datetime_format)
    return x_ticks


def plot2(x, style="solid", width=1.5, color=None, marker=None, marker_size=None, alpha=None, xlab=None, ylab=None,
              title=None, figure_inches=None, y_scale_range=None,
              x_scale_ticks=None, x_scale_rotation=0, x_scale_label_mapper=None, facet_label_mapper=None,
              subplots_ncol=4, subplots_adjust=None,
              subplots_adjust_top=None, subplots_adjust_bottom=0.0, subplots_adjust_hspace=0.2,
              subplots_adjust_wspace=0.2, facets_sort_by_value=None, facets_ascending=False, standardize_x_ticks_for_grouped_line_plots=False,
              group_label_mapper=None, legend_title=None,
              legend_loc="upper right", show=True):
    """
    Supported x examples:
    DataFrame index: (facet_by, x_numeric/datetime) {col0: y_numeric, col1: z_numeric_arr}
    DataFrame index: (facet_by, group_by, x_numeric/datetime) {col0: y_numeric, col1: z_numeric_arr}
    :param x: DataFrame
    :param style:
    :param width:
    :param color:
    :param marker:
    :param marker_size:
    :param alpha:
    :param xlab:
    :param ylab:
    :param title:
    :param figure_inches:
    :param y_scale_range:
    :param x_scale_ticks:
    :param x_scale_rotation:
    :param x_scale_label_mapper:
    :param facet_label_mapper:
    :param subplots_ncol:
    :param subplots_adjust:
    :param subplots_adjust_top:
    :param subplots_adjust_bottom:
    :param subplots_adjust_hspace:
    :param subplots_adjust_wspace:
    :param facets_sort_by_value:
    :param facets_ascending:
    :param standardize_x_ticks_for_grouped_line_plots:
    :param group_label_mapper:
    :param legend_title:
    :param legend_loc:
    :param show:
    :return:
    """

    plot_type = "line"
    if (style == "scatter") or (style == "point") or (style == "area") or (style == "stackarea"):
        plot_type = style
        style = None

    return _facet_plot(x, plot_type, style=style, width=width, color=color, marker=marker, marker_size=marker_size,
                alpha=alpha, xlab=xlab,
                ylab=ylab, title=title,
                figure_inches=figure_inches, y_scale_range=y_scale_range, x_scale_ticks=x_scale_ticks,
                x_scale_rotation=x_scale_rotation,
                standardize_x_ticks_for_grouped_line_plots=standardize_x_ticks_for_grouped_line_plots,
                x_scale_label_mapper=x_scale_label_mapper, facet_label_mapper=facet_label_mapper,
                subplots_ncol=subplots_ncol, subplots_adjust=subplots_adjust,
                subplots_adjust_top=subplots_adjust_top, subplots_adjust_bottom=subplots_adjust_bottom,
                subplots_adjust_hspace=subplots_adjust_hspace,
                subplots_adjust_wspace=subplots_adjust_wspace,
                facets_sort_by_value=facets_sort_by_value, facets_ascending=facets_ascending,
                group_label_mapper=group_label_mapper,
                legend_title=legend_title, legend_loc=legend_loc, show=show)


def _normalize_z(x, z, normalize_z_range):
    if (type(z) == str) and (type(x) == pd.DataFrame):
        if np.sum(x.columns.values == z) == 1:
            marker_size = x[z].values
        else:
            raise Exception("Invalid z column {}".format(z))
    elif type(z) == list or () or ():
        marker_size = np.array(z)
    elif type(z) == np.ndarray:
        marker_size = z
    elif type(z) == pd.Series:
        marker_size = z.values
    else:
        raise Exception("z must be a column name or array that represents the marker size.")

    if normalize_z_range is not None:
        min_z = np.min(marker_size)
        max_z = np.max(marker_size)

        if max_z > min_z:
            return (marker_size - min_z) * (normalize_z_range[1] - normalize_z_range[0]) / (
                max_z - min_z) + normalize_z_range[0]
        else:
            return (marker_size - min_z) * (
                        normalize_z_range[1] - normalize_z_range[0]) / 0.00001 + normalize_z_range[0]
    else:
        return marker_size


def scatter(x, y=None, z=None, normalize_z_range=(10, 255), color=None, marker=None, marker_size=10, alpha=None,
                xlab=None, ylab=None, title=None,
                x_scale_ticks=None, x_scale_rotation=0, group_by=None,
                group_label_mapper=None, legend_title=None,
                legend_loc="upper right", figure_inches=None, show=True):

    plot(x, y=y, z=_normalize_z(x, z, normalize_z_range) if z is not None else None, style="scatter", color=color, marker=marker,
         marker_size=marker_size, alpha=alpha,
         xlab=xlab, ylab=ylab, title=title,
         x_scale_ticks=x_scale_ticks, x_scale_rotation=x_scale_rotation, group_by=group_by,
         group_label_mapper=group_label_mapper, legend_title=legend_title,
         legend_loc=legend_loc, figure_inches=figure_inches, show=show)


def scatter2(x, z=None, normalize_z_range=(10, 255), color=None, marker=None, marker_size=None, alpha=None,
                 xlab=None, ylab=None,
                 title=None, figure_inches=None, y_scale_range=None,
                 x_scale_ticks=None, x_scale_rotation=0, x_scale_label_mapper=None, facet_label_mapper=None,
                 subplots_ncol=4, subplots_adjust=None,
                 subplots_adjust_top=None, subplots_adjust_bottom=0.0, subplots_adjust_hspace=0.2,
                 subplots_adjust_wspace=0.2,
                 group_label_mapper=None, legend_title=None,
                 legend_loc="upper right", show=True):

    x2 = x
    if z is not None:
        if len(x.dtypes) == 1:
            x2 = x.copy()
            x2["__z"] = _normalize_z(x, z, normalize_z_range)
        elif (type(z) == str) and (np.sum(x.columns.values == z) > 0) and (normalize_z_range is not None):
            x2 = x.copy()
            x2.iloc[: 1] = _normalize_z(x, z, normalize_z_range)

    return _facet_plot(x2, "scatter", style="scatter", color=color, marker=marker,
                marker_size=marker_size,
                alpha=alpha, xlab=xlab,
                ylab=ylab, title=title,
                figure_inches=figure_inches, y_scale_range=y_scale_range, x_scale_ticks=x_scale_ticks,
                x_scale_rotation=x_scale_rotation,
                x_scale_label_mapper=x_scale_label_mapper, facet_label_mapper=facet_label_mapper,
                subplots_ncol=subplots_ncol, subplots_adjust=subplots_adjust,
                subplots_adjust_top=subplots_adjust_top, subplots_adjust_bottom=subplots_adjust_bottom,
                subplots_adjust_hspace=subplots_adjust_hspace,
                subplots_adjust_wspace=subplots_adjust_wspace,
                group_label_mapper=group_label_mapper,
                legend_title=legend_title, legend_loc=legend_loc, show=show)


def cartesian_array(*arrays, dtype_of_ndarray_return=None, return_as_dataframe=False):
    n_dim = len(arrays)
    if n_dim > 1:
        iter = itertools.product(*arrays)
        tuples = list(iter)
        if return_as_dataframe:
            df_data = {}
            for dim in range(n_dim):
                col_name = arrays[dim].name if type(arrays[dim]) == pd.Series else "arr_{}".format(dim + 1)
                df_data[col_name] = list()

            col_names = list(df_data.keys())
            for i, tup in enumerate(tuples):
                for dim in range(n_dim):
                    df_data[col_names[dim]].append(tup[dim])

            return pd.DataFrame(df_data)
        elif dtype_of_ndarray_return is not None:
            out = np.empty(len(tuples)*n_dim, dtype=dtype_of_ndarray_return)
            for i, tup in enumerate(tuples):
                for dim in range(n_dim):
                    out[i * n_dim + dim] = tup[dim]
            return out.reshape(-1, n_dim)
        else:
            return tuples
    else:
        raise Exception("len(arrays) must be > 1")


def cartesian_dataframe(*dataframes):
    n_df = len(dataframes)
    if n_df > 1:
        df_left = dataframes[0]
        for i in range(1, n_df):
            df_right = dataframes[i]
            rows = itertools.product(df_left.iterrows(), df_right.iterrows())

            df_left = pd.DataFrame(left.append(right) for (_, left), (_, right) in rows)
        return df_left.reset_index(drop=True)
    else:
        raise Exception("len(dataframes) must be > 1")


def gather(df, key_col, value_col, gather_cols, create_new_index=True):
    if type(gather_cols[0]) == int:
        gather_cols = df.columns.values[gather_cols]
    elif type(gather_cols[0]) != str:
        raise Exception("gather_cols must be array of column index or column name.")

    df_gathered = df.loc[:, df.columns.values[pd.Series(df.columns.values).isin(gather_cols).values == False]].copy()
    df_gathered[key_col] = None
    df_gathered[value_col] = None
    key_col_idx = len(df_gathered.columns) - 2
    value_col_idx = len(df_gathered.columns) - 1

    copy_template = df_gathered.copy()
    for c in range(len(gather_cols)):
        if c > 0:
            df_gathered = pd.concat([df_gathered, copy_template.copy()], ignore_index=create_new_index)
        row_from = c * len(df)
        row_to = (c + 1) * len(df)
        df_gathered.iloc[row_from:row_to, key_col_idx] = gather_cols[c]
        df_gathered.iloc[row_from:row_to, value_col_idx] = df[gather_cols[c]].values

    return df_gathered


def spread(df, key_col, value_col, fill_numeric_zero=True, new_col_name_format="{col_name}_{col_value}", return_group_values=False):
    index_dim = None
    index_of_index = None
    if type(key_col) == int:
        key_col = df.columns.values[key_col]
    elif type(key_col) != str:
        raise Exception("key_col must be either column name or index name of a multi-indices data frame.")
    elif np.sum(df.columns.values == key_col) == 0:
        index_of_index = df.index.names.index(key_col)
        index_dim = len(df.index[0])
        if index_dim <= 1:
            raise Exception("key_col must be either column name or index name of a multi-indices data frame.")

    if type(value_col) == int:
        value_col = df.columns.values[value_col]
    elif (type(value_col) != str) or (np.sum(df.columns.values == value_col) == 0):
        raise Exception("value_col must be either column index or column name.")

    df_spread = None
    # the key column is a normal column
    if index_dim is None:
        if df.loc[:, key_col].dtype.name == "category":
            key_values = df.loc[:, key_col].cat.categories
        else:
            key_values = df.loc[:, key_col].unique()
        keep_cols = list(df.columns.values[pd.Series(df.columns.values).isin([key_col, value_col]).values == False])
        group_indices = df.loc[:, keep_cols + [key_col]].groupby(by=keep_cols).count().index

        df_spread = pd.DataFrame({})
        for i, c in enumerate(keep_cols):
            if type(group_indices[0]) == tuple:
                df_spread[str(c)] = [tup[i] for tup in group_indices]
            else:
                df_spread[str(c)] = group_indices

        for k in key_values:
            df_spread = df_spread.merge(df.loc[df[key_col] == k, keep_cols + [value_col]], how="left", on=keep_cols)

        if (new_col_name_format is None) or (new_col_name_format == ""):
            df_spread.columns = keep_cols + [key_col + str(i) for i, k in enumerate(key_values)]
        elif (new_col_name_format.find("{col_name}") >= 0) or (new_col_name_format.find("{col_value}") >= 0):
            df_spread.columns = keep_cols + [
                new_col_name_format.replace("{col_name}", key_col).replace("{col_value}", str(k)) for k in key_values]
        elif new_col_name_format.find("{}") >= 0:
            df_spread.columns = keep_cols + [new_col_name_format.format(str(k)) for k in key_values]
        else:
            df_spread.columns = keep_cols + [new_col_name_format + str(k) for k in key_values]

        if fill_numeric_zero and (
                (str(df[value_col].dtype).find("int") >= 0) or (str(df[value_col].dtype).find("float") >= 0)):
            start_ind = len(df_spread.columns) - len(key_values)
            end_ind = len(df_spread.columns)
            df_spread.iloc[:, list(range(start_ind, end_ind))] = df_spread.iloc[:,
                                                                 list(range(start_ind, end_ind))].fillna(0).values
        if return_group_values:
            return df_spread, key_values,
        else:
            return df_spread

    # the key column is the index of the df, and the df only has multiple indices
    else:
        df_temp = df.copy()
        df_temp.index = list(range(len(df)))

        keep_name_of_index = list()
        for i, c in enumerate(df.index.names):
            df_temp[c] = [tup[i] for tup in df.index]
            if i != index_of_index:
                keep_name_of_index.append(c)

        spread_return = spread(df_temp, key_col, value_col, fill_numeric_zero=fill_numeric_zero,
                               new_col_name_format="" if new_col_name_format is None else new_col_name_format,
                               return_group_values=return_group_values)
        if return_group_values:
            return spread_return[0].set_index(keep_name_of_index), spread_return[1]
        else:
            return spread_return[0].set_index(keep_name_of_index)


def nanmin(arr):
    min_val = None
    for val in arr:
        if val is not None:
            if (min_val is None) or (val < min_val):
                min_val = val
    return min_val


def nanmax(arr):
    max_val = None
    for val in arr:
        if val is not None:
            if (max_val is None) or (val > max_val):
                max_val = val
    return max_val


def _localize_datetime(dt, tz):
    if dt is not None:
        if dt.tzinfo is None:
            return tz.localize(dt)
        else:
            return dt.astimezone(tz)
    else:
        return dt


def localize_datetime(datetime_data, timezone="Asia/Singapore"):
    if timezone is not None:
        tz = pytz.timezone(timezone)
        if str(type(datetime_data)) == "<class 'datetime.datetime'>":
            return _localize_datetime(datetime_data, tz)
        elif ((type(datetime_data) == list) or (type(datetime_data) == np.ndarray)) and (len(datetime_data) > 0) and (str(type(datetime_data[0])) == "<class 'datetime.datetime'>"):
            return [_localize_datetime(dt, tz) for dt in datetime_data]
        elif (type(datetime_data) == pd.Series) and (str(datetime_data.dtype) != "datetime64[D]"):
            if datetime_data.dt.tz is None:
                return datetime_data.dt.tz_localize(timezone)
            else:
                return datetime_data.dt.tz_convert(timezone)
        else:
            return datetime_data
    else:
        return datetime_data


def create_datetime_features(datetime_arr, df, col_name_prefix, year=True, month=True, day=True, wday=True,
                                 period=False, date_key=False,
                                 hour=True, minute=True, yday=True, yweek=False, month_sn=True, day_sn=True, week_sn=False,
                                 hour_sn=False, min_sn=False, sec_sn=False, round_to_nearest_nmin=[], categorize=True, timezone="Asia/Singapore"):
    if df is None:
        df = pd.DataFrame({})
    elif type(datetime_arr) == str:
        datetime_arr = df[datetime_arr]

    tz = pytz.timezone(timezone) if timezone is not None else None

    is_date = False
    datetime_obj_list = None
    date_obj_list = None
    if type(datetime_arr) == list:
        is_date = (len(datetime_arr) > 0) and (str(type(datetime_arr[0])) == "<class 'datetime.date'>")
        if (timezone is not None) and (not is_date):
            datetime_obj_list = localize_datetime(datetime_arr, timezone)
        else:
            datetime_obj_list = datetime_arr
        date_obj_list = datetime_obj_list
    elif (type(datetime_arr) == np.ndarray) or (type(datetime_arr) == pd.Series):
        if type(datetime_arr) == pd.Series:
            datetime_obj_list = localize_datetime(datetime_arr, timezone).values
        else:
            datetime_obj_list = localize_datetime(datetime_arr, timezone)

        if str(datetime_arr.dtype).startswith("datetime64[ns"):
            datetime_obj_list = [datetime.fromtimestamp(ticks, tz) if (ticks is not None) and (ticks > 0) else None for ticks in
                                 (datetime_obj_list.astype("int64") / 1e9).astype("float")]
        elif str(datetime_obj_list.dtype).startswith("datetime64[ms"):
            datetime_obj_list = [datetime.fromtimestamp(ticks, tz) if (ticks is not None) and (ticks > 0) else None for ticks in
                                 (datetime_obj_list.astype("int64") / 1e6).astype("float")]
        elif str(datetime_obj_list.dtype).startswith("datetime64[s"):
            datetime_obj_list = [datetime.fromtimestamp(ticks, tz) if (ticks is not None) and (ticks > 0) else None for ticks in
                                 datetime_obj_list.astype("float")]
        elif str(datetime_obj_list.dtype) == "datetime64[D]":
            is_date = True
            datetime_obj_list = [datetime.fromtimestamp(ticks, tz).date() if (ticks is not None) and (ticks > 0) else None for ticks in
                                 datetime_obj_list.astype("datetime64[s]").astype("float")]
            date_obj_list = datetime_obj_list
    else:
        raise Exception("datetime_arr must be list, ndarray or Series")

    if is_date:
        transformed = np.array(
            [[dt.year, dt.month, dt.day, dt.weekday()] if dt is not None else [None, None, None, None] for dt in
             datetime_obj_list])
    else:
        transformed = np.array([[dt.year, dt.month, dt.day, dt.weekday(), dt.hour, dt.minute] if dt is not None else [
            None, None, None, None, None, None] for dt in datetime_obj_list])
        date_obj_list = [dt.date() if dt is not None else None for dt in datetime_obj_list]

    if year:
        df[col_name_prefix + "year"] = transformed[:, 0]
        if categorize:
            df[col_name_prefix + "year"] = df[col_name_prefix + "year"].astype("category")

    if month:
        df[col_name_prefix + "month"] = transformed[:, 1]
        if categorize:
            df[col_name_prefix + "month"] = pd.Categorical(df[col_name_prefix + "month"], categories=list(range(1, 13)),
                                                       ordered=True)

    if day:
        df[col_name_prefix + "day"] = transformed[:, 2]
        if categorize:
            df[col_name_prefix + "day"] = pd.Categorical(df[col_name_prefix + "day"], categories=list(range(1, 32)),
                                                     ordered=True)

    if wday:
        df[col_name_prefix + "wday"] = transformed[:, 3]
        if categorize:
            df[col_name_prefix + "wday"] = pd.Categorical(df[col_name_prefix + "wday"], categories=list(range(0, 7)),
                                                      ordered=True)

    if period:
        filt = transformed[:, 0] != None
        df.loc[filt, col_name_prefix + "period"] = transformed[filt, 0] * 100 + transformed[filt, 1]
        if categorize:
            comb = cartesian_array(pd.Series(transformed[filt, 0] * 100).sort_values().unique(), list(range(1, 13)))
            levels = [tup[0] + tup[1] for tup in comb]
            df[col_name_prefix + "period"] = pd.Categorical(df[col_name_prefix + "period"], categories=levels,
                                                              ordered=True)

    if date_key:
        filt = (transformed[:, 0] != None) & (transformed[:, 1] != None)
        df.loc[filt, col_name_prefix + "date_key"] = transformed[filt, 0] * 10000 + transformed[filt, 1] * 100 + transformed[filt, 2]

    if not is_date:
        if hour:
            df[col_name_prefix + "hour"] = transformed[:, 4]
            if categorize:
                df[col_name_prefix + "hour"] = pd.Categorical(df[col_name_prefix + "hour"], categories=list(range(0, 24)),
                                                          ordered=True)
        if minute:
            df[col_name_prefix + "minute"] = transformed[:, 5]
            if categorize:
                df[col_name_prefix + "minute"] = pd.Categorical(df[col_name_prefix + "minute"], categories=list(range(0, 60)),
                                                            ordered=True)

    if yday or yweek:
        first_day_of_years = {}
        weekday_of_first_day_of_years = {}
        for yr in transformed[:, 0]:
            if (yr is not None) and (first_day_of_years.get(yr) is None):
                first_day_of_years[yr] = datetime(yr, 1, 1).date()
                weekday_of_first_day_of_years[yr] = first_day_of_years[yr].weekday()
        yday_vals = np.array([
            (date_obj_list[i] - first_day_of_years[yr]).days if not pd.isna(yr) else None
            for i, yr in enumerate(transformed[:, 0])])

    if yday:
        df[col_name_prefix + "yday"] = yday_vals
        if categorize:
            df[col_name_prefix + "yday"] = pd.Categorical(df[col_name_prefix + "yday"], categories=list(range(366)),
                                                      ordered=True)

    if yweek:
        df[col_name_prefix + "yweek"] = [
            int((yday_vals[i] + weekday_of_first_day_of_years[yr]) / 7) if not pd.isna(yr) else None
            for i, yr in enumerate(transformed[:, 0])]
        if categorize:
            df[col_name_prefix + "yweek"] = pd.Categorical(df[col_name_prefix + "yweek"], categories=list(range(53)),
                                                      ordered=True)

    if month_sn:
        filt = transformed[:, 0] != None
        n_months = transformed[filt, 0] * 12 + transformed[filt, 1]
        n_months = n_months - np.min(n_months)
        df.loc[filt, col_name_prefix + "month_sn"] = n_months

    if day_sn:
        first_date = nanmin(date_obj_list)
        df[col_name_prefix + "day_sn"] = [int((dt - first_date).days) if dt is not None else None for dt in
                                          date_obj_list]

    if week_sn:
        first_wday = nanmin(date_obj_list).weekday()
        if not day_sn:
            first_date = nanmin(date_obj_list)
            df[col_name_prefix + "week_sn"] = [
                math.floor(((dt - first_date).days + first_wday) / 7) if dt is not None else None for dt in
                date_obj_list]
        else:
            df[col_name_prefix + "week_sn"] = [math.floor((daysn + first_wday) / 7) if not pd.isna(daysn) else None for
                                               daysn in df[col_name_prefix + "day_sn"].values]

    if not is_date:
        if hour_sn or min_sn or sec_sn:
            first_time = nanmin(datetime_obj_list)

        if hour_sn:
            first_hr = localize_datetime(datetime(first_time.year, first_time.month, first_time.day, first_time.hour, 0, 0), timezone)
            df[col_name_prefix + "hour_sn"] = [int((dt - first_hr).total_seconds() / 3600) if dt is not None else None for
                                               dt in datetime_obj_list]

        if min_sn:
            first_min = localize_datetime(datetime(first_time.year, first_time.month, first_time.day, first_time.hour, first_time.minute, 0), timezone)
            df[col_name_prefix + "minute_sn"] = [int((dt - first_min).total_seconds() / 60) if dt is not None else None for
                                               dt in datetime_obj_list]

        if sec_sn:
            first_sec = localize_datetime(datetime(first_time.year, first_time.month, first_time.day, first_time.hour, first_time.minute, first_time.second), timezone)
            df[col_name_prefix + "second_sn"] = [int((dt - first_sec).total_seconds()) if dt is not None else None for
                                               dt in datetime_obj_list]

        if round_to_nearest_nmin is not None:
            for nmin in round_to_nearest_nmin:
                if nmin <= 0:
                    raise Exception("round_to_nearest_nmin must be positive")
                elif nmin == 1:
                    col_name = col_name_prefix + "per_min"
                elif nmin == 60:
                    col_name = col_name_prefix + "hourly"
                elif (nmin > 60) and (nmin % 60 == 0):
                    col_name = col_name_prefix + str(int(nmin / 60)) + "hours"
                else:
                    col_name = col_name_prefix + str(nmin) + "mins"

                df[col_name] = [
                    datetime.fromtimestamp(round(dt.timestamp() / (nmin * 60)) * nmin * 60, tz) if dt is not None else None for
                    dt in datetime_obj_list]

    return df


def iqr(arr):
    q1 = np.nanquantile(arr, 0.25)
    q3 = np.nanquantile(arr, 0.75)
    return q3 - q1


def iqr_outliers(arr, multiplier=1.5, upper_only=False, return_filter=False, return_indices=False,
                 return_reversed=False):
    q1 = np.nanquantile(arr, 0.25)
    q3 = np.nanquantile(arr, 0.75)
    if type(arr) == list:
        arr0 = np.array(arr)
    elif type(arr) == np.ndarray:
        arr0 = arr
    elif type(arr) == pd.Series:
        arr0 = arr.values
    else:
        raise Exception("{} type not supported".format(type(arr)))
    if upper_only:
        filt = arr0 > q3 + (q3 - q1) * multiplier
    else:
        filt = (arr0 > q3 + (q3 - q1) * multiplier) | (arr0 < q1 - (q3 - q1) * multiplier)

    if return_filter:
        return filt == False if return_reversed else filt
    elif return_indices:
        return np.argwhere(filt == False).flatten() if return_reversed else np.argwhere(filt).flatten()
    else:
        return arr0[filt == False] if return_reversed else arr0[filt]


def create_one_hot(df, categorical_col, col_name_format=None, levels_mapper="smart", dtype=None):
    if (type(categorical_col) == str) and (np.sum(df.columns.values == categorical_col) == 0):
        raise Exception("{} has to be a dataframe's column name or column index")
    elif type(categorical_col) == pd.Series:
        raise Exception("categorical_col must be a column name or list of column names")

    if type(categorical_col) == int:
        if categorical_col < len(df.columns.values):
            categorical_col = df.columns.values[categorical_col]
        else:
            raise Exception("{} has to be a dataframe's column name or column index")
    elif (type(categorical_col) == list) or (type(categorical_col) == np.ndarray):
        if (col_name_format is not None) and (len(col_name_format) != len(categorical_col)):
            raise Exception("col_name_format must be a list and have same length as categorical_col")
        all_new_col_indices = list()
        for c, col in enumerate(categorical_col):
            df, new_col_indices = create_one_hot(df, col, col_name_format=col_name_format[
                c] if col_name_format is not None else None, levels_mapper=levels_mapper, dtype=dtype)
            all_new_col_indices.append(new_col_indices)
        return df, all_new_col_indices

    arr = df[categorical_col].values

    levels = levels_mapper
    if type(arr) == pd.core.arrays.categorical.Categorical:
        if arr.ordered:
            print("Not recommended to create one-hot encoding for ordered categorical variable.")
        if (levels is None) or (levels == "smart"):
            if dir(arr).__contains__("categories"):
                levels = arr.categories.values
            else:
                levels = arr.values.categories.values
    elif levels is None:
        levels = df[categorical_col].unique()
    elif levels == "smart":
        uniq_vals = df[categorical_col].unique()
        if (type(uniq_vals[0]) == str) or (type(uniq_vals[len(uniq_vals) - 1]) == str):
            levels = {}
            used_names = set()
            for val in uniq_vals:
                for suffix in [""] + ["_" + str(i) for i in range(1, 99)]:
                    if pd.isna(val):
                        name = "None{}".format(suffix)
                    elif val.find(" ") > 0:
                        name = "{}{}".format("".join([sub[:1] for sub in val.strip().split(" ")]), suffix)
                    else:
                        name = "{}{}".format(val[:8], suffix)
                    if not used_names.__contains__(name):
                        used_names.add(name)
                        levels[val] = name
                        break
        else:
            levels = uniq_vals

    if col_name_format is None:
        col_name_format = categorical_col + ".{}"

    new_col_indices = {}
    if type(levels) == dict:
        for data_val in levels:
            new_col = col_name_format.format(levels[data_val])
            if pd.isna(data_val):
                df[new_col] = pd.isna(arr)
            else:
                df[new_col] = arr == data_val
            if dtype is not None:
                df[new_col] = df[new_col].astype(dtype)
            new_col_indices[new_col] = np.argwhere(df.columns.values == new_col)[0][0]
    elif (type(levels) == list) or (type(levels) == np.ndarray):
        for data_val in levels:
            new_col = col_name_format.format(data_val)
            if pd.isna(data_val):
                df[new_col] = pd.isna(arr)
            else:
                df[new_col] = (arr == data_val)
            if dtype is not None:
                df[new_col] = df[new_col].astype(dtype)
            new_col_indices[new_col] = np.argwhere(df.columns.values == new_col)[0][0]
            if len(str(data_val)) > 8:
                print(
                    "One-hot encoded column name is too long. Consider using levels_mapper to map the long data value to a shorter code.")

    return df, new_col_indices


def shift_down(src_col, append_col_to_df=None, new_col_name=None, shift_by=1, fill_head_with="same"):
    if (type(src_col) == np.ndarray) or (type(src_col) == list):
        out_lst = list(src_col)
        out_lst[shift_by:] = src_col[:(-shift_by)]
    elif type(src_col) == pd.Series:
        out_lst = src_col.to_list()
        out_lst[shift_by:] = src_col.iloc[:(-shift_by)].to_list()
    elif (type(src_col) == str) and (append_col_to_df is not None):
        col_ind = np.argwhere(append_col_to_df.columns.values == src_col)
        if len(col_ind) == 0:
            raise Exception("'{}' column doesn't exist".format(src_col))
        col_ind = col_ind[0][0]
        out_lst = append_col_to_df[src_col].to_list()
        out_lst[shift_by:] = append_col_to_df.iloc[:(-shift_by), col_ind].to_list()
    else:
        raise Exception("Invalid src_col")

    if fill_head_with != "same":
        out_lst[:shift_by] = [fill_head_with]*shift_by

    if append_col_to_df is not None:
        if type(new_col_name) == str:
            append_col_to_df.loc[:, new_col_name] = out_lst
            return append_col_to_df
        elif type(src_col) == str:
            append_col_to_df.loc[:, src_col + ".prev"] = out_lst
            return append_col_to_df
        elif type(src_col) == pd.Series:
            append_col_to_df.loc[:, src_col.name + ".prev"] = out_lst
            return append_col_to_df

    return out_lst


def shift_up(src_col, append_col_to_df=None, new_col_name=None, shift_by=1, fill_tail_with="same"):
    if (type(src_col) == np.ndarray) or (type(src_col) == list):
        out_lst = list(src_col)
        out_lst[:(-shift_by)] = src_col[shift_by:]
    elif type(src_col) == pd.Series:
        out_lst = src_col.to_list()
        out_lst[:(-shift_by)] = src_col.iloc[shift_by:].to_list()
    elif (type(src_col) == str) and (append_col_to_df is not None):
        col_ind = np.argwhere(append_col_to_df.columns.values == src_col)
        if len(col_ind) == 0:
            raise Exception("'{}' column doesn't exist".format(src_col))
        col_ind = col_ind[0][0]
        out_lst = append_col_to_df[src_col].to_list()
        out_lst[:(-shift_by)] = append_col_to_df.iloc[shift_by:, col_ind].to_list()
    else:
        raise Exception("Invalid src_col")

    if fill_tail_with != "same":
        out_lst[(-shift_by):] = [fill_tail_with]*shift_by

    if append_col_to_df is not None:
        if type(new_col_name) == str:
            append_col_to_df.loc[:, new_col_name] = out_lst
            return append_col_to_df
        elif type(src_col) == str:
            append_col_to_df.loc[:, src_col + ".next"] = out_lst
            return append_col_to_df
        elif type(src_col) == pd.Series:
            append_col_to_df.loc[:, src_col.name + ".next"] = out_lst
            return append_col_to_df

    return out_lst


class DataFrameParallelTaskPartition:
    def __init__(self, data_slice):
        self.data_slice = data_slice
        self.n_pending = len(data_slice)

    def reduce(self, by=1):
        self.n_pending = self.n_pending - by

    def completed(self):
        return self.n_pending <= 0


class DataFramePartitionThread (threading.Thread):
    def __init__(self, thread_id, partition, task_func, *args):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.task_func = task_func
        self.args = args
        self.partition = partition

    def run(self):
        print("Starting thread[{}]".format(self.thread_id))
        # self.data.apply(self.task_func, 1, thread_id = self.thread_id, n_incomplete_rows_arr = self.n_incomplete_rows_arr)
        if len(self.args) == 0:
            for i, row in self.partition.data_slice.iterrows():
                row = self.task_func(row, i, self.partition.data_slice)
                if type(row) == pd.core.series.Series:
                    self.partition.data_slice.loc[i] = row
                self.partition.reduce()
        else:
            for i, row in self.partition.data_slice.iterrows():
                row = self.task_func(row, i, self.partition.data_slice, *self.args)
                if type(row) == pd.core.series.Series:
                    self.partition.data_slice.loc[i] = row
                self.partition.reduce()


def parallelize_for_dataframe(df, partition_filter_2D, task_func, print_progress_interval=30, *args):
    if (type(partition_filter_2D) != np.ndarray) or (partition_filter_2D.dtype != np.bool) or (len(partition_filter_2D.shape) != 2) or (partition_filter_2D.shape[0] != len(df)):
        raise Exception("partition_filter_2D must be a 2D boolean ndarray in shape (n_row, n_partition), where n_row = len(df) and n_partition is the number of threads to be used.")

    n_thread = partition_filter_2D.shape[1]
    n_total_rows_arr = np.sum(partition_filter_2D, axis=0)
    partitions = list()
    threads = list()

    start_time = datetime.now()
    print("Parallel processing starts at {}".format(start_time))
    for thread_id in range(n_thread):
        slice = df.loc[partition_filter_2D[:, thread_id]].copy()
        partition = DataFrameParallelTaskPartition(slice)
        partitions.append(partition)
        thread = DataFramePartitionThread(thread_id, partition, task_func, *args)
        threads.append(thread)
        thread.start()

    if print_progress_interval > 0:
        n_sec = 0
        n_incomplete_rows_arr = [partition.n_pending for partition in partitions]
        while np.sum(n_incomplete_rows_arr) > 0:
            time.sleep(print_progress_interval)
            n_sec += print_progress_interval
            print("{} min completion %: {}".format(round(n_sec / 60, 1), list(np.round((1 - n_incomplete_rows_arr / n_total_rows_arr) * 100, 1))))
            n_incomplete_rows_arr = [partition.n_pending for partition in partitions]
    else:
        for thread in threads:
            thread.join()

    finish_time = datetime.now()
    total_sec = (finish_time - start_time).total_seconds()
    if total_sec > 60:
        print("Parallel processing finishes at {}, taken {} minutes".format(finish_time, round(total_sec / 60, 1)))
    else:
        print("Parallel processing finishes at {}, taken {} seconds".format(finish_time, round(total_sec, 0)))

    return pd.concat([partition.data_slice for partition in partitions], ignore_index=False)


SEC_PER_HOUR = 60*60
SEC_PER_DAY = SEC_PER_HOUR * 24
SEC_PER_YEAR = SEC_PER_HOUR * 24 * 365


def friendly_text_for_duration(total_seconds, return_parts=False):
    if total_seconds < 3:
        parts = [np.round(total_seconds, 1), "second"]
    elif total_seconds < 60:
        parts = [int(np.round(total_seconds)), "second"]
    elif total_seconds < SEC_PER_HOUR:
        n_min = int(total_seconds / 60)
        n_sec = int(np.round(total_seconds - n_min * 60))
        if n_sec == 0:
            parts = [n_min, "minute"]
        else:
            parts = [n_min, "minute", n_sec, "second"]
    elif total_seconds < SEC_PER_DAY:
        n_hour = int(total_seconds / SEC_PER_HOUR)
        n_min = int((total_seconds - n_hour * SEC_PER_HOUR) / 60)
        if n_min == 0:
            parts = [n_hour, "hour"]
        else:
            parts = [n_hour, "hour", n_min, "minute"]
    elif total_seconds < SEC_PER_YEAR:
        n_day = int(total_seconds / SEC_PER_DAY)
        n_hour = int((total_seconds - n_day*SEC_PER_DAY) / SEC_PER_HOUR)
        if n_hour == 0:
            parts = [n_day, "day"]
        else:
            parts = [n_day, "day", n_hour, "hour"]
    else:
        n_year = int(total_seconds / SEC_PER_YEAR)
        n_day = int((total_seconds - n_year * SEC_PER_YEAR) / SEC_PER_DAY)
        if n_day == 0:
            parts = [n_year, "year"]
        else:
            parts = [n_year, "year", n_day, "day"]
    if return_parts:
        return parts
    else:
        texts = []
        for i in range(0, len(parts), 2):
            if (parts[i] == 0) or (parts[i] == 1):
                texts.append("{} {}".format(parts[i], parts[i + 1]))
            else:
                texts.append("{} {}s".format(parts[i], parts[i + 1]))
        return ", ".join(texts)


def movoper(arr, func, window_size, type, padding, padding_with=np.nan, forward_offset=1, stripe=1, return_valid_only=False):
    if len(arr) == 0:
        return arr

    n_arr = len(arr)
    output = np.repeat(padding_with, n_arr)
    vec = np.array([np.nan if pd.isna(num) else num for num in arr])

    if padding == "valid":
        if type == "c":
            start = int(np.ceil(window_size / 2.0)) - 1
            if (forward_offset == 1) and (window_size % 2 == 0):
                offsets = list(range(0, n_arr - window_size + 1, stripe))

                if return_valid_only:
                    output = np.empty(len(offsets))
                    for i, offset in enumerate(offsets):
                        output[i] = func(vec[offset:(offset + window_size)])
                else:
                    for offset in offsets:
                        output[start + 1 + offset] = func(vec[offset:(offset + window_size)])

            else:
                offsets = list(range(0, n_arr - window_size + 1, stripe))

                if return_valid_only:
                    output = np.empty(len(offsets))
                    for i, offset in enumerate(offsets):
                        output[i] = func(vec[offset:(offset + window_size)])
                else:
                    for offset in offsets:
                        output[start + offset] = func(vec[offset:(offset + window_size)])

        elif type == "s":
            start = window_size - 1
            offsets = list(range(0, n_arr - window_size + 1, stripe))

            if return_valid_only:
                output = np.empty(len(offsets))
                for i, offset in enumerate(offsets):
                    output[i] = func(vec[(start + offset + 1 - window_size):(start + offset + 1)])
            else:
                for offset in offsets:
                    output[start + offset] = func(vec[(start + offset + 1 - window_size):(start + offset + 1)])

        elif type == "f":
            offsets = list(range(0, n_arr - window_size + 1 - forward_offset, stripe))

            if return_valid_only:
                output = np.empty(len(offsets))
                for i, offset in enumerate(offsets):
                    output[i] = func(vec[(offset + forward_offset):(offset + forward_offset + window_size)])
            else:
                for offset in offsets:
                    output[offset] = func(vec[(offset + forward_offset):(offset + forward_offset + window_size)])

        else:
            raise Exception("Invalid type: {}. type must be 'c', 's' or 'f'.".format(type))

    elif padding == "same":
        if type == "c":
            if (forward_offset == 1) or (window_size % 2 != 0):
                offset_fore = int(np.floor(window_size / 2.0))
            else:
                offset_fore = int(np.floor(window_size / 2.0)) - 1
            offset_back = window_size - offset_fore - 1
            for offset in range(0, n_arr, stripe):
                start = offset - offset_fore
                end = offset + offset_back + 1
                if (start >= 0) and (end <= n_arr):
                    output_val = func(vec[start:end])
                elif (start < 0) and (end > n_arr):
                    output_val = func(np.concatenate([[padding_with] * (-start), vec, [padding_with] * (end - n_arr)]))
                elif start < 0:
                    output_val = func(np.concatenate([[padding_with] * (-start), vec]))
                else:
                    output_val = func(np.concatenate([vec, [padding_with] * (end - n_arr)]))

                if not pd.isna(output_val):
                    output[offset] = output_val

        elif type == "s":
            offset_fore = window_size - 1
            for offset in range(0, n_arr, stripe):
                start = offset - offset_fore
                end = offset + 1
                if start >= 0:
                    output_val = func(vec[start:end])
                else:
                    output_val = func(np.concatenate([[padding_with] * (-start), vec]))

                if not pd.isna(output_val):
                    output[offset] = output_val

        elif type == "f":
            for offset in range(0, n_arr - forward_offset, stripe):
                start = offset + forward_offset
                end = offset + forward_offset + window_size
                if end <= n_arr:
                    output_val = func(vec[start:end])
                else:
                    output_val = func(np.concatenate([vec, [padding_with] * (end - n_arr)]))

                if not pd.isna(output_val):
                    output[offset] = output_val

        else:
            raise Exception("Invalid type: {}. type must be 'c', 's' or 'f'.".format(type))

    else:
        raise Exception("Invalid padding: {}. padding must be 'valid' or 'same'.".format(padding))

    return output


def ma(arr, window_size=5, type="c", padding="valid", padding_with=0.0, forward_offset=1):
    return movoper(arr, np.nanmean, window_size, type, padding, padding_with, forward_offset)


def mov_mean(arr, window_size=5, type="c", padding="valid", padding_with=0.0, forward_offset=1):
    return movoper(arr, np.nanmean, window_size, type, padding, padding_with, forward_offset)


def mov_median(arr, window_size=5, type="c", padding="valid", padding_with=0.0, forward_offset=1):
    return movoper(arr, np.nanmedian, window_size, type, padding, padding_with, forward_offset)


def mov_sum(arr, window_size=5, type="c", padding="valid", padding_with=0.0, forward_offset=1):
    return movoper(arr, np.nansum, window_size, type, padding, padding_with, forward_offset)


def mov_max(arr, window_size=5, type="c", padding="valid", padding_with=0.0, forward_offset=1):
    return movoper(arr, np.nanmax, window_size, type, padding, padding_with, forward_offset)


def mov_min(arr, window_size=5, type="c", padding="valid", padding_with=0.0, forward_offset=1):
    return movoper(arr, np.nanmin, window_size, type, padding, padding_with, forward_offset)


def mov_all(arr, window_size=5, type="c", padding="valid", padding_with=False, forward_offset=1):
    return movoper(arr, np.all, window_size, type, padding, padding_with, forward_offset)


def mov_any(arr, window_size=5, type="c", padding="valid", padding_with=False, forward_offset=1):
    return movoper(arr, np.any, window_size, type, padding, padding_with, forward_offset)


def __test_ma():
    ma([1], 3, "f", "same")
    ma([1, 4], 3, "f", "same")
    ma([1, 4, 2], 3, "f", "same")
    ma([1, 4, 2, 10], 3, "f", "same")
    ma([1, 4, 2, None, 1], 3, "f", "same")
    ma([1], 3, "f", "same", forward_offset=0)
    ma([1, 4], 3, "f", "same", forward_offset=0)
    ma([1, 4, 2], 3, "f", "same", forward_offset=0)
    ma([1, 4, 2, 10], 3, "f", "same", forward_offset=0)
    ma([1, 4, 2, None, 1], 3, "f", "same", forward_offset=0)

    ma([1], 3, "s", "same")
    ma([1, 4], 3, "s", "same")
    ma([1, 4, 2], 3, "s", "same")
    ma([1, 4, 2, 10], 3, "s", "same")
    ma([1, 4, 2, None, 1], 3, "s", "same")

    ma([1], 3, "c", "same")
    ma([1, 4], 3, "c", "same")
    ma([1, 4, 2], 3, "c", "same")
    ma([1, 4, 2, 10], 3, "c", "same")
    ma([1, 4, 2, None, 1], 3, "c", "same")
    ma([1], 2, "c", "same")
    ma([1, 4], 2, "c", "same")
    ma([1, 4, 2], 2, "c", "same")
    ma([1, 4, 2, 10], 2, "c", "same")
    ma([1, 4, 2, None, 1], 2, "c", "same")
    ma([1], 2, "c", "same", forward_offset=0)
    ma([1, 4], 2, "c", "same", forward_offset=0)
    ma([1, 4, 2], 2, "c", "same", forward_offset=0)
    ma([1, 4, 2, 10], 2, "c", "same", forward_offset=0)
    ma([1, 4, 2, None, 1], 2, "c", "same", forward_offset=0)

    ma([1], 3, "f", "valid")
    ma([1, 3], 3, "f", "valid")
    ma([1, 3, 2], 3, "f", "valid")
    ma([1, 3, 2, 10], 3, "f", "valid")
    ma([1, 3, 2, None, 1], 3, "f", "valid")
    ma([1], 3, "f", "valid", forward_offset=0)
    ma([1, 3], 3, "f", "valid", forward_offset=0)
    ma([1, 3, 2], 3, "f", "valid", forward_offset=0)
    ma([1, 3, 2, 10], 3, "f", "valid", forward_offset=0)
    ma([1, 3, 2, None, 1], 3, "f", "valid", forward_offset=0)

    ma([1], 3, "s", "valid")
    ma([1, 3], 3, "s", "valid")
    ma([1, 3, 2], 3, "s", "valid")
    ma([1, 3, 2, 10], 3, "s", "valid")
    ma([1, 3, 2, None, 1], 3, "s", "valid")

    ma([1], 3, "c", "valid")
    ma([1, 3], 3, "c", "valid")
    ma([1, 3, 2], 3, "c", "valid")
    ma([1, 3, 2, 10], 3, "c", "valid")
    ma([1, 3, 2, None, 1], 3, "c", "valid")
    ma([1], 2, "c", "valid")
    ma([1, 3], 2, "c", "valid")
    ma([1, 3, 2], 2, "c", "valid")
    ma([1, 3, 2, 10], 2, "c", "valid")
    ma([1, 3, 2, None, 1], 2, "c", "valid")
    ma([1], 2, "c", "valid", forward_offset=0)
    ma([1, 3], 2, "c", "valid", forward_offset=0)
    ma([1, 3, 2], 2, "c", "valid", forward_offset=0)
    ma([1, 3, 2, 10], 2, "c", "valid", forward_offset=0)
    ma([1, 3, 2, None, 1], 2, "c", "valid", forward_offset=0)


# base_time = datetime(2020, 9, 10, 23, 2, 13)
# sn = np.linspace(0, 977, 978)
# date_time_arr = [base_time + timedelta(minutes=s*5) for s in sn]
# date_time_arr = localize_datetime([base_time + timedelta(minutes=s*5) for s in sn], "Asia/Singapore")
# date_time_arr = np.array([base_time + timedelta(minutes=s*5) for s in sn])
# date_time_arr = pd.Series([base_time + timedelta(minutes=s*5) for s in sn])
# date_time_arr = localize_datetime(pd.to_datetime(pd.Series([base_time + timedelta(minutes=s*5) for s in sn])))
# y = np.sin(sn / 50)
# # sn = np.linspace(0, 11520, 11520)
# # date_time_arr = localize_datetime(pd.to_datetime(pd.Series([base_time + timedelta(seconds=s) for s in sn])))
# # y = np.sin(sn/50)


