class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def EnQueue(self, item):
        new_item = Node(item)

        if self.rear == None:
            self.front = self.rear = new_item
            return
        self.rear.next = new_item
        self.rear = new_item

    # Method to remove an item from queue
    def DeQueue(self):

        if self.isEmpty():
            print "there are no data to delete"
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None
        return str(temp.data)

    def userEnQueue(self):
        x = raw_input("Do you want to add new data")
        while True:
            if x == "yes":
                data = raw_input("please enter the data you want to add")
                self.EnQueue(data)
                x = raw_input("do you want to add other data")
            elif x == "no":
                break
            else:
                x = raw_input("please enter yes or no")

    def userDeQueue(self):
        y = raw_input("Do you want to delete any data ?")
        while True:
            if y == "yes":
                while True:
                    if self.isEmpty() is False:
                        x = raw_input("Do you want to delete " + self.front.data)
                        if x == "yes":
                            self.DeQueue()
                        elif x == "no":
                            y = "no"
                            break
                        else:
                            print "please enter yes or no"
                    else:
                        print "there are no items to delete"
                        print "The list is empty"
                        exit()
            elif y == "no":
                break
            else:
                print "please enter yes or no"

    def display(self):
        if self.isEmpty() is False:
            print "Saved data is :"
            temp = self.front
            while temp is not None:
                print temp.data
                temp = temp.next
        else:
            print "There are no data"





def main():
    q = Queue()
    q.EnQueue("test1") # add "test1"
    q.EnQueue("test2") # add "test2"
    q.DeQueue() # delete "test1"
    q.DeQueue()  # delete "test2"
    print q.isEmpty() #ptint True if list is empty, False if is not empty
    q.userEnQueue() # user adds data
    q.userDeQueue() # user chooses if he wants to delete the last data
    q.display()  # print all saved data if there is data

main()


