subject1 = int(input("Enter your subject1 marks: "))
subject2 = int(input("Enter your subject2 marks: "))
subject3 = int(input("Enter your subject3 marks: "))
subject4 = int(input("Enter your subject4 marks: "))
subject5 = int(input("Enter your subject5 marks: "))
subject6 = int(input("Enter your subject6 marks: ")) 
obtained_marks = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
percentage = (obtained_marks / 600) * 100
if percentage >= 90:
    print("A grade")
elif percentage >= 75:
    print("B grade")
elif percentage >=  35:
    print("C grade")
else:
    print("Fail")
print("Your percentage is: ", percentage)
print("Your obtained marks are: ", obtained_marks)