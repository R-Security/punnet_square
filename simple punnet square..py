"""
Author = RAED AHSAN
Creation Date = 08/07/2022
Simple punnet Square | automated | Error detection functionality
R-Security
"""




# Input of values from user
a1 = input("ENTER ALELLE 1[R or r]: ")
a2 = input("ENTER ALELLE 2[R or r]: ")
b1 = input("ENTER ALELLE 3[R or r]: ")
b2 = input("ENTER ALELLE 4[R or r]: ")

# adding the values in an array[list]
array1 = [a1, a2]
array2 = [b1, b2]


# combining the values according to punnet square rules.
genes = (a1 + b1)
genes2 = (a1 + b2)
genes3 = (a2 + b1)
genes4 = (a2 + b2)

# displaying the alelles
print(genes)
print(genes2)
print(genes3)
print(genes4)


# for error detection; example : rR = [!] Error
for info in genes, genes2, genes3, genes4:
    if info == "rR":
        swap = info.swapcase()
        print("[!] Found incorrect value at, ", info)
        print("Original correct alelle : ", swap)