name=input("First Name: ")
surname=input("Last Name: ")        
age=int(input("Age: "))
date=int(input("Date of birth(just year): "))

list=[name , surname , age , date]

for i in list:
    print(i)

if age < 18:
    print("You can't go out because it's too dangerous.")
elif age >= 18:
    print("You can go out to the street.")