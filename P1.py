import random
MAX_LINES = 3
MAX_BET = 2500
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines + 1)
    
    return winnings , winnings_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        
        print()

def deposit():
    amount = input("How much would you like to deposit? Rs/-")
    while True:
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Enter a number: ")
    return amount

def get_number_of_lines():
    lines = input("How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? ")
    while True:
        if lines.isdigit():
            lines = int(lines)
            if  1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the vaild number of lines.")
        else:
            print("Enter a number: ")
    return lines

def get_bet():
    bet = input("What would you like to bet on each line? Rs/-")
    while True:
        if bet.isdigit():
            bet = int(bet)
            if  MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter Amount between Rs/-{MIN_BET} - Rs/-{MAX_BET}")
        else:
            print("Enter a number: ")
    return bet

def spin(balance):
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = lines * bet
            if total_bet > balance:
                print(f"You do not have enough Amount to bet,your current balance is Rs/-{balance}")
            else:
                break
        
        print(f"You are betting Rs/-{bet} on {lines}.Total bet is equal to Rs/-{total_bet}")
        slots = get_slot_machine_spin(ROWS,COLS,symbols_count)
        print_slot_machine(slots)
        winnings,winnings_lines = check_winnings(slots, lines, bet,symbols_value)
        print(f"You won Rs/-{winnings}.")
        print(f"You won on lines:",*winnings_lines)
        return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is Rs/-{balance}")
        answer = input("Press Enter to Play or (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with Rs\-{balance}.")


    

main()

    

    