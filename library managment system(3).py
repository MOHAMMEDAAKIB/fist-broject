import datetime

class book:
    
    def __book_details__(self):
        data= dict()
        book_name= str(input("book name: "))
        book_author= str(input("book auathor: "))
        book_isbn= str(input("book ISBN number: "))
        data.update({"name":f"{book_name}","author":f"{book_author}","ISBN": f"{book_isbn}"})
        return data

book=book()
book_racode=[ ]  
barrow_recode=[ ]
return_recode=[ ]
barrow_recode_not_date_time=[]
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

class library:
    # create a table
    

    def __add__(self):
        data=book.__book_details__()
        book_racode.append(data)
        return book_racode ,__continuas__()

    #barrow a book
    def __barrow__(self):
        data=book.__book_details__()
        if data  in book_racode:
            i= book_racode.index(data)
            massge_box=print("this book is avilable")
            date= str(datetime.datetime.now().strftime('%y/%m/%d'))
            time= str(datetime.datetime.now().strftime('%H:%M:%S'))
            barrow_recode_not_date_time.append(data)
            data.update({"date":date,"time":time})
            barrow_recode.append(data)
            del book_racode[i]
            
        else:
            massge_box=print("this book not avilable")
        print(massge_box) 
    
        return barrow_recode ,__continuas__()
        
    #retun book
    def __retun__(self):
        data=book.__book_details__()
        if data not in book_racode:
            massge_box=print("----------this book not avilable--------- \n you can retun")
            book_racode.append(data)
            date= str(datetime.datetime.now().strftime('%y/%m/%d'))
            time= str(datetime.datetime.now().strftime('%H:%M:%S'))
            data.update({"date":date,"time":time})
            return_recode.append(data)  
        else:
            massge_box=print("---------Tis book is avilable---------\n pleace chak book details") 
        print(massge_box) 
       
        return return_recode , __continuas__()
        
        
    #viwe deatails
    def __viwe__(self):
        print('''\t\t>>>>>>>>>>>>pleace coose the number<<<<<<<<<<<<<<<\n \t 1. barrow book deatils\n\t 2. retun book detais\n \t 3. all avilable books''')
        coose_num_viwe= int(input("what book do you wont to viwe? "))
        if coose_num_viwe == 1:
            __table__(barrow_recode,coose_num_viwe)
        elif coose_num_viwe == 2:
            __table__(return_recode,coose_num_viwe)
        elif coose_num_viwe == 3:
            __table__(book_racode,coose_num_viwe)
        __continuas__()
    

library=library()
def _servis_(num):
    if num == 1:
        library.__add__()
    elif num ==2:
        library.__barrow__()
    elif num ==3:
        library.__retun__()
    elif num == 4:
        library.__viwe__()

def __continuas__():
    print(''' \t\t\t<<<<<<<<plleace choose a number>>>>>>>\n\t 1.countinu \n\t 2.exit''')
    num = int(input("enter the number :  "))
    if num ==2:
        print('''________________Tank you________________''')
    elif num==1:
        __front_page_()
        
def __front_page_():
    print('''\t\t>>>>>>>>>>>>>>> plece choose the number<<<<<<<<<<<<<<<<<\n \t 1. add a book\n \t 2. barrow a book\n \t 3. retun a book\n \t 4. viwe details''')
    coose_num= int(input("what servis do you need:"))
    _servis_(coose_num)


__front_page_()
          
        
            
   

