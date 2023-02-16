x=1
marks=67
grades=4000
#if statement
if x>0:print("the number is positive")
print(4+12)

#if else statement
if marks>=60:print("you have passed")
else:print("you have failed")

#if..elis..else
if grades<=25 and grades>=0:
    print("you have failed")
elif grades<=49 and grades>=30:
    print("you have passed")
elif grades<=79 and grades>=50:
    print("yuo have credit")
elif grades<=100 and grades>=80:
    print("yuo have distinction")
else:print("wrong input")