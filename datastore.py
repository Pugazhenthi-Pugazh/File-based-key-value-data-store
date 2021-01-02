import time 
import threading
import os
import json

class datastore:
    def __init__(self):
        self.filepath = "D:\pugazh\File based key value data store\sample.json"  #Default file path
        self.data = {}  #This  is a dictionary to store the  data        
     
    def changefilepath(self,path):  #optional file path funtion user can be change the file path
        self.filepath = path
    def checkfilesize(self):
        if os.stat(self.filepath).st_size == 0:
            return False
        else:
            return True
        
    def create(self,key,value,timeout=0):  #creating operation to create key and value with living time of key
        if self.checkfilesize():
            json_file = open(self.filepath, "r")
            #Reading the json file in the filepath
            self.data = json.load(json_file) # return the json object
        else:
            outfile = open(self.filepath, "w") #write the given data in json object
            json.dump(self.data,outfile) #converting python object into json string

        if key in self.data:
            print("Error: This key is already exists")
        else:
            if(key.isalpha()):
                if len(self.data)<(1024*1024*1024) and value<=(16*1024): # file size less than  1GB and  json object value less than 16KB
                    if timeout == 0:
                        List=[value,timeout]
                    else:
                        List=[value,time.time()+timeout] # to calculate the timeout value 
                    if len(key)<=32: #input key neme at 32 char
                        self.data[key]=List
                        print("key and value is succesfully created")
                else:
                    print("Error: Out of  Memory limit.")
            else:
                print("Error: Key name is invalid, key name must in alphabets and please enter the alphbets only.")
        outfile = open(self.filepath, "w") #write the given data in json object
        json.dump(self.data,outfile) #converting python object into json string

                
    def read(self,key): #Reading operation function
        if self.checkfilesize():
            json_file = open(self.filepath, "r")
            self.data = json.load(json_file)
 
        if key not in self.data:
            print("Error: Entered key is not exist. Please enter the valid key")
        else:
            key_name = self.data[key]
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
                        
    def delete(self,key):
        if self.checkfilesize():
            json_file = open(self.filepath, "r")
            self.data = json.load(json_file)
        if key not in self.data:
            print("This",key,"key does not exist. Please enter the valid key")
        else:
            key_name = self.data[key]
            if key_name[1]!=0:
                if time.time()<key_name[1]:
                        if key in self.data:
                            del self.data[key]
                            print("key is deleted successfully")
                else:
                    print("Error: This ",key,"key time is expired")
            else:
                if key in self.data:
                            del self.data[key]
                print("Key is deleted successfully")
        outfile = open(self.filepath, "w")
        json.dump(self.data,outfile);

