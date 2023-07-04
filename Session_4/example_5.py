#1/usr/bin/python



Error= ""
def calc ():
    result = {}
    try:
        age = int(input("please insert your age :"))
    except ZeroDivisionError:
        print(" Value : ZeroDivisionError " )
        result={"error":"ZeroDivisionError"}
    except:
        print("except")
        result={"error":"except"}
        return "except"
    else:
        if age > 18:
            print("Error")
        result = {"error": "None","data":True}
    # finally:
    #     print(result)

    print("final-func")


calc()