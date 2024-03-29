# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

# Queues: A Tale of Two Stacks

# A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

# A basic queue has the following operations:

#     Enqueue: add a new element to the end of the queue.
#     Dequeue: remove the element from the front of the queue and return it.

# In this challenge, you must first implement a queue using two stacks. Then process
# queries, where each query is one of the following

# types:

#     1 x: Enqueue element 

#     into the end of the queue.
#     2: Dequeue the element at the front of the queue.
#     3: Print the element at the front of the queue.

# For example, a series of queries might be as follows:

# image

# Function Description

# Complete the put, pop, and peek methods in the editor below. They must perform the actions as described above.

# Input Format

# The first line contains a single integer,

# , the number of queries.

# Each of the next
# lines contains a single query in the form described in the problem statement above. All queries start with an integer denoting the query , but only query is followed by an additional space-separated value,

# , denoting the value to be enqueued.

# Constraints

# It is guaranteed that a valid answer always exists for each query of types and

#     .

# Output Format

# For each query of type

# , return the value of the element at the front of the fifo queue on a new line.

# Sample Input

# 10
# 1 42
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2

# Sample Output

# 14
# 14

# Explanation

# image

class MyQueue(object):
    def __init__(self):
        self.Fifo = []
        self.Lifo = []
        
    def peek(self):  #print the last item in Lifo or first in Fifo
        # return (f"3 has been called. Fifo: {self.Fifo}, Lifo: {self.Lifo}, Output: {self.Fifo[0]}")
        return self.Fifo[0]
        
    def pop(self): #dequeue
        if self.Lifo: #if Lifo is NOT empty
            self.Lifo.pop(-1)
            self.Fifo.pop(0)
            # print(f'2 has been called. Fifo: {self.Fifo}, Lifo:{self.Lifo}')

        else: #if Lifo is empty
            for item in self.Fifo:
                self.Lifo.insert(0,self.Fifo.pop())
                self.Lifo.pop(-1)
                # print('2 has been called')
                
    def put(self, value): #enqueue
        self.Lifo.insert(0,value)
        self.Fifo.insert(len(self.Fifo),value)
        # print(f"1 has been called. Fifo:{self.Fifo}, Lifo:{self.Lifo}")

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
