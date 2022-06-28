import random

# A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# generating random characters
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
digit1 = (random.randint(1, 9))
digit2 = (random.randint(1, 9))
punctuationSign1 = chr(random.randint(33, 40))
punctuationSign2 = chr(random.randint(33, 40))


# combining all the characters of the password
passwordLetters = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + punctuationSign1 + punctuationSign2
passwordDigit1 = str(digit1)
passwordDigit2 =str(digit2)


# output of the password
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + passwordDigit1 + passwordDigit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)

print('Here is your password:', password)
print("\n")
input("Press enter to exit ;)")

