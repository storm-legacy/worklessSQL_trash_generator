with open("dependencies/countries.txt", 'r', encoding='UTF-8') as f: #opens a file as f
    countries = [country.strip('\n') for country in f] #then saves to array every line of file as seperate element
with open("dependencies/nationalities.txt", 'r', encoding='UTF-8') as f:
    nationalities = [nationality.rstrip('\n') for nationality in f]
with open("dependencies/names.txt", 'r', encoding='UTF-8') as f:
    names = [name.strip('\n') for name in f]
with open("dependencies/surnames.txt", 'r', encoding='UTF-8') as f:
    surnames = [surname.strip('\n') for surname in f]
with open("dependencies/cities.txt", 'r', encoding='UTF-8') as f:
    cities = [city.strip('\n') for city in f]
with open("dependencies/domains.txt", 'r', encoding='UTF-8') as f:
    domains = [domain.strip('\n') for domain in f]

#Just arrays with elements, feel free to make your own
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
currencies = ["PLN", "USD", "YEN", "CAD", "EUR"]
products_names = ["Milk", "Coffee", "Eggs","Butter", "Juice", "Wine", "Chocolate", "Bread", "Roll", "Cheese", "Ham", "Scissors", "Knife", "Board", "Wooden Board"]
