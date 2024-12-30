class Recipe():
    def __init__(self, mode: int, product: str, num: int, plate: list):
        self.mode = mode
        self.product = product
        self.num = num
        self.plate = plate


class Item():
    def __init__(self, name, count):
        self.name = name
        self.count = count


recipes = list()
items = list()
table = [3][3]

n, m, q = map(int, input().split())
for _ in range(n):  # recipes input
    temp = list(map(int, input().split()))
    temp_list = list()
    for _ in range(3):
        temp_list.append(list(map(int, input().split())))
    temp.append(temp_list())
    recipes.append(Recipe(temp[0], temp[1], temp[2], temp[3]))
item_input = list(input().split())
for i in range(0, m, 2):  # items input
    items.append(Item(item_input[i], item_input[i+1]))
actions = list()
for _ in range(q):  # actions input
    actions.append(list(input().split()))


def stricCompare(recipe, plate):
    pass


def countCompare(recipe, plate):
    pass


def rotateCompare(recipe, plate):
    pass
