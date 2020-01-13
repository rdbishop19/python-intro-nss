### COLLECTIONS ###

### list --------------
junk = ["Frank", False, [2,3,4], 234]
# print(junk)

junk.append("uh-oh")
junk.insert(3, "noice")
# print(junk)
junk.extend(["Mary", "Joseph", "Bob"])
# print(junk)

# JS
# junk.join(" ")

# py
names = ["Frank", "Bildo", "Divad"]
# print(", ".join(names))

#### dictionaries - --------------
my_pairs = {
    911: "help",
    "name": "Throckmorton"
}

# print(my_pairs["name"])
my_pairs["last"] = "Brinkmeyer"
my_pairs["address"] = {"number": 123, "street": "Bourbon St."}

street_name = my_pairs["address"]["street"]

# print(my_pairs.keys())
# print(my_pairs.values())
# print(my_pairs.items())


### sets -----------------------
my_stuff = {"Fred", "Drew", "Drew"}
# print(my_stuff)
# print(list(set(my_stuff))) # why not

my_set = {1, 2, 3}
my_set.add("Feed me")
# print(my_set)

### tuple ----------------------
my_tup = (1, 2, 3, 3, 'hello')
# print(my_tup)

### loops ----------------------
for foo in my_pairs.values():
    print(f'Why I still have {foo} in this drawer?')

### loops - END -----------------------