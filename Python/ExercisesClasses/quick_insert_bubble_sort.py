def bubble_sort(input_data):
    temporary = input_data

    for i in range(0, len(temporary) - 1):
        for j in range(0, len(temporary) - 1):
            if temporary[j] > temporary[j + 1]:
                temporary[j], temporary[j + 1] = temporary[j + 1], temporary[j]
    return temporary


def insertion_sort(input_data):
    temporary = input_data

    for i in range(2, len(temporary)):
        key = temporary[i]
        j = i - 1
        while j >= 0 and temporary[j] > key:
            temporary[j + 1] = temporary[j]
            j -= 1
        temporary[j + 1] = key
    return temporary


def quick_sort(input_data):
    def partition(input_data, beginning, end):
        x = input_data[end]
        i = beginning - 1

        for j in range(beginning, end):
            if input_data[j] <= x:
                i += 1
                input_data[i], input_data[j] = input_data[j], input_data[i]

        input_data[end], input_data[i + 1] = input_data[i + 1], input_data[end]

        return i + 1

    def main(input_data, beginning, end):
        if beginning < end:
            q = partition(input_data, beginning, end)
            main(input_data, beginning, q - 1)
            main(input_data, q + 1, end)

    temporary = input_data
    main(temporary, 0, len(temporary) - 1)

    return temporary


numbers = []

try:
    file = open("input104.txt", "r")
    for line in file.readlines():
        try:
            numbers.append(int(line))
        except ValueError:
            continue

    file.close()

    # BUBBLE SORT
    bubbleFile = open("output_bubble.txt", "w")

    for number in bubble_sort(numbers):
        bubbleFile.write(str(number) + "\n")

    bubbleFile.close()

    # INSERTION SORT
    insertionFile = open("output_insertion.txt", "w")

    for number in insertion_sort(numbers):
        insertionFile.write(str(number) + "\n")

    insertionFile.close()

    # QUICK SORT
    quickFile = open("output_quick.txt", "w")

    for number in quick_sort(numbers):
        quickFile.write(str(number) + "\n")

    quickFile.close()

except IOError:
    print("Error opening file")
