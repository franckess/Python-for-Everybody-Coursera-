## Assignment 3.1

# 3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))

if hrs <= 40:
    pay = hrs * rate
    print pay
else:
    pay = 40 * rate + (rate * 1.5 * (hrs - 40))
    print pay