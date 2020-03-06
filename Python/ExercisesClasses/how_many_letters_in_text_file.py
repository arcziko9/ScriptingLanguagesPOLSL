def read_file(readFile):
    try:
        input_file = open(readFile, "r")
        input_data = str(input_file.read())
        input_file.close()
    except IOError:
        print("Failed to open the file")
        exit()
    return input_data

def get_letter():
        letter = str(input("Enter letter: "))
        return letter

def count_letter(input_data, letter):
    count = 0;
    for char in input_data:
        if char is letter:
            count += 1
    return count

input_data = readFile("zadanie93input.txt")
letter = get_letter()
print("Number of '" + letter +"' in '" + input_data + "' = "+ str(count_letter(input_data, letter)))
