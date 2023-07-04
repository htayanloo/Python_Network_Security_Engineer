#1/usr/bin/python

#
# fir_arg = input("first_arg")
# sec_arg = input("second_arg")
#
#
# print(fir_arg+sec_arg)
#
#
#
# thir_arg = input("thir_arg")
# four_arg = input("four_arg")
#
# print(thir_arg+four_arg)


def over_18(age):
    result = False
    if age>18:
        print("wellcome")
        result = True
    else:
        print("access deny")
        result = False

    return result
def under_18():
    print("http://kids.filimo.com")


input_age = int(input("please inter your age : "))
result = over_18(age=input_age)

if not result:
    under_18()




