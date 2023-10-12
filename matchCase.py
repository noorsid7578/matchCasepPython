# Match Case

x=2
# x is the variable to match
match x:
    case 0:
        print("x is zero")
    case 1:
        print("case is 1")
    case 2:
        print("case 2")
    case 3:
         print("case 3")
    case 4:
        print("case 4")
    case 5:
        print("case 5")


print("This is match-case statements")



#Another Example

age=int(input("Enter a age:"))

match age:
    case 1:
        print("Case  is Baby")
    case  _ if age<6:
        print("Case  is Child ")
    case  _ if age<18:
        print("Case start adulting")
    case _ if age<45:
        print("Case  is Adult")
    case 45:
        print("Case  is Old")

print("Alwase Executed")



#End Match Case

