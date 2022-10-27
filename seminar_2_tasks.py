cw = input("What is your score form cw?")
exam = input("Your mark on exam?")
cw_mark = int(cw)
exam_mark = int(exam)
Final_mark = cw_mark*0.4+exam_mark*0.6
print(Final_mark)

check = Final_mark % 2

if check != 0:
    print("this is an odd number")
else:
    print("this is the even number")

def my_function():
    inputt = input("yes or no")
    if inputt == "Yes" or "yes" or "y":
        print("we are friends")
    else:
        print("I hate you")


my_function()


def add(a, b):
    answer = a + b
    print(answer)

add(9, 9)