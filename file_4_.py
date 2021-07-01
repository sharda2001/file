
def file1():
    file1=open("delhi.txt","r")
    c=0
    for i in (file1):
        c=c+1
        print(i)
    file1.close()
def file2():
    file2=open("shimla.txt","r")
    d=0
    for j in (file2):
        d=d+1
        print(j)
    file2.close()
def file3():
    file3=open("others.txt","r")
    e=0
    for k in (file3):
        e=e+1
        print(k)
    file3.close()
def main():
    user_choice=input("enter the name:_")
    if user_choice=="delhi":
        file1()
    elif user_choice=="shimla":
        file2()
    elif user_choice=="others":
        file3()
    else:
        pass
main()