

bd = {
    "a": "2/3/98",
    "b": "5/6/76",
    "c": "12/4/78",
    "d": "3/5/89"
}

def print_title():
    print("Welcome to the birthday dictionary. We know the birthdays of : \n%s" %str("\n".join(bd.keys())))

def print_bd(name):
    print("%s's birthday is %s" %(name, bd[name]))

if __name__ == "__main__":
    print_title()
    who = input("Who's birthday do you want to look up? \n")
    print_bd(who)
    
