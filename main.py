import os
import datetime

class RestaurantSeatManager:
    def __init__(self):
        self.tables = {
            '4': [],
            '8': [],
            '12': [],
            '16': []
        }

    def clear_screen(self):
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux and macOS
            os.system('clear')

    def admin_control(self):
        self.clear_screen()
        print("\nAdmin Control:")
        num_tables = int(input("Enter the number of tables to add: "))

        for _ in range(num_tables):
            table_number = input("Enter table number: ")
            seats = int(input("Enter the number of seats for the table: "))
            category = self.get_category(seats)

            existing_category, index_in_existing_category = self.find_category_and_index_of_existing_table(table_number)

            if existing_category and category != existing_category:
                # Remove the table from the existing category
                removed_table = self.tables[existing_category].pop(index_in_existing_category)
                # Add the table to the new category
                self.tables[category].append(removed_table)
                print(f"Table {table_number} category updated to {category} from category {existing_category}")
            elif existing_category:
                print("Error: Table with the same number and category already exists. Please re-enter.")
                input("Press enter ...")
                self.admin_control()  # Retry input
                return
            else:
                self.tables[category].append(table_number)
                print(f"Table {table_number} with {seats} seats added to category {category}")

        # Print tables in tabular form
        print("\nTable Allocation:")
        print("Category\tTable Numbers")
        print("-----------------------------")
        for category, tables in self.tables.items():
            print(f"{category}\t\t{', '.join(tables)}")

    def get_category(self, seats):
        if seats <= 4:
            return '4'
        elif seats <= 8:
            return '8'
        elif seats <= 12:
            return '12'
        else:
            return '16'

    def find_category_and_index_of_existing_table(self, table_number):
        for category, tables in self.tables.items():
            if table_number in tables:
                index_in_existing_category = tables.index(table_number)
                return category, index_in_existing_category
        return None, None

    def customer_control(self):
        self.clear_screen()
        print("\nCustomer Control:")
        print("1. Walk-in")
        print("2. Reserve")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            num_people = int(input("Enter the number of people: "))
            table_number = self.find_available_table(num_people)
            if table_number.isdigit():
                print(f"Table {table_number} assigned for {num_people} people. Enjoy your meal!")
            else:
                print(table_number)
        elif choice == '2':
            num_people = int(input("Enter the number of people: "))
            date_str = input("Enter the reservation date (YYYY-MM-DD): ")
            time_str = input("Enter the reservation time (HH:MM): ")
            reservation_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            print(f"Reservation confirmed for {num_people} people on {reservation_datetime}")
        else:
            print("Invalid choice. Please enter 1 or 2.")

    def find_available_table(self, num_people):
        for category, tables in self.tables.items():
            if category == '4' and num_people <= 4 and tables:
                return tables.pop(0)
            elif category == '8' and num_people <= 8 and tables:
                return tables.pop(0)
            elif category == '12' and num_people <= 12 and tables:
                return tables.pop(0)
            elif category == '16' and num_people <= 16 and tables:
                return tables.pop(0)
        return "No available table for the specified number of people."

if __name__ == "__main__":
    seat_manager = RestaurantSeatManager()
    print("-"*40)
    print("Restaurant Seat Management System")
    print("-"*40)
    
    while True:
        print("\n1. Admin Control")
        print("2. Customer Control")
        print("3. Exit")
        user_choice = input("Enter your choice (1, 2, or 3): ")

        if user_choice == '1':
            seat_manager.admin_control()
        elif user_choice == '2':
            seat_manager.customer_control()
        elif user_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        back_to_menu = input("Do you want to go back to the main menu? (yes/no): ").lower()
        if back_to_menu != 'yes':
            break
