def make2to10(num):
    value = 0
    for i in range(len(num)):
        value += int(num[len(num)-1-i])*(2**i)
    return value

def make3to10(num):
    value = 0
    for i in range(len(num)):
        value += int(num[len(num)-1-i])*(3**i)
    return value

def check23(num2, num3):
    for i in range(len(num2)):
        for j in range(int(num2[i])):
            temp_num2 = num2[:i] + str(int(num2[i])-(j+1)) + num2[i+1:]
            temp_2 = make2to10(temp_num2)

            for q in range(len(num3)):
                for p in range(2-int(num3[q])):
                    temp_num3 = num3[:q] + str(int(num3[q])+(p+1)) + num3[q+1:]
                    temp_3 = make3to10(temp_num3)
                    if temp_2 == temp_3:
                        return temp_2
    return None

def check32(num3, num2):
    for i in range(len(num3)):
        for j in range(int(num3[i])):
            temp_num3 = num3[:i] + str(int(num3[i])-(j+1)) + num3[i+1:]
            temp_3 = make3to10(temp_num3)

            for q in range(len(num2)):
                for p in range(1-int(num2[q])):
                    temp_num2 = num2[:q] + str(int(num2[q])+(p+1)) + num2[q+1:]
                    temp_2 = make2to10(temp_num2)
                    if temp_2 == temp_3:
                        return temp_2
    return None

def check_plus(num2, num3):
    for i in range(len(num3)):
        for j in range(2-int(num3[i])):
            temp_num3 = num3[:i] + str(int(num3[i])+(j+1)) + num3[i+1:]
            temp_3 = make3to10(temp_num3)

            for q in range(len(num2)):
                for p in range(1-int(num2[q])):
                    temp_num2 = num2[:q] + str(int(num2[q])+(p+1)) + num2[q+1:]
                    temp_2 = make2to10(temp_num2)
                    if temp_2 == temp_3:
                        return temp_2
    return None

def check_minus(num2, num3):
    for i in range(len(num3)):
        for j in range(int(num3[i])):
            temp_num3 = num3[:i] + str(int(num3[i])-(j+1)) + num3[i+1:]
            temp_3 = make3to10(temp_num3)

            for q in range(len(num2)):
                for p in range(int(num2[q])):
                    temp_num2 = num2[:q] + str(int(num2[q])-(p+1)) + num2[q+1:]
                    temp_2 = make2to10(temp_num2)
                    if temp_2 == temp_3:
                        return temp_2
    return None

T = int(input())

for t in range(T):
    num2 = input()
    num3 = input()
    value_num2 = make2to10(num2)
    value_num3 = make3to10(num3)

    result = 0

    if value_num2 > value_num3:
        result = check23(num2,num3)
        if not result:
            result = check_plus(num2,num3)
        if not result:
            result = check_minus(num2,num3)
    else:
        result = check32(num3,num2)
        if not result:
            result = check_plus(num2,num3)
        if not result:
            result = check_minus(num2,num3)

    print("#{} {}".format(t+1, result))