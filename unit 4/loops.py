
# A Python Loop is a programming concept where
# code repeats itself under specific conditions 

# In python, there are 2 versions of loops;for loop and
# while loop

# while Loops - A type of loop that will repeat a
# set of instructions so long as some condition is true

hp = 10
normalAttack = 2
normalAttack = 4
def battleFunction():
while hp > 0:
    print('Do you want to attack')
    hp -= normalAttack
    if hp == 0:
    else:
        print('game over')

#battleFunction()

# For Loops - this is a type of loop that iterates over a collection
# of data and will run a specific set of instuctions on data

numbers = [1,2,3,4,5,6,7,8]

for x in numbers:
    print(x)

attackValues =[10,25,50, 90]

for attacks in attackvalues:
    print (attack * 2)


def shoppingDioscountFunction(): 
    shoppingcart = []
    customerItem = input(''how much does this item cost'')
    shoppingCart.append(customerItem)
    print(''here are the item prices in your cart'')
    print