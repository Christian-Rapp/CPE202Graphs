
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.front = 0
        self.back = 0
        self.capacity = capacity
        self.list = [None]*capacity
        self.numItems = 0
        pass

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.numItems == 0
        pass

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.numItems == self.capacity
        pass

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if not self.is_full():
            self.list[self.back] = item
            self.numItems += 1
            self.back = (self.back + 1) % self.capacity
        else:
            raise IndexError
        pass

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if not self.is_empty():
            temp = self.list[self.front]
            self.front = (self.front + 1) % self.capacity
            self.numItems += -1
            return temp
        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.numItems

