#Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program

class Cart():
    #constructor
    def __init__(self):
        self.shop_list = {}
        
    #method to add item
    def add_item(self):
        item_tobe_added = input("What would you like to add? " )
        if item_tobe_added in self.shop_list:
            self.shop_list[item_tobe_added] += 1
        else:
            self.shop_list[item_tobe_added] = 1

    #method to delete item
    def delete_item(self):
        item_tobe_deleted = input("What would you like to delete? ")
        if item_tobe_deleted in self.shop_list:
            del self.shop_list[item_tobe_deleted]
        else:
            print("You don't have that in your list.")

    #method to view list
    def view_list(self):
        for key, value in self.shop_list.items():
            print(value," ",key)

    #method to quit 
    def quit_input(self):
        print("Thanks! See you soon!")
        view_list()   

#Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case 
class ThisString():
    def __init__(self):
        self.thisstring=""
    
    def get_String(self):
        self.thisstring = input("Please enter a string: ")
        
    def print_String(self):
        print(self.thisstring.upper())