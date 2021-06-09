stk=[]
size=int(input("enter the size of the stack"))
top=0
n=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        p=int(input("enter the element to be pushed"))
        stk.append(p)
        top+=1
        print(stk)

def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        stk.pop()
        top-=1
        print(stk)

while (True):
    print(".......enter the operation to be performed....")
    opt=int(input("press::1)PUSH 2)POP"))
    if opt==1:
        push()
    elif opt==2:
        pop()