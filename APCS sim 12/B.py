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
plate = [3][3]
n, m, q = map(int, input().split())
for _ in range(n):  # recipes input
    temp = list(map(int, input().split()))
    temp[1] = str(temp[1])
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
    plateItems = list()
    recipeItems = list()
    for item in recipe:
        recipeItems.append(item)
    for item in plate:
        plateItems.append(item)
    if any(recipeItems not in plateItems):
        return False
    else:
        if any(recipeItems.name in plateItems.name and recipeItems.count > plateItems.count):
            return False
        else:
            return True


def rotateCompare(recipe, plate):
    pass


def craft(recipe, plate):
    pass


canCraft = False

for action in actions:
    if action[0] == 'put':  # action -> put
        i, p, c = action[1:]
        if items[i].count > c:
            pass
        else:
            plateIndexX = 0
            plateIndexY = 2
            if p in (2, 5, 8):
                if p == 2:
                    plateIndexX = 0
                elif p == 5:
                    plateIndexX = 1
                else:
                    plateIndexX = 2
            else:
                plateIndexY = p // 3
                p %= 3
                plateIndexY = p - 1

            if plate[plateIndexX][plateIndexY].name != items[i].name:
                for item in items:
                    if item.name == plate[plateIndexX][plateIndexY].name:
                        item.count += plate[plateIndexX][plateIndexY]
                        found = True
                        break
            else:
                plate[plateIndexX][plateIndexY] += c
                for item in items:
                    if item.name == plate[plateIndexX][plateIndexY].name:
                        item.count -= c
                        break
    elif action[0] == 'return':  # action -> return

        p = action[1]
        plateIndexX = 0
        plateIndexY = 2
        if p in (2, 5, 8):
            if p == 2:
                plateIndexX = 0
            elif p == 5:
                plateIndexX = 1
            else:
                plateIndexX = 2
        else:
            plateIndexY = p // 3
            p %= 3
            plateIndexY = p - 1

        if not plate[plateIndexX][plateIndexY]:
            pass
        else:
            for item in items:
                if item.name == plate[plateIndexX][plateIndexY].name:
                    item.count += plate[plateIndexX][plateIndexY].count
                    break
    elif action[0] == 'craft':
        for recipe in recipes:
            if recipe.mode == 0 and stricCompare(recipe, plate):
                pass
            elif recipe.mode == 1 and countCompare(recipe, plate):
                pass
            elif recipe.mode == 2 and rotateCompare(recipe, plate):
                pass
    elif action[0] == 'craft_all':
        while canCraft:
            craft()
