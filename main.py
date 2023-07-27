from src.item_names import printValues, items
from src.command import runCommand, clear

item_list = list(items.values())

def main():
    while True:
        string = """
                [1] Add a specific item
                [2] Add all items (900)
                [3] Choose the amount of all items\n
        """

        print(string) 
        choice = int(input("> "))
        if choice == 1:
            printValues()
            input_choice = int(input("\n> "))
            quantity = int(input("\nChoose the quantity: "))
            runCommand(item_list[input_choice], quantity)

        elif choice == 2:
            for i in items:
                runCommand(i, 900)

        elif choice == 3:
            inp_quantity = int(input("Choose the quantity for each item: \n>"))
            for i in items:
                runCommand(i, inp_quantity)
        
        clear()
    

main()