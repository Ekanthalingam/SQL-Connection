from tabulate import tabulate
import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="Ekan@2005",database="sql_python_connection")

def insert(cus_name,age,city_state):
    result=connection.cursor()
    sql="insert into cus_info (cus_name,age,city_state) values (%s,%s,%s)"
    user= (cus_name,age,city_state)
    result.execute(sql,user)
    connection.commit()
    print("Inserted Successfully")

def update(cus_name,age,city_state,cus_id):
    result=connection.cursor()
    sql= "update cus_info set cus_name=%s,age=%s,city_state=%s where cus_id=%s"
    user= (cus_name,age,city_state,cus_id)
    result.execute(sql,user)
    connection.commit()
    print("Inserted Successfully")

def select():
    result=connection.cursor()
    sql="select cus_id,cus_name,age,city_state from cus_info"
    result.execute(sql,)
    final_res=result.fetchall()
    print(tabulate(final_res,headers=["cus_id","cus_name","age","city_state"]))

def delete(cus_id):
    result=connection.cursor()
    sql= "Delete from cus_info where cus_id=%s"
    user= [cus_id]
    result.execute(sql,user)
    connection.commit()
    print("Data Deleted Successfully")

while True:
        print("1.Insert")
        print("2.Update")
        print("3.Select")
        print("4.Delete")
        print("5.Exit")
        choice=int(input("Enter your choice:"))

        if choice==1:
            cus_name=input("Enter cus_name:")
            age=input("Enter age:")
            city_state=input("Enter city state:")
            insert(cus_name,age,city_state)

        elif choice==2:
            cus_id=input("Enter cus_id:")
            cus_name=input("Enter cus_name:")
            age=input("Enter age:")
            city_state=input("Enter city state:")
            update(cus_name,age,city_state,cus_id)

        elif choice==3:
            select()

        elif choice==4:
            cus_id=input("Enter cus_id:")
            delete(cus_id)

        elif choice==5:
            quit()
