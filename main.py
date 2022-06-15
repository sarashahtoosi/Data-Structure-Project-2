studentsID = []

numberOfStudents = int(input('Enter number of students: '))

while numberOfStudents > 10001:
    numberOfStudents = int(input('Please enter a number less than 10000: '))

while numberOfStudents != 0 or len(studentsID) != 0:

    print('Enter your command:')

    _input = input()

    command = _input[:7]
    
    if command == "ENQUEUE":

        if numberOfStudents == 0:

            print('you can\'t add any student')

        else:

            _input = _input[8:].replace(')', '')

            studentID = int(_input)

            studentsID.append(_input)

            numberOfStudents -= 1

    elif command == "DEQUEUE":

        if len(studentsID) == 0:

            print('\"no students to leave\"')

        else:
            
            print(studentsID[0])

            del studentsID[0]
        
    else:
        print('Unknown Command')


print('END')