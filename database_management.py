import os
import psycopg2


# Get the value of an environment variable
db_user = os.getenv("DB_USER")   # returns None if not found
db_name = "ebooks"


def create_table():
    conn =psycopg2.connect(dbname=db_name, user=db_user,password='',host="localhost",port="5432")
    cur=conn.cursor()
    cur.execute("CREATE TABLE  ebooks(ebookid serial primary key, name text,price int,publisher text);")
    print("ebooks table created")
    conn.commit()
    conn.close()
def insert_data():
    name = input("Enter the name of book: ")
    price=int(input("Enter the price of book: "))
    publisher= input("Enter the name of publisher : ")
    conn =psycopg2.connect(dbname=db_name, user=db_user,password='',host="localhost",port="5432")
    cur=conn.cursor()
    cur.execute("""insert into ebooks (name,price,publisher) values (%s,%s,%s)""",(name,price,publisher))
    print("ebooks data inserted ")
    conn.commit()
    conn.close()

def read_data():
    conn =psycopg2.connect(dbname=db_name, user=db_user,password='',host="localhost",port="5432")
    cur=conn.cursor()
    cur.execute("select * from ebooks ;")
    ebooksdata=cur.fetchall()
    print("Displaying all ebooks records .")
    for ebook in ebooksdata:
        print(f"ID:{ebook[0]},name:{ebook[1]},price;{ebook[2]},publisher:{ebook[3]}")
        conn.close()
    
def update_data():
    ebookid =input("Enter the id of the book to be updated")
    name = input("Enter the name of the book to be updated")
    price = input("Enter the updated price of the book")
    publisher=input("Enter the udpated name of the publisher")
    conn = psycopg2.connect(dbname=db_name,user=db_user,password="",host="localhost",port="5432")
    cur=conn.cursor()
    cur.execute("""UPdate ebooks SET name=%s ,price=%s, publisher=%s WHERE ebookid = %s""",(name,price,publisher,ebookid))
    print("data updated successfully")
    conn.commit()
    conn.close()

def delete_data():
    ebookid=input("Enter the id of the book to be deleted: ")
    conn= conn = psycopg2.connect(dbname=db_name,user=db_user,password="",host="localhost",port="5432")
    cur=conn.cursor()
    cur.execute("Delete FROM ebooks where ebookid= %s ",(ebookid,))
    print("ebooks record deleted ")
    conn.commit()
    conn.close()

while True :
    print("\n Welcome to the ebooks management system ")
    print("1. Create Table ")
    print("2. Insert data")
    print("3.Read data")
    print("4.update data")
    print("5.delete date")
    print("6. Exit ")
    choice = input("Enter your choice 1 to 6 : ")
    if choice== "1":
        create_table()
    elif choice =="2":
        insert_data()
    
    elif choice =="3":
        read_data()
    elif choice =="4":
        update_data()

    elif choice =="5":
        delete_data()
    elif choice =="6":
        print("Exiting the program")
        break
    else:
        print("Invalid choice,please enter a valid number .")

