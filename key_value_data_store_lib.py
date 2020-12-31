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
    json.dump(data,outfile)
    print("key and value is succesfully created")
            
def read(key):
    json_file = open(filepath, "r")
    data = json.load(json_file)
    if key not in data:
        print("Error: Entered key is not exist. Please enter the valid key")
    else:
        key_name = data[key]
        if key_name[1]!=0:
            if time.time()<key_name[1]:
                str1 = key
                str2 = key_name[0]
                return str(str1)+":"+str(str2)
                
            else:
                print("Error: This key is expired")
        else:
            str1 = key
            str2 = key_name[0]
            return (str1)+ ":" +str(str2)
                    
def delete(key):
    
    json_file = open(filepath, "r")
    data = json.load(json_file)
    if key not in data:
        print("This",key,"key does not exist. Please enter the valid key")
    else:
        key_name = data[key]
        if key_name[1]!=0:
            if time.time()<key_name[1]:
                    if key in data:
                        del data[key]
                        print("key is deleted successfully")
            else:
                print("Error: This ",key,"key time is expired")
        else:
            if key in data:
                        del data[key]
            print("Key is deleted successfully")
    outfile = open(filepath, "w")
    json.dump(data,outfile);
<<<<<<< HEAD
    
=======

>>>>>>> 89c749c1394b5d10cd0a5b9881607f8d32cd9c43
