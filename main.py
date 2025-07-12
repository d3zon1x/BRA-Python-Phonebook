phonebook = {}

def add_entry():
    print("Add new entry - stub")

def search_by_first_name():
    print("Search by first name - stub")

def search_by_last_name():
    print("Search by last name - stub")

def search_by_full_name():
    print("Search by full name - stub")

def search_by_phone_number():
    a = input('Уведіть номер телефону для пошуку: ')
    result = []
    for i in phonebook.values():
        print(i)

def search_by_city_or_state():
    print("Search by city or state - stub")

def delete_by_phone_number():
    print("Delete a record by telephone number - stub")

def update_by_phone_number():
    print("Update a record by telephone number - stub")

def exit_program():
    print("Exiting program.")
    exit()

def application_loop():
    while True:
        print("""\nPhonebook Menu:
1) Add new entries 
2) Search by first name 
3) Search by last name 
4) Search by full name
5) Search by telephone number
6) Search by city or state
7) Delete a record for a given telephone number
8) Update a record for a given telephone number
9) Exit the program""")
        try:
            choice = int(input('Your choice: '))
        except ValueError:
            print("Please enter a valid number from 1 to 9.")
            continue

        match choice:
            case 1:
                add_entry()
            case 2:
                search_by_first_name()
            case 3:
                search_by_last_name()
            case 4:
                search_by_full_name()
            case 5:
                search_by_phone_number()
            case 6:
                search_by_city_or_state()
            case 7:
                delete_by_phone_number()
            case 8:
                update_by_phone_number()
            case 9:
                exit_program()
            case _:
                print("Invalid choice. Please select a number from 1 to 9.")

def main():
    application_loop()

main()
search_by_phone_number()