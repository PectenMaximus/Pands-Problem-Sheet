# This programme reads the percentage value and issues the corresponding grade 
# Author Alec Reid 20/04/2023

percentage = float (input(" Enter a percentage "))

if percentage > 100:  
    print ("Please enter a number between 0 and 100")

elif percentage <40:  
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60: 
    print ("Merit 1")
elif percentage < 70:
    print ("Merit 2")
elif percentage >70 or percentage <100: 
    print ("Distinction")

    