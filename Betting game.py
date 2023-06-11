import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value={"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(columns, lines, bet, values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for col in columns:
            symbol_to_check=col[line]
            if symbol != symbol_to_check:
                break

        else:  # executes when break is not run
            winnings += values[symbol]*bet
            winning_lines.append(line+1)

    return winnings, winning_lines


def get_spin(rows, cols, symbols):
    all_symbols=[]
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count): # underscore can be used in the place of a variable which is not used later
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        cur_symbol=all_symbols[:]  # making copy of all symbols in the curr symbol
        for _ in range (rows):
            value=random.choice(all_symbols)
            cur_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i!= len(columns)-1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()


def deposit():    # to collect users input money
    while True:   # to continue to take input unless we get valid input amount
        amount=input("Enter the deposit money: ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid number.")

    return amount


def number_lines():
    while True:
        lines=input("Enter the no of lines (1- " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break;
            else:
                print("Enter a valid no of lines:")
        else:
            print("Enter a no.")

    return lines


def get_bet():
    while True:
        amount=input("Enter the bet: ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}- {MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return amount


def game(balance):
    lines = number_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if total > balance:
            print("You do not have enough balance.")
        else:
            break

    print(f"You are betting Rs{bet} on {lines} lines. \n")
    print(f"Your Total bet is: {total}")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Your total winnings are: {winnings}")
    print(f"You won on lines: ", *winning_lines)
    return winnings-total


def main():
    balance=deposit()
    while True:
        print(f"Current Balance is {balance}")
        spin=input("Press Enter to spin (q to quit)")
        if spin== "q":
            break
        balance+= game(balance)

    print(f"You left with: {balance}")


main()