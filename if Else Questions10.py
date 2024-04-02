salary=int(input("Enter your Salary:"))
age=int(input("Enter yoyr age:"))
if(salary>=20000 or age<=25):
    Loan=int(input("Enter you loan amount:"))
    if(Loan<=50000):
        print("You are eligible for loan amount!")
    elif(Loan>50000):
        print("Max loan amount is 500000")
else:
    print("You are not eligible for loan amount!")
