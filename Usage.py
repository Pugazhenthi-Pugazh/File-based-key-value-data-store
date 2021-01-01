import key_value_data_store_lib as kv
kv.create("apple",30) #create the key and vlue

kv.create("banana",20,5) #creating key value pairs with living time of the key

kv.read("apple") # reading the given key and return the key and value pair.

kv.delete("apple") # deleting the given key.

kv.delete("banana") #it will can not delete the key becuse its time is expired.