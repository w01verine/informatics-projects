sales = { "apples": 0, "lemonade": 0 }
sales["apples"] = sales["apples"] + 1
del sales["lemonade"]
print(len(sales["apples"]))
