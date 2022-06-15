# 1

filename = "Faze2.py"

scenario = ""

with open(filename) as f:
    content = f.read().splitlines()

for line in content:
    scenario = line[1:]
    break

lines = open(filename, 'r').readlines()
lines[0] = '#' + str(int(scenario) + 1) + '\n'
out = open(filename, 'w')
out.writelines(lines)
out.close()

print('Scenario #' + scenario)

studentsID = []

numberOfMajors = int(input('Enter number of students: '))

while numberOfMajors > 1001:
    numberOfMajors = int(input('Please enter a number less than 1000: '))

for x in range(numberOfMajors):
    studentsID.append([])

x = 0

while numberOfMajors != x:

    print('Enter Students Count and Students Id: ')

    _input = input().split(" ")

    count = _input[0]

    del _input[0]

    if int(count) != len(_input):

        print('count of students is not equal to number of students IDs')

    else:
        flag = False
        for y in range(int(count)):
            if int(_input[y]) > 999999 or int(_input[y]) < 0 and flag == False:
                print('student id is more than 999999 or less than 0')
                flag == True
                break

        if flag == False:
            studentsID[x] = _input.copy()
            x += 1

studentsIDInput = []

for x in range(numberOfMajors):
    studentsIDInput.append([])

studentsCount = 0

for x in range(numberOfMajors):
    studentsCount += len(studentsID[x])

studentsIn = 0

while studentsCount != 0 or studentsIn != 0:

    print('Enter your command:')

    _input = input()

    if _input == 'STOP':
        break

    command = _input[:7]

    if command == "ENQUEUE":
        if studentsCount != 0:

            _input = _input.split(" ")[1]

            studentID = int(_input)

            for x in range(numberOfMajors):
                if str(studentID) in studentsID[x]:
                    studentsIDInput[x].append(str(studentID))
                    studentsCount -= 1
                    studentsIn += 1
                    break
        else:
            print('All students have entered the queue')

    elif command == "DEQUEUE":

        if studentsIn != 0:
            for x in range(numberOfMajors):

                if len(studentsIDInput[x]) != 0:

                    print(str(studentsIDInput[x][0]))

                    del studentsIDInput[x][0]

                    studentsIn -= 1

                    break
        else:
            print('no students to leave')
    else:
        print('Unknown Command')

print(0)
