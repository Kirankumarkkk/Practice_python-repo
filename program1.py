variable1=True
variable2=True
variable3=True
testvariable1=""


if variable1 and variable2:
    print("variable1 and variable2")
    testvariable1="abcd"
    print(testvariable1)
else:
    print("false")
    testvariable1 = "efgh"
    print(testvariable1)

if testvariable1=="abcd":
    print("it's true working")
elif testvariable1=="efgh":
    print("it's false working")