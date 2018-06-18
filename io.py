# def Fibonacci(var):
#     a = 0
#     b = 1
#     for i in range(1,var+1):
#         v = a + b
#         a = b
#         b = v
#         print(v)
#
# Fibonacci(20)


# def inArray(var):
#     T = [3, 5, 0, 4]
#     for v in T:
#         if v == var:
#             status = var,' est dans le tableau'
#             print(status)
#     status = var,' n\'est pas dans le tableau'
#     print(status)
# inArray(3)
# inArray(6)

# def returnIndice(var):
#     T = [3, 5, 0, 4, 4, 7]
#     r = []
#     i = 0
#     for v in T:
#         if v == var:
#             r.append(i)
#         i = i + 1
#     print(r)
#
# returnIndice(5)
# returnIndice(4)

# def isPalindrome(mot):
#     t = list(mot)
#     str1 = t[::-1]
#     str1 = ''.join(str1)
#     if mot == str1:
#         print mot," est un palindrome"
#     else:
#         print mot, "n'est pas un palindrome"
#
# isPalindrome('kayak')
# isPalindrome('radar')
# isPalindrome('vittel')

# def returnNbPremier(var):
#     for i in range(2,var-1):
#         if var % i == 0:
#             return False
#     return True
#
# returnNbPremier(100)

# def leplusgrandNombre():
#     max = 0;
#     for i in range(0, 10):
#         chiffre = raw_input("Entrez un chiffre : ")
#         if (int(chiffre) > int(max)):
#             max = int(chiffre)
#     print("Le plus grand chiffre que vous avez entre est " + str(max))
#
# leplusgrandNombre()

