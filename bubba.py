name = "Fred"

def say_name():
    global name
    name = "Bubba"
    print("internal", name)

say_name()
print("external", name)