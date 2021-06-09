que=[]
size=int(input("enter the size to be inserted"))
rear=0
front=0
n=0

def insert():
    global front, rear, size,que
    if rear>=size:
        print("queue is full")
    else:
        p=int(input("enter the element to be inserted"))
        que.insert(rear,p)
        rear+=1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print("queue is empty")
    else:
        front+=1
        for i in range (front,rear):
            print(que[i])

while (True):
    print(".......enter the operation to be performed....")
    opt=int(input("press::1)INSERT 2)DELETE"))
    if opt==1:
        insert()
    elif opt==2:
        delete()