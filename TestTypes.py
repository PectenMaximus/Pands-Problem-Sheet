# Variable Types
# This code displays 5 variables for 5 different types
# Author: Alec Reid 18/04/2023

int = 4 + 3
float = 4.5
bool = True
str =  'Where then blue ben'
lots = [] 

print (f"type of answer is {type(int)}") 
print (f"type of answer is {type(float)}") 
print (f"type of answer is {type(bool)}")
print (f"type of answer is {type(str)}")
print (f"type of answer is {type(lots)}")

print ('variable {} is of type: {} and value: {}'.format ('str', type(str), (str)))
print ('variable {} is of type: {} and value: {}' .format ('int', type(int), (int)))
print ('variable {} is of type: {} and value: {}'.format('fl', type(float), (float)))
print ('variable {} is of type: {} and value: {}'.format ('boolean', type(bool), (bool)))
print ('variable {} is of type: {} and value: {}'.format('lots', type(lots), (lots)))