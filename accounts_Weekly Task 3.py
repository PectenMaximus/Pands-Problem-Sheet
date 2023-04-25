# This programme reads in a 10 character account number and outputs the account number with only the last 4 digits showing.
# The first 6 digitis are hidden with X symbols.

# Author Alec Reid 25/04/2023

Account_number = (input("Please Enter Your Account Number "))
Last_4_digits = Account_number [5:9]
print ("Your Account Number is","XXXXXX", Last_4_digits) 

# Here I used the slicing string feature to isolate the last four digits of the string
