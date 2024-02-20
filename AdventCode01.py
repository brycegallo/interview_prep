def processLines2():
    input = open('input.txt', 'r')
    lines = input.readlines()

    sum_total = 0

    for line in lines:
        cal_value = ""
        while len(cal_value) == 0:
            for i in range(0, len(line)):
                if line[i].isdigit():
                    cal_value += line[i]
                    break
        for i in range(len(line) - 1, 0 - 1, -1):
            if line[i].isdigit():
                cal_value += line[i]
                break
        sum_total += int(cal_value)

    return sum_total


print(processLines2())

