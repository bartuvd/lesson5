
def personal_wallet():
    wallet = 0
    histori = []

    while True:
        print(f'На вашем счете; {wallet} рублей')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            wallet_fill = int(input('Введите сумму: '))
            wallet += wallet_fill
        elif choice == '2':
            amount_buy = int(input('Введите сумму покупки: '))
            if amount_buy <= wallet:
                name_buy = input('Введите название покупки: ')
                wallet -= amount_buy
                histori.append({name_buy, amount_buy})
            else:
                print('Денег не хватает\n')
        elif choice == '3':
            print(histori)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
