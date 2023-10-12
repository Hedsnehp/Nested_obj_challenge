# Nested_obj_challenge


CHALLENGE: 
We have a nested object. We would like a function where you pass in the object and a key and 
get back the value. 
The choice of language and implementation is up to you.
Example Inputs
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a

STEPS EXPLAINED:

This block of code defines a function named get_nested_value which takes two arguments: obj (a dictionary) and key (a string).
Inside the function, there's a try block, which is used to handle exceptions.
The for loop iterates over the keys obtained by splitting the input key using /.
For each key k in the split keys, obj is updated to be obj[k]. This effectively drills down into the nested structure of obj.
If the loop completes without any errors, it means the value has been successfully retrieved, and it is returned.
If an exception occurs (either KeyError or TypeError), it means that the specified key was not found, or there was a type error (e.g., trying to index a non-dictionary object). In this case, None is returned

These lines define two dictionaries (object1 and object2) with varying levels of nesting.
They also define two strings (key1 and key2) that represent the paths to retrieve a specific value from each respective object.

These lines call the get_nested_value function with the provided objects and keys.
value1 will contain the result of attempting to retrieve the value at the path 'a/b/c' from object1.
value2 will contain the result of attempting to retrieve the value at the path 'x/y/z' from object2

These lines print out the values obtained from the get_nested_value calls
