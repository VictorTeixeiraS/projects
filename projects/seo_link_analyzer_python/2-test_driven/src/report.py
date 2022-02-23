# remove_none_values removes all keys from a dictionary
# where the value was None
def remove_none_values(dict):
    keys_to_delete = []
    for key, value in dict.items():
        if value is None:
            keys_to_delete.append(key)
    for key_to_delete in keys_to_delete:
        del dict[key_to_delete]
    return dict
