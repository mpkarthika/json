import threading 
from threading import*
import start_time
a={}#'a' is the dictionary to store data

#to create a file
def create_folder(key_value,number,end_time=0):
    if key_value in a:
        print("error: this key already exists") #1st error message
    else:
        if(key_value.isalpha()):
            if len(a)<(1024*1024*1020) and number<=(1024*16*1024): #file size less than 1GB and Jasonobject less than 16Kb
                if end_time==0:
                    new=[number,end_time]
                else:
                    new=[number,start_time.start_time()+end_time]
                if len(key_value)<=32: #for input capped at 32chars
                    a[key_value]=new
            else:
                print("error: Memory limit exceeded!!") #2nd error message
        else:
            print("error: Invalid keyname!! keyname must contain only alphabets and no special characters or numbers") #3rd error message
#to read file
def read_folder(key_value):
    if key_value not in a:
        print("error: Given key does not exist. Enter a valid key")#4th error message
    else:
        b=a[key_value]
        if b[1]!=0:
            if start_time.start_time()<b[1]: #comparing present and ending time
                string=s(key_value)+":"+s(b[0]) #returning value in JasonObject format
                return string
            else:
                print("error: time of",key_value,"expired") #5th error message
        else:
            string=s(key_value)+":"+s(b[0])
            return string
#to delete file
def delete_folder(key_value):
    if key_value not in a:
        print("error: Given key does not exist. Enter a valid key") #4th error message
    else:
        b=a[key_value]
        if b[1]!=0:
            if start_time.start_time()<b[1]:#comparing present and ending time
                del a[key_value]
                print("key is deleted successfully")
            else:
                print("error: time of",key_value,"expired")#5th error message
        else:
            del a[key_value]
            print("key is deleted successfully")
#to change the value before ending time
#to modify

def modify_folder(key_value,number):
    b=a[key_value]
    if b[1]!=0:
        if start_time.start_time()<b[1]:
            if key_value not in a:
                print("error: Given key does not exist. Enter a valid key")#6th error message
            else:
                new=[]
                new.append(number)
                new.append(b[1])
                a[key_value]=new
        else:
            print("error: time of",key_value,"expired")#5th error message
    else:
        if key_value not in a:
            print("error: Given key does not exist. Enter a valid key")#6th error message
        else:
            new=[]
            new.append(number)
            new.append(b[1])
            a[key_value]=new
