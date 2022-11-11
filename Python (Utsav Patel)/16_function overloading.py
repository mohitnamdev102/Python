def one(*args):

    if type(args[0]) == str:
        total = ""
    elif type(args[0]) == int:
        total = 0

    for x in args:
        total = total+x

    print(total)

one(1,2,3,4,5)
one("Utsav ", "Patel")