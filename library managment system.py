import datetime
import pickle
import os
os.system("cls")

book_racode=[ ] #all books details
barrow_recode= [ ] #all barrow book details
return_recode=[ ] #all barrow book details
data= dict()
#get the date from the user
def _qustion_():
    book_name= str(input("book name: "))
    book_author= str(input("book auathor: "))
    book_isbn= str(input("book ISBN number: "))
    data.update({"name":f"{book_name}","author":f"{book_author}","ISBN": f"{book_isbn}"})
    return data

#if the user whont to continuor exit 
def __continu__():
    print(''' \t\t>>>>>>>pleace coose number<<<<<<<<<\n\t 1. exit\t\t 2. continue ''')
    choose_num= int(input("enter the number :"))  
    if choose_num == 1:
        print('''________________Tank you________________''')
    elif choose_num ==2:
        __front_page_()

# create a table
def __table__(lis,num):
    if num ==3:
        print("+---------------+---------------+----------+")
        print("| Book name     | Book auathor  | book ISBM|")
        print("+---------------+---------------+----------+")
        for item in lis:
            print("|",(item["name"])," "*(12-len(item["name"])),"|",item["author"]," "*(12-len(item["author"])),"|",(item["ISBN"])," "*(7-len(item["ISBN"])),"|")
            print("+---------------+---------------+----------+")
    else:
        print("+---------------+---------------+----------+------------+-------------+")
        print("| Book name     | Book auathor  | book ISBM| date       | time        |")
        print("+---------------+---------------+----------+------------+-------------+")
        for item in lis:
            print("|",(item["name"])," "*(12-len(item["name"])),"|",item["author"]," "*(12-len(item["author"])),"|",(item["ISBN"])," "*(7-len(item["ISBN"])),"|",(item["date"])," ","|",(item["time"])," ","|")
            print("+---------------+---------------+----------+------------+------------+")

 #add a book
def __add__():
        _qustion_()
        book_racode.append(data) 
        pickle.dump(book_racode, open("book reacode.dat","wb"))
        __continu__()
        return book_racode

#barrow a book
def __barrow__():
    _qustion_()
    if data in book_racode:
        massge_box=print("this book is avilable")
        date= str(datetime.datetime.now().strftime('%y/%m/%d'))
        time= str(datetime.datetime.now().strftime('%H:%M:%S'))
        data.update({"date":date,"time":time})
        barrow_recode.append(data)
        book_racode.remove(data)
        pickle.dump(barrow_recode,open("barrow reacode.dat","wb"))
    else:
        massge_box=print("this book not avilable")
    print(massge_box) 
    __continu__()
    return barrow_recode
    
#retun book
def __retun__():
    _qustion_()
    if data in barrow_recode:
        massge_box=print("----------this book not avilable--------- \n you can retun")
        book_racode.append(data)
        date= str(datetime.datetime.now().strftime('%y/%m/%d'))
        time= str(datetime.datetime.now().strftime('%H:%M:%S'))
        data.update({"date":date,"time":time})
        return_recode.append(data)
        pickle.dump(return_recode,open("return reacode.dat","wb"))  
    else:
        massge_box=print("---------Tis book is avilable---------\n pleace chak book details") 
    print(massge_box) 
    __continu__()
    return return_recode
    
#viwe deatails
def __viwe__():
    print('''\t\t>>>>>>>>>>>>pleace coose the number<<<<<<<<<<<<<<<\n \t 1. barrow book deatils\n\t 2. retun book detais\n \t 3. all avilable books''')
    coose_num_viwe= int(input("what book do you wont to viwe? "))
    if coose_num_viwe == 1:

        __table__(pickle.load(open("barrow reacode.dat","rb")),coose_num_viwe)
    elif coose_num_viwe == 2:
        __table__(return_recode,coose_num_viwe)
    elif coose_num_viwe == 3:
        __table__(pickle.load(open("book reacode.dat","rb")),coose_num_viwe)
    __continu__()  


def _servis_(num):

    if num == 1:
        __add__()
    elif num ==2:
        __barrow__()
    elif num ==3:
        __retun__()
    elif num == 4:
        __viwe__()
    
    
        
#this is the front page  
def __front_page_():
    print('''\t\t>>>>>>>>>>>>>>> plece choose the number<<<<<<<<<<<<<<<<<\n \t 1. add a book\n \t 2. barrow a book\n \t 3. retun a book\n \t 4. viwe details''')
    coose_num= int(input("what servis do you need:"))
    _servis_(coose_num)

#funtion call
__front_page_()
