intCodes_permanent = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,5,27,2,27,10,31,1,31,9,35,1,35,5,39,1,6,39,43,2,9,43,47,1,5,47,51,2,6,51,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,2,10,71,75,1,6,75,79,2,79,9,83,1,83,5,87,1,87,9,91,1,91,9,95,1,10,95,99,1,99,13,103,2,6,103,107,1,107,5,111,1,6,111,115,1,9,115,119,1,119,9,123,2,123,10,127,1,6,127,131,2,131,13,135,1,13,135,139,1,9,139,143,1,9,143,147,1,147,13,151,1,151,9,155,1,155,13,159,1,6,159,163,1,13,163,167,1,2,167,171,1,171,13,0,99,2,0,14,0]
intCodes = intCodes_permanent
intCodes[1] = 12
intCodes[2] = 2
list_of_ints = []


def try_codes(int_code: int, noun: int, verb: int):
    if int_code == 1:
        return intCodes[noun]+intCodes[verb]
    elif int_code == 2:
        return intCodes[noun]*intCodes[verb]
    elif int_code == 99:
        return False
    else:
        raise ValueError("Value is not 1, 2, or 99")

def update_list():
    loi = []
    tups = ()
    i = 0
    for j in intCodes:
        tups += (j,)
        if len(tups) == 4 or i == len(intCodes):
            loi.append(tups)
            tups = ()
        i += 1
    return loi
list_of_ints = update_list()

for t in list_of_ints:
    returned = try_codes(t[0], t[1], t[2])
    if returned:
        intCodes[t[3]] = returned
    else:
        break
print("Part1: IntCode 0: ", intCodes[0])
intCodes = intCodes_permanent

def gravity_assist():
    for noun in range(0,100):
        for verb in range(0,100):
            intCodes = intCodes_permanent
            intCodes[1] = noun
            intCodes[2] = verb
            for t in list_of_ints:
                returned = try_codes(t[0], t[1], t[2])
                if returned:
                    intCodes[t[3]] = returned
                else: 
                    break
                if intCodes[0] == 19690720:
                    print(intCodes[0])
                    print(f"Noun: {noun}\nVerb: {verb}\n")
                    print('Answer: ' + str((100*noun)+verb))
                    return
gravity_assist()
