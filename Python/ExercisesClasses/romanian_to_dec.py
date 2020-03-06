def romToDec(year):
    convert = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'],  [9, 'IX'],  [5, 'V'],   [4, 'IV'],  [1, 'I']]

    result = 0
    for i in range(0, len(year)):
        for row in convert:
            if year[i] == row[1]:
                if row[0] > result:
                    result = row[0] - result
                else:
                    result += row[0]

    return result
print(romToDec("MXMV"))