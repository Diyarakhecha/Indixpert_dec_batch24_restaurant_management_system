import json
import os

class menu:
    def init(self, filepath):
        self.file_path = filepath
        self.menu_items = self._fetch_menu_data()

    def _fetch_menu_data(self):
        if os.path.isfile(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Warning: JSON data corrupted in menu file.")
                return {"Breakfast": [], "Lunch": [], "Dinner": []}
        else:
            print("Error: Menu data file does not exist.")
            return {"Breakfast": [], "Lunch": [], "Dinner": []}

    def display_full_menu(self):
        print("\n**** COMPLETE MENU LISTING ****")
        for category, dishes in self.menu_items.items():
            print(f"\n-- {category} Options --")
            if len(dishes) == 0:
                print("   Currently no items available.")
            else:
                print(f"{'Item ID':<12} {'Dish Name':<25} {'Portion':<10} {'Cost (₹)':<8}")
                print("=" * 55)
                for dish in dishes:
                    print(f"{dish['item_id']:<12} {dish['item_name']:<25} {dish['size']:<10} ₹{dish['price']:<8.2f}")

    def find_dish_by_name(self, dish_name):
        search_key = dish_name.casefold()
        for menu_list in self.menu_items.values():
            for dish in menu_list:
                if dish['item_name'].casefold() == search_key:
                    return dish
        return None

