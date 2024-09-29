#While loop
'''n = 1
while n > 0:
    n += 1
    if n == 100:
        break
    print(n)

#by pop() function we will remove last subject until the list become empty
#when the list become empty the lopp will terminate because Python treats the empty list as false
subjects = ['Data Structure', 'System Design', 'Math', 'Social Ethics']
while subjects:
    subjects.pop(-1)
    print(subjects)

Tapo = (1, 2, 3, 4, 5)
while Tapo:
    print(Tapo)
    break #The break statment will terminate the loop once after printing the tuple
'''
#for loop
Tapo = (1, 2, 3, 4, 5)
for i in Tapo:
    print(i) #this prints each element in the tuple
    print(Tapo) #this prints the whole tuple 5 times since the tuple has 5 elements

