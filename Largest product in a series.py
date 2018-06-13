#! Python 3

# Find the difference between the sum of the squares in a range and the square of the sum of the range

import pyperclip

print("Please input the number you would like to find the greatest product of 13 adjacent digits:")
InputNum = ''.join(pyperclip.paste().split())

InputLen = len(InputNum)

MaxProduct = 0

for i in range(InputLen - 12):
    Product = 1
    for j in range(13):
        Product *= int(InputNum[i+j])
    if Product > MaxProduct:
        MaxProduct = Product
print(MaxProduct)
    
