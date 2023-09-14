sub1 = int(input("Enter the first subject marks\n"))
sub2 = int(input("Enter the second subjct marks\n"))
sub3 = int(input("Enter the third subjct marks\n"))
if (sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in any subject")

elif(sub1+sub2+sub3)/3 <40:
    print("You are failled because total marks is less than 40%")
else:
    print("Congratulations You are passed in the examination")





