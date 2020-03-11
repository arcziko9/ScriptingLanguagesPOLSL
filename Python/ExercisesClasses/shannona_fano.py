alpha = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

mode = int(input("Zaszyfruj: 0\nOdszyfruj: 1\nWybierz tryb: "))
phrase = input("Podaj ciąg: ").upper()
key = int(input("Podaj klucz: "))
processed = ""

print(phrase)
if mode == 0:
    for c in phrase:
        if c.isalpha():
            c = alpha[(alpha.index(c) + key) % len(alpha)]
        processed = processed + c

if mode == 1:
    for c in phrase:
        if c.isalpha():
            c = alpha[(alpha.index(c) - key) % len(alpha)]
        processed = processed + c

print(f"\nTekst pierwotny: {phrase}")
print(f"Tekst przetworzony: {processed}")