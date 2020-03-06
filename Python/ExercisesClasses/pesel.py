import re


class Pesel:
    def __init__(self, pesel):
        pattern1 = re.compile("^[0-9]{11}")
        pattern2 = re.compile("^(0[0-9]|10|11|12|$)")
        pattern3 = re.compile("^([0-2][0-9]|30|31$)")
        if (pattern1.match(pesel) and pattern2.match(pesel[2] + pesel[3]) and
                pattern3.match(pesel[4] + pesel[5])):

            self.birth_year = "19" + pesel[0] + pesel[1]
            self.birth_month = pesel[2] + pesel[3]
            self.birth_day = pesel[4] + pesel[5]
            pesel_array = [int(i, 11) for i in pesel]
            sex_check = str(pesel_array[7]) + str(pesel_array[8]) + str(pesel_array[9]) + str(pesel_array[10])
            if (int(sex_check) % 2) == 1:
                self.sex = "Male"
            else:
                self.sex = "Female"
            weight_array = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            control_sum_array = []
            for i in range(0, 10):
                value = weight_array[i] * pesel_array[i]
                control_sum_array.append(value)
            controlSum = sum(control_sum_array) % 10
            controlSum = (10 - controlSum) % 10
            if controlSum == pesel_array[10]:
                self.pesel = pesel
                print("PESEL is correct")
            else:
                print("PESEL is incorrect")

    def __str__(self):
        return "PESEL: " + self.pesel + "\nBirth year: " + self.birth_year + "\nBirth month: " + self.birth_month + "\nBirth day: " + self.birth_day + "\nSex: " + self.sex


test = Pesel(input("Enter PESEL: "))
print(test)
