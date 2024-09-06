class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self):
        item_id = input("Enter item ID: ")
        if item_id in self.items:
            print(f"Item with ID {item_id} already exists.")
            return
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity in kgs: "))
        price_per_kg = float(input("Enter price per kg: "))
        self.items[item_id] = {
            'name': name,
            'quantity': quantity,
            'price_per_kg': price_per_kg
        }
        print(f"Item {name} added successfully.")

    def update_item(self):
        item_id = input("Enter item ID to update: ")
        if item_id not in self.items:
            print(f"Item with ID {item_id} not found.")
            return
        quantity = int(input("Enter new quantity in kgs: "))
        price_per_kg = int(input("Enter new price per kg: "))
        self.items[item_id]['quantity'] = quantity
        self.items[item_id]['price_per_kg'] = price_per_kg
        print(f"Item ID {item_id} updated successfully.")

    def remove_item(self):
        item_id = input("Enter item ID to remove: ")
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item ID {item_id} removed successfully.")
        else:
            print(f"Item with ID {item_id} not found.")

    def search_item(self):
        search_term = input("Enter item name or ID to search: ")
        found_items = [item for item_id, item in self.items.items()
                       if search_term in (item['name'], str(item_id))]
        if found_items:
            for item in found_items:
                print(f"Found item: {item}")
        else:
            print(f"No items found with ID '{search_term}'.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item_id, item in self.items.items():
                print(f"ID: {item_id}, Name: {item['name']}, "
                      f"Quantity: {item['quantity']}, Price per Unit: ${item['price_per_unit']}")

    def calculate_inventory_value(self):
        total_value = sum(item['quantity'] * item['price_per_kg'] for item in self.items.values())
        print(f"Total inventory value: Rs{total_value}")


if __name__ == '__main__':
    inventory = Inventory()

    while True:
        print("\nChoose an action: add, update, remove, search, view, value, exit")
        action = input("Enter action: ").lower()

        if action == 'add':
            inventory.add_item()
        elif action == 'update':
            inventory.update_item()
        elif action == 'remove':
            inventory.remove_item()
        elif action == 'search':
            inventory.search_item()
        elif action == 'view':
            inventory.view_inventory()
        elif action == 'value':
            inventory.calculate_inventory_value()
        elif action == 'exit':
            print("Exiting the inventory system.")
            break
        else:
            print("Invalid action. Please try again.")
