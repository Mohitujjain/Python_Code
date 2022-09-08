#Stack
#Implement a Stack and Queue Using a List Data Type:
#->The stack is a linear data structure. (sequentially)
#->Stores items in a Last-In/First-Out(FILO) manner.
#Stack Operation:
#1>Push => inserting an elements.
#2>Pop => Deletion An Element (last element)
#3>Peek=>Display the Last Element
#4>Display => Display List
#5=>Exit
'''

l=[]    #book in a rake,platein a party
while True:
    c=int(input('''
     #   1 Push Elements
     #   2 Pop Elements
    #    3 Peek Element
    #    4 Display Stack
    #    5 Exit
        
    # '''))
    #if c==1:
    # n=input("Enter The Value");
    #    l.append(n)
    #    print(l)
    #elif c==2:
    #    if len(l)==0:
    #        print("Empty Stack")
    #    else:
    #        p=l.pop()
    #       print(p)
    #       print(l)
    #elif c==3:
    #    if len(l)==0:
    #        print("Empty Stack")
    #    else:
    #        print("Last Stack Value",l[-1])
    #elif c==4:
    #    print("Display Stack",l)
    #elif c==5:
    #    break;
    #else:
    #    print("Invalid Opr...")

#QUEUE:-
#->The Queue is a linear data structure.
#->Stores items in first in first out(fifo),manner.

#Queue Operation.
#->1 Enqueue: Adds an item to the queue.
#->2 Dequeue: Removes an item from the queue.
#->3 Front: Get the front item from queue.
#->4 Rear: Get the last item from queue.
# train ticket buy on station

l = []  # book in a rake,platein a party
while True:
    c = int(input('''
        1 Push Elements
        2 Pop First Elements
        3 Front Element
        4 Last Elements
        5 Display Queue
        6 Exit

            '''))
    if c == 1:
        n = input("Enter The Value:-");
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Empty Stack")
        else:
            del l[0]

            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("First Queue Value", l[0])
    elif c == 4:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("First Queue Value", l[-1])
    elif c == 5:
        print("Display Queue", l)
    elif c == 6:
        break;
    else:
        print("Invalid Opr...")


