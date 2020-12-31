import time
import os
import json

data = {}
def create(key,value,timeout=0):
    if key in data:
        print("Error: This key is already exists")
    else:
        if(key.isalpha()):
            if len(data)<(1024*1024*1024) and value<=(16*1024):
                if timeout == 0:
                    List=[value,timeout]
                else:
                    List=[value,time.time()+timeout]
                if len(key)<=32:
                    data[key]=List
            else:
                print("Error: Out of  Memory limit.")
        else:
            print("Error: Key name is invalid, key name must in alphabets and please enter the alphbets only.")
def read(key):
    if key not in data:
        print("Error: Entered key is not exist. Please enter the valid key")
    else:
        key_name = data[key]
        if key_name[1]!=0:
            if time.time()<key_name[1]:
                 string =  json.dumps(key)
                 string2 = json.dumps(str(key_name[0])
                 print(string)
             
            else:
                print("Error: This key is expired")
        else:
            string =  json.dumps(key)
            string2 = json.dumps(str(key_name[0]))
            print(string,":",string2)
             