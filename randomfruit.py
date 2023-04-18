# This program prints a random from from a defined set 
# Author Alec Reid 18/04/2023

import random
fruits = ['Apple', 'Tomatoe', 'Kiwi', 'Pineapple']

index = random.randint (0, len (fruits) -1)

fruit = fruits[index] 
print (" A random fruit is :{}" .format(fruit)) 