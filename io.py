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

def returnIndice(var):
    T = [3, 5, 0, 4, 4, 7]
    r = []
    i = 0
    for v in T:
        if v == var:
            r.append(i)
        i = i + 1
    print(r)

returnIndice(5)
returnIndice(4)