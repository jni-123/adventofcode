def readInformation():
    infoFile = open('day2.txt','r')
    numbers = []
    for number in infoFile:
        numbers.append(number)
    return numbers

numbers = readInformation()
#print(numbers)
def function():
    array = []
    number = []
    letter = []
    password = []
    for i in range(len(numbers)):
        array.append(numbers[i].split())
    #
    for i in range(len(array)):
        number.append(array[i][0].split('-'))
    for i in range(len(array)):
        letter.append(array[i][1][0])
    for i in range(len(array)):
        password.append(array[i][2])
    for i in range(len(array)):
        number[i][0] = int(number[i][0])
        number[i][1] = int(number[i][1])

    total = 0
    for i in range(len(numbers)):
        count = 0
        for j in range(len(password[i])):
            if (password[i][j] == letter[i]):
                count = count + 1
        if ((count >= number[i][0]) and (count <= number[i][1])):
            total = total + 1
        
    return total

def new():
    array = []
    number = []
    letter = []
    password = []
    for i in range(len(numbers)):
        array.append(numbers[i].split())
    #
    for i in range(len(array)):
        number.append(array[i][0].split('-'))
    for i in range(len(array)):
        letter.append(array[i][1][0])
    for i in range(len(array)):
        password.append(array[i][2])
    for i in range(len(array)):
        number[i][0] = int(number[i][0])
        number[i][1] = int(number[i][1])

    total = 0
    for i in range(len(numbers)):
        count = 0
        if (password[i][number[i][0]-1] == letter[i]):
            count = count + 1
        if (password[i][number[i][1]-1] == letter[i]):
            count = count + 1
        if (count == 1):
            total = total + 1

    return total 
print(new())
