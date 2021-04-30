
def current_status():
    print(f'''The coffee machine has: 
{amount_in_machine['water']} of water 
{amount_in_machine['milk']} of milk 
{amount_in_machine['beans']} of coffee beans 
{amount_in_machine['cup']} of disposable cups 
{amount_in_machine['cash']} of money''')


def menu():
    pick = input('Write action (buy, fill, take): ')
    if pick.lower() == 'buy':
        action_buy()
    elif pick.lower() == 'fill':
        action_fill()
    elif pick.lower() == 'take':
        action_take()
    else:
        print('Wrong input.')
        menu()


def action_buy():
    coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
    if coffee == '1':
        amount_in_machine['water'] -= espresso['water']
        amount_in_machine['milk'] -= espresso['milk']
        amount_in_machine['beans'] -= espresso['beans']
        amount_in_machine['cup'] -= espresso['cup']
        amount_in_machine['cash'] += espresso['cash']
    elif coffee == '2':
        amount_in_machine['water'] -= latte['water']
        amount_in_machine['milk'] -= latte['milk']
        amount_in_machine['beans'] -= latte['beans']
        amount_in_machine['cup'] -= latte['cup']
        amount_in_machine['cash'] += latte['cash']
    elif coffee == '3':
        amount_in_machine['water'] -= cappuccino['water']
        amount_in_machine['milk'] -= cappuccino['milk']
        amount_in_machine['beans'] -= cappuccino['beans']
        amount_in_machine['cup'] -= cappuccino['cup']
        amount_in_machine['cash'] += cappuccino['cash']


def action_fill():
    amount_in_machine['water'] += int(input('Write how many ml of water do you want to add: '))
    amount_in_machine['milk'] += int(input('Write how many ml of milk do you want to add: '))
    amount_in_machine['beans'] += int(input('Write how many grams of coffee beans do you want to add: '))
    amount_in_machine['cup'] += int(input('Write how many disposable cups of coffee do you want to add: '))


def action_take():
    print(f"I gave you ${amount_in_machine['cash']}")
    amount_in_machine['cash'] = 0


def main():
    current_status()
    menu()
    current_status()


if __name__ == '__main__':
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cup': 1, 'cash': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'cup': 1, 'cash': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cup': 1, 'cash': 6}
    amount_in_machine = {'water': 400, 'milk': 540, 'beans': 120, 'cup': 9, 'cash': 550}
    main()
