cup = {'water': 200, 'milk': 50, 'beans': 15}
water = int(input('Write how many ml of water the coffee machine has:\n'))
milk = int(input('Write how many ml of milk the coffee machine has:\n'))
beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
cups = int(input('Write how many cups of coffee you will need:\n'))
n = 1000000
if milk // cup['milk'] < n:
    n = milk // cup['milk']
if beans // cup['beans'] < n:
    n = beans // cup['beans']
if water // cup['water'] < n:
    n = water // cup['water']

if n == cups:
    print(f'Yes, I can make that amount of coffee')
elif n < cups:
    print(f'No, I can make only {n} cups of coffee')
elif n > cups:
    print(f'Yes, I can make that amount of coffee (and even {n - cups} more than that)')
