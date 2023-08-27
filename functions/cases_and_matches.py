def age(age: int):
    match age:
        case 0:
            return "Fish"
        case 1:
            return "Dog"
        case 2:
            return "Doctor Suess"
        case default:
            return "Something ngl"


base = age(age=2)
print(base)
