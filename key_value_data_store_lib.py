<<<<<<< HEAD
import os
import time 
import threading
import pathlib as path
import json

filepath = "D:\pugazh\File based key value data store\sample.json"
data = {}

def changefilepath(path):
    filepath = path

def create(key,value,timeout=0):
    json_file = open(filepath, "r")
    data = json.load(json_file)
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
    outfile = open(filepath, "w")
    json.dump(data,outfile);
            
def read(key):
    if key not in data:
        print("Error: Entered key is not exist. Please enter the valid key")
    else:
        key_name = data[key]
        if key_name[1]!=0:
            if time.time()<key_name[1]:
                string = str(key)+":"+str(key_name[0])
                return string       
            else:
                print("Error: This key is expired")
        else:
            string =  str(key)+":"+str(key_name[0])
            return string
                    
def delete(key):
    if key not in data:
        print("This",key,"key does not exist. Please enter the valid key")
    else:
        key_name = data[key]
        if key_name[1]!=0:
            if time.time()<key_name[1]:
                del data[key]
                print("key is deleted successfully")
            else:
                print("Error: This ",key,"key time is expired")
        else:
            del data[key]
            print("Key is deleted successfully")
            

create("oldkey",30)
            

=======
import os
import json
import time 
import threading

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
                string = string = json.dumps(data)
                return string       
            else:
                print("Error: This key is expired")
        else:
            string = string = json.dumps(data)
            return string
                    
def delete(key):
    if key not in data:
        print("This",key,"key does not exist. Please enter the valid key")
    else:
        key_name = data[key]
        if key_name[1]!=0:
            if time.time()<key_name[1]:
                del data[key]
                print("key is deleted successfully")
            else:
                print("Error: This ",key,"key time is expired")
        else:
            del data[key]
            print("Key is deleted successfully")
>>>>>>> e3e3f9870d50b9c8a29e743c1495c626fb0cbafa
