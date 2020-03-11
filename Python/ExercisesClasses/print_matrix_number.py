#Zadanie 86

l0 = """
 ### 
## ##
#   #
#   #
#   #
## ##
 ### 
"""

l1 = """
  ###
 ####
## ##
   ##
   ##
   ##
   ##
"""

l2 = """
 ### 
## ##
## ##
  ## 
 ##  
##   
#####
"""

l3 = """
#### 
   ##
   ##
#####
   ##
   ##
#### 
"""

l4 = """
   ##
  ###
 ## #
##  #
#####
   ##
   ##
"""

l5 = """
#####
##   
##   
#### 
   ##
   ##
#### 
"""

l6 = """
    #
   # 
  #  
 ### 
#   #
#   #
 ### 
"""

l7 = """
#####
#####
   ##
  ## 
  ## 
 ##  
##   
"""

l8 = """
 ### 
#   #
#   #
 ### 
#   #
#   #
 ### 
"""

l9 = """
 ### 
#   #
#   #
 ####
   ##
  ## 
##   
"""

alphabet = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]

def getNumber():

    while(True):

        value = input("Wprowadz liczbe: ")

        try:
            return int(value)
        except ValueError:
            print("Blad!")

n = getNumber()

outputLines = ["", "", "", "", "", "", ""]

def appendDigit(n):
    i = 0

    lines = n.splitlines()
    lines.pop(0)

    for line in lines:
        outputLines[i] += line + "  "
        i+=1


for letter in str(n):
    digit = int(letter)
    appendDigit(alphabet[digit])

for line in outputLines:
    print(line)