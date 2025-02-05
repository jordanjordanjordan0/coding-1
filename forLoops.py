
# FOR LOOPS - Is a type of loop that iterate over a list
# it will go through your list and do whatever operation
# you want it to do

# for loops use an iterator, which is just a varaible
# that is intended to represent a value in the list

# the "IN" keyword gives us access to the list we
# want to go through

def grocery():
groceryList = [ 'apple','water','milk','chicken']
for x in groceryList:
    if x == 'milk':
        groceryList.remove(x)
        print('the value being removed is: ' + x)
    print(x)

gradeList =[100, 70, 90, 70, 65, 95]

for grade in gradeList:
    if x < 75:
        continue
    print(x)                    

for grade in gradeList:
    gradeList.append(85)
    print(grade)
    break

# add all the number together and then return the
# value in the for loop