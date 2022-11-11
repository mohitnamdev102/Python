
try:
    # import aaj
    # a = int(input("Please Enter no 1: "))
    # b = int(input("Please Enter no 2: "))
    # print(a / b)
    s = "Utsav"
    print(s[2])

except ValueError:
    print("Please Take input as Int")

except TypeError:
    print("Wrong Type Given.")

except ZeroDivisionError:
    print("You can not divide by zero.")

except ImportError:
    print("Module not found")

except IndexError:
    print("Value out of Index range")

except Exception as e:
    print("Error:",e)

else:
    print("This is the second part of code")

finally:
    print("Good Bye.")
