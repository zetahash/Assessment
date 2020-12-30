
"""
Created on Mon Dec 28 21:47:14 2020

@author: abnre
"""

import time

d={} 

def create_file(key,value,timetolive=0):
    if key in d:
        print("error: this key already does exist")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timetolive==0:
                    z=[value,timetolive]
                else:
                    z=[value,time.time()+timetolive]    
                if len(key)<=32: 
                    d[key]=z
            else:
                print("error: Memory limit exceeded ")
        else:
            print("error: Invalid keyname! keyname must contain only alphabets and no special characters or numbers")


            
def read_file(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        x=d[key]
        if x[1]!=0:
            if time.time()<x[1]: 
                string=str(key)+":"+str(x[0]) 
                return string
            else:
                print("error: time to live of",key,"has expired")
        else:
            string=str(key)+":"+str(x[0])
            return string



def delete_file(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        x=d[key]
        if x[1]!=0:
            if time.time()<x[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time to live of",key,"has expired")
        else:
            del d[key]
            print("key is successfully deleted")



def update_file(key,value):
    x=d[key]
    if x[1]!=0:
        if time.time()<x[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                z=[]
                z.append(value)
                z.append(x[1])
                d[key]=z
        else:
            print("error: time to live of",key,"has expired") 
    else:
        if key not in d:
            print("error: The key doesn't exist in database. Please enter a valid key") 
        else:
            z=[]
            z.append(value)
            z.append(x[1])
            d[key]=z