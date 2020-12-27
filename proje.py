name='Emirhan'
surname='Arslan'
check=False
for i in range(3):
    loginName=input('Name:')
    loginSurname=input('Surname:')
    loginName.capitalize()
    loginSurname.upper()
    if loginName==name and loginSurname==surname :
        print(f"Welcome{name} {surname}")
        check=True
        break
    elif loginName!=name or loginSurname!=surname :
        print('Please try again')
    else:
        print('account could not be verified')
if not check:
    print('Sorry,you could not login')
    quit()


lessons=[]
count=0
for i in range(5):
    lesson=input('Add a lesson:')
    lessons.append(lesson)
    count+=1
    print('Do you want to add another lesson?  Yes or No')
    answer=input('answer:')
    if answer== 'No' or answer=='no' :
        if count>=3:
            print('Your lessons are ready')
            break
        else:
             print('You entered a small number of classes!\n closing')
             quit()
    elif answer=='yes'or answer=='Yes' :
         print('your lessons have been added')

exam=input("which lesson's to exams do you want to take? \n lesson:")
grades=[50,60,70]
exams={'midterm':0,'final':0,'project':0}
x=0
for i in exams:
    exams[i]=grades[x]
    x+=1
grade= (exams["midterm"]*30/100)+(exams["final"]*50/100)+(exams["project"]*20/100)

if 90<=grade<=100:
    print("Grade: ", grade)
    print("Your grade is AA")
elif 70<=grade<90:
    print("Grade: ", grade)
    print("Your grade is BB")
elif 50<=grade<70:
    print("Grade: ",grade)
    print("Your grade is CC")
elif 30<=grade<50:
    print("Grade: ", grade)
    print("Your grade is DD")
elif grade<30:
    print("Grade: ", grade)
    print("Your grade is FF\nYou should take the exam again!")
else:
    print("Invalid score!")
