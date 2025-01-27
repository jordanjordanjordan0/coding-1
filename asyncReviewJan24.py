# Review the order of the list provided

numberList = [1,23,56,3,20,200]

def reverseLoop():
        print(len(numberList))
        listCount = 7
        while listCount >= 0:
                print(numberList[listCount])
                listCount -=1
    
reverseLoop()

numberList.reverse()
print(numberList) 