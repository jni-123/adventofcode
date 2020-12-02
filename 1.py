from collections import Counter
def readInformation():
    infoFile = open('input1.txt','r')
    numbers = []
    for number in infoFile:
        numbers.append(int(number))
    return numbers

numbers = readInformation()
#print(numbers)

#print(search(2004,numbers))
def function(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (numbers[j] == 2020 - numbers[i]):
                return numbers[j],numbers[i]
    return 0
#print(function(numbers))
def new(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if (numbers[k] == 2020 - numbers[i] - numbers[j]):
                    return numbers[j],numbers[k],numbers[i]
    return 0
print(new(numbers))

    
