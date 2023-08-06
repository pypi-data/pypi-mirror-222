from itertools import groupby
from typing import List, Dict


def list_dict_group(data: List[Dict], key):
    new_data = {"list_data": list(), "dict_data": dict()}
    data.sort(key=lambda x: x.get(key, ""))
    group_data = groupby(data, key=lambda x: x.get(key, ""))
    for data_key, values in group_data:
        _values = list(values)
        new_data["list_data"].append({"key": data_key, "values": _values})
        new_data["dict_data"].update({data_key: _values})

    return new_data
