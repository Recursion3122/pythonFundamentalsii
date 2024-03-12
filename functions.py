# fuctions
# - consists of function name, parameters
# - starts "def" keyword.
# optimizes and make a block of code reusable.


# # void function
# def averageOfThreeNumbers(num1, num2, num3):
#     #codes ...
#     average = (num1 + num2 + num3) / 3
#     print("Average: ", average)

# SHORTCUT FOR COPYING HIGHLIGHTED/SINGLE LINE : alt + shift + ArrowDown/ArrowUp
# ALT = ArrowUp/Down
# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(56, 90, 90)
# averageOfThreeNumbers(80, 85, 84)

# return function

title = "Ang Alamat ni Loudie"
title2 = ": bagsakan Era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def joinString(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)

print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
# print(joinString(title, title2))
print(countLetters(title))