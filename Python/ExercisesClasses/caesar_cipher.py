class CaesarCipher:
    def __init__(self, word):
        self.word = word

    def code(self, word, key):
        alphabet = "ABCDEĘFGHIJKLMNOPQRSTUVWXYZ"
        output_string = ""
        for letter in word:
            if letter.isalpha():
                letter = alphabet[(alphabet.index(letter) + key) % len(alphabet)]
            output_string = output_string + letter
        print(output_string)

    def decode(self, word, key):
        alphabet = "ABCDEĘFGHIJKLMNOPQRSTUVWXYZ"
        output_string = ""
        for letter in word:
            if letter.isalpha():
                letter = alphabet[(alphabet.index(letter) - key) % len(alphabet)]
            output_string = output_string + letter
        print(output_string)


key = int(input("Enter key: "))
inputString = input("Enter word: ").upper()
print("---------------------------------------------------------")
print("1. Code")
print("2. Decode")
choice = input("Your choice: ")

code_object = Cezar(inputString.upper())
if choice == '1':
    code_object.szyfrowanie(code_object.word, key)
elif choice == '2':
    code_object.deszyfrowanie(code_object.word, key)
else:
    print("There is no such choice")
