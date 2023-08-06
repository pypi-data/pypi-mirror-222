# value = get_value_by_key(jsn, key)
def get_value_by_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    for value in dictionary.values():
        if isinstance(value, dict):
            result = get_value_by_key(value, key)
            if result is not None:
                return result
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result = get_value_by_key(item, key)
                    if result is not None:
                        return result


# key_value_pairs = [("name", "John Smithxx"), ("makeId", 783)]
# update_values_by_keys(jsn, key_value_pairs)
def update_values_by_keys(dictionary, key_value_pairs):
    for key, new_value in key_value_pairs:
        if key in dictionary:
            dictionary[key] = new_value
        for value in dictionary.values():
            if isinstance(value, dict):
                update_values_by_keys(value, key_value_pairs)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        update_values_by_keys(item, key_value_pairs)
    return dictionary


# updated_jsn = update_dictionary_value(jsn, "name", "lksdjfldsjfs")
def update_dictionary_value(dictionary, key, new_value):
    if isinstance(dictionary, dict):
        for k, v in dictionary.items():
            if k == key:
                dictionary[k] = new_value
            elif isinstance(v, dict):
                update_dictionary_value(v, key, new_value)
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        update_dictionary_value(item, key, new_value)
    return dictionary


# update_frm_to_keys(jsn)
def update_frm_to_keys(jsn, dValue):
    # dValue=xst["engineCapacities"][1]
    # Retrieve the desired value from xst
    desired_value = dValue
    # Find the index of the desired value in jsn's engineCapacities
    index = next((i for i, item in enumerate(jsn["engineCapacities"]) if item["sort"] == desired_value["sort"]), None)

    # Update the value at the identified index in jsn
    if index is not None:
        jsn["engineCapacities"][index] = desired_value
    return jsn


def update_frm_to_values_keys(jsn, xst):
    # jsn = jsn["engineCapacities"]
    # xst = xst["engineCapacities"]
    for i in range(min(len(xst), len(jsn))):
        jsn[i] = xst[i]
    return jsn


# get_value_by_key(dictionary, "attributeRequests.attributeValueId")
def get_value_by_key_multiples(dictionary, key, atx=None):
    if '.' in key:
        key, atx = key.split('.')
    else:
        pass
    if key in dictionary:
        if isinstance(dictionary[key], dict):
            for nested_key, nested_value in dictionary[key].items():
                if nested_key in atx:  # ["name", "id", "attribute", "series"]:
                    return nested_value
        else:
            return dictionary[key]

    if isinstance(dictionary, dict):
        for value in dictionary.values():
            if isinstance(value, (dict, list)):
                result = get_value_by_key(value, key)
                if result is not None:
                    return result

    return None


# value = get_nested_value(dictionary, keys)
# Response : Add data infront / Request no need
def get_nested_value(data, keys="attributeRequests.attributeValueId"):
    if isinstance(keys, str):
        keys = keys.split(".")
    if len(keys) == 0:
        return data
    key = keys[0]
    remaining_keys = keys[1:]
    if isinstance(data, dict):
        if key in data:
            return get_nested_value(data[key], remaining_keys)
    elif isinstance(data, list):
        values = []
        for item in data:
            value = get_nested_value(item, keys)
            if value is not None:
                if isinstance(value, list):
                    values.extend(value)
                else:
                    values.append(value)
        return values
    return None
