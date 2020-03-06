# Zadanie 124
romanMap = [(1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')]


def rom(input):
    output = ""

    while input > 0:
        for i, r in romanMap:
            while input >= i:
                output += r
                input -= i

    return output


print(rom(1234))