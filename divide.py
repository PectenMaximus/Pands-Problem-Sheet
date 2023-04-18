# This program allows you to input two integers and divides the first integer by the second integer
# Author Alec Reid 18/04/2023

X = int( input ("Enter the First Number "))
Y = int( input ("Enter the Second Number 13"))
answer = (X//Y)
remainder = (X%Y)

print ("{} divided by {} is {} with remainder {}".format (X,Y,answer,remainder) )