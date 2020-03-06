try:
    file = open("inputSystemyLiczb.txt", 'r')
except IOError:
    print("Failed to open the file")

values = []
values_hex = []
values_oct = []
count = 0
for line in file:
    values.append(int(line))
    count = count + 1
for value in values:
    values_hex.append(hex(value))
    values_oct.append(oct(value))

new_file = open("outputSystemyLiczb.txt", "w")
new_file.write("Decimal | Octal | hexadecimal ")
for i in range(count):
    new_file.write("\n")
    new_file.write(str(values[i]) + "                  ")
    new_file.write(str(values_oct[i]) + "                  ")
    new_file.write(str(values_hex[i]) + "                  ")
