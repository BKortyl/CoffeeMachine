
def current_status():
    print(f'''The coffee machine has: 
{amount_in_machine['water']} of water 
{amount_in_machine['milk']} of milk 
{amount_in_machine['beans']} of coffee beans 
{amount_in_machine['cup']} of disposable cups 
{amount_in_machine['cash']} of money''')


def menu():
    while True:
        pick = input('Write action (buy, fill, take, remaining, exit): ')
        if pick.lower() == 'buy':
            action_buy()
        elif pick.lower() == 'fill':
            action_fill()
        elif pick.lower() == 'take':
            action_take()
        elif pick.lower() == 'remaining':
            current_status()
        elif pick.lower() == 'exit':
            quit()
        else:
            print('Wrong input.')
            menu()


def compare_amount(machine, coffee):
    lacking = []
    for keys in machine:
        if machine[keys] <= coffee[keys]:
            lacking.append(keys)
    if not bool(lacking):
        return True
    else:
        print(f'Sorry, not enough {lacking[0]}!')
        menu()


def action_buy():
    coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if coffee == '1':
        if compare_amount(amount_in_machine, espresso):
            print('I have enough resources, making you a coffee!')
        amount_in_machine['water'] -= espresso['water']
        amount_in_machine['milk'] -= espresso['milk']
        amount_in_machine['beans'] -= espresso['beans']
        amount_in_machine['cup'] -= espresso['cup']
        amount_in_machine['cash'] += espresso['cash']
    elif coffee == '2':
        if compare_amount(amount_in_machine, latte):
            print('I have enough resources, making you a coffee!')
        amount_in_machine['water'] -= latte['water']
        amount_in_machine['milk'] -= latte['milk']
        amount_in_machine['beans'] -= latte['beans']
        amount_in_machine['cup'] -= latte['cup']
        amount_in_machine['cash'] += latte['cash']
    elif coffee == '3':
        if compare_amount(amount_in_machine, cappuccino):
            print('I have enough resources, making you a coffee!')
        amount_in_machine['water'] -= cappuccino['water']
        amount_in_machine['milk'] -= cappuccino['milk']
        amount_in_machine['beans'] -= cappuccino['beans']
        amount_in_machine['cup'] -= cappuccino['cup']
        amount_in_machine['cash'] += cappuccino['cash']
    elif coffee == 'back':
        menu()
    else:
        print('Wrong input')
        action_buy()


def action_fill():
    amount_in_machine['water'] += int(input('Write how many ml of water do you want to add: '))
    amount_in_machine['milk'] += int(input('Write how many ml of milk do you want to add: '))
    amount_in_machine['beans'] += int(input('Write how many grams of coffee beans do you want to add: '))
    amount_in_machine['cup'] += int(input('Write how many disposable cups of coffee do you want to add: '))


def action_take():
    print(f"I gave you ${amount_in_machine['cash']}")
    amount_in_machine['cash'] = 0


def main():
    menu()


if __name__ == '__main__':
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cup': 1, 'cash': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'cup': 1, 'cash': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cup': 1, 'cash': 6}
    amount_in_machine = {'water': 400, 'milk': 540, 'beans': 120, 'cup': 9, 'cash': 550}
    main()
