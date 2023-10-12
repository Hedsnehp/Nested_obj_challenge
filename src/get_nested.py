#Python script to execute the Nested object key challenge 



def get_nested_value(obj, key):
    try:
        for k in key.split('/'):
            obj = obj[k]
        return obj
    except (KeyError, TypeError):
        return None

object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"

object2 = {"x": {"y": {"z": "a"}}
key2 = "x/y/z"

value1 = get_nested_value(object1, key1)
value2 = get_nested_value(object2, key2)

print("Value 1:", value1)
print("Value 2:", value2)
