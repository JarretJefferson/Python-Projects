def hello():
    print("This is python")

hello()

def pack(food1, food2, food3):
    snacks = [food1, food2, food3]
    return snacks

food_item1 = "Chips"
food_item2 = "Fruit"
food_item3 = "Yogurt"

result = pack(food_item1, food_item2, food_item3)
print(result)



def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

food_items = ["Sandwich", "Chips", "Fruit", "Yogurt"]
eat_lunch(food_items)







 