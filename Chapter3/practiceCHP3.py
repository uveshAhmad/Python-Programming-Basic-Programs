#Problem1


#name = input("Enter your name\n")
#print("Good Night , " + name)

#problem2

letter = ''' Dear <|Name|>, 
You are selected!
Date : <|DATE|>
'''
name = input("Enter your Name\n")
date =  input("Enter Date\n")
letter = letter.replace("<|Name|>" ,name)
letter = letter.replace("<|Date|>" , date)
print(letter)
