# file = open("D:\\npkey.txt", "r")
# a = []
# for x in file:
#     a.append(x.rstrip("\n"))
#
# print(a)


# file = open('D:\\thandi.txt', 'w')
#
# n = int(input("Please Enter Lines to add: "))
# for x in range(1, n+1):
#     s = "This is my new line "+str(x)+".\n"
#     file.writelines(s)
# file.close()

# file = open('D:\\thandi.txt', 'a')

# n = int(input("Please Enter Lines to add: "))
# for x in range(1, n+1):
#     s = "This is my new line "+str(x)+".\n"
#     file.writelines(s)
# file.close()


'''
r
r+
rb
rb+

w
w+
wb
wb+

a
a+
ab
ab+

'''


a = [1, 2, 3, 4, 5]


def double(x):
    return x*2
a = list(map(double,a))

print(a)





