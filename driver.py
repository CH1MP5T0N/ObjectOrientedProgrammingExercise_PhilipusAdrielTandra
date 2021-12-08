import OOP
#Main input Loop
def list_PAT():
    shopping_list = []
    number = eval(input("How many items will you order today?"))
    if number < 1:
        print("Number of items must be at least 1.")
    else:
        item = 1
        while number != 0:
            print("Item #", item)
            item += 1
            name = input("Enter food: ")
            amount = eval(input("Enter amount of pounds: "))
            if amount < 1:
                print("Amount of pounds must be greater than 0")
            object = OOP.List_PAT(name, amount)
            shopping_list.append(object)
            number -= 1

        return shopping_list
#Display function that relates to the OOP.py file
def display_PAT(shopping_list):
    for i in shopping_list:
        i.getprivate()
        print("Item: ", i.getfood_PAT())
        print("Amount Ordered:", i.getamount_PAT(), "pounds")
        print("Price per pound: $", i.getpriceperpound_PAT())
        print("Price of order: $", i.calculation_PAT())
    print("\nTotal cost: $",calculate_PAT(shopping_list))
#Calculate the total cost and returns it
def calculate_PAT(shopping_list):
    pop = 0
    for i in shopping_list:
        pop += i.calculation_PAT()
    return pop
#BIG MAIN FUNCTION!!!
def main_PAT():
    large = list_PAT()
    display_PAT(large)


main_PAT()



