'''
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
'''
from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        start = 0
        end = len(students)-1
        notFound = False

        while  True:
            print(start,end)
            length = len(students)
            if length ==0: return 0

            if students[start] == sandwiches[0]:
                students.pop(start)
                sandwiches.pop(0)
                if length -1 == 0 : return 0

                start = start %  (length-1)
                end = (start -1) % (length-1)
                notFound = False
            else:
                if start ==0: notFound = True
                start = (start + 1) % length
                end = (end +1) % length
                if notFound and start ==0: return len(students)

students = [1,1,0,0]
sandwiches = [0,1,0,1]


Solution().countStudents(students,sandwiches)