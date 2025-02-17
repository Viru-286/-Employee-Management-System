emp_Id= {
  101: {'name':'Satya\n','Age':27,'Department':'HR','Salary':50000},
  102: {'name':'Viren\n','Age':27,'Department':'IT','Salary':60000},
  103: {'name':'Samyak\n','Age':27,'Department':'Management','Salary':70000},
  104: {'name':'Pratham','Age':27,'Department':'Finance','Salary':80000},
 
}

def main_menu():
  print()
   

while True: 
   print("1.Add Employ:")
   print("2.View all employs:")
   print("3.Search for employ:")
   print("4.Exit:")

   choice= input("Enter your choice:")

   if choice == "1":
     Emp_Id = input("Enter Employ Id")
     Name= input("Enter the name: ")
     Age= input("\nEnter the age: ")
     Department= input("\nDepartment: ")
     Salary= input("\nsalary: ")
  
     emp_Id[Emp_Id]= {'nmae':Name,'Age':Age,'Department':Department,'Salary':Salary} 
  
   elif choice== "2":
    print(emp_Id)
  
   elif choice=="3":
      Emp_Id = input("Employ ID: ")
      if Emp_Id in emp_Id:
         print(emp_Id[Emp_Id])
      else:
          print("Wrond Employ Id:")
    
   elif choice=="4":
      print("Exiting")
 
      break
   else:
     print("Invalid choice")
