import gendiff.diff_states as ds


def mark_nested_keys(item):
    if not isinstance(item, dict):
        return item
    marked_dict = {}
    for key in item:
        value = item[key]
        marked_dict[(key, ds.NESTED)] = mark_nested_keys(value)
    return marked_dict


def compare_files(item1: dict, item2: dict) -> dict:
    item1_keys = set(item1.keys())
    item2_keys = set(item2.keys())

    mutual_keys = item1_keys & item2_keys
    item1_unique_keys = item1_keys - item2_keys
    item2_unique_keys = item2_keys - item1_keys

    diff = {}

    for key in item1_unique_keys:
        diff[(key, ds.DELETED)] = mark_nested_keys(item1[key])

    for key in item2_unique_keys:
        diff[(key, ds.ADDED)] = mark_nested_keys(item2[key])

    for key in mutual_keys:
        value1 = item1[key]
        value2 = item2[key]
        if value1 == value2:
            diff[(key, ds.SAME)] = mark_nested_keys(value1)
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff[(key, ds.NESTING)] = compare_files(value1, value2)
            else:
                diff[(key, ds.CHANGED)] = {
                    ds.CHANGED_FROM: mark_nested_keys(value1),
                    ds.CHANGED_TO: mark_nested_keys(value2)
                }

    return diff
