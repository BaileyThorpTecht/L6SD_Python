items = ["smartphone", "laptop", "tablet", "smartphone case", "laptop charger", "tablet cover"]

def Count(lis):
    i = len(lis)
    return i

print(Count(items))





office_supplies = ("pens", "paper", "rulers")

print(office_supplies[2])

try:
    office_supplies.index("sticky notes")
except:
    print("sticky notes are not present")
else:
    print("sticky notes are present")



