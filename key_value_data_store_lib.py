import time 
import threading
import pathlib as path
import json

filepath = "D:\pugazh\File based key value data store\sample.json" #Default file path
data = {} #This  is a dictionary to store the  data

def changefilepath(path):  #optional file path funtion user can be change the file path
    filepath = path

def create(key,value,timeout=0):  #creating operation to create key and value with living time of key
    json_file = open(filepath, "r") #Reading the json file in the filepath
    data = json.load(json_file) # return the json object
    
    if key in data:
        print("Error: This key is already exists")
    else:
        if(key.isalpha()):
            if len(data)<(1024*1024*1024) and value<=(16*1024): # file size less than  1GB and  json object value less than 16KB
                if timeout == 0:
                    List=[value,timeout]
                else:
                    List=[value,time.time()+timeout] # to calculate the timeout value 
                if len(key)<=32: #input key neme at 32 char
                    data[key]=List
                    print("key and value is succesfully created")
            else:
                print("Error: Out of  Memory limit.")
        else:
            print("Error: Key name is invalid, key name must in alphabets and please enter the alphbets only.")
    outfile = open(filepath, "w") #write the given data in json object
    json.dump(data,outfile) #converting python object into json string

            
def read(key):  #Reading operation function
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
                return str(str1)+":"+str(str2) #return the key and value 
                
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
