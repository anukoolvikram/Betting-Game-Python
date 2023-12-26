**Slot Machine Game/Betting Game**

_Overview_

This is a simple text-based slot machine game implemented in Python. 
Players can deposit money, choose the number of lines to bet on, and spin the slot machine to try their luck. 
The game features a basic balance system, input validation, and winnings calculation based on matching symbols on the slot machine lines.

**How to Play**

_Deposit Money:_

Run the script, and you will be prompted to enter the deposit amount. This is the initial amount of money the player has to start the game.

_Number of Lines:_

Enter the number of lines you want to bet on. The game supports a customizable number of lines, with a default maximum of 3.

_Place a Bet:_

Enter the amount you want to bet per line. The minimum and maximum bet amounts are configurable (default: 1 to 100).

_Spin the Slot Machine:_

Press Enter to spin the slot machine. The machine will randomly generate symbols for each column and display the result.

_Winnings:_

The game calculates winnings based on the symbols matched on the chosen lines. Winnings are displayed, and the total is adjusted accordingly.

_Quit the Game:_

To quit the game, press 'q' when prompted to spin.

**Configuration**

The game allows customization of certain parameters:
Maximum lines to bet on (MAX_LINES)
Maximum and minimum bet amounts (MAX_BET, MIN_BET)
Number of rows and columns on the slot machine (ROWS, COLS)
Symbol count and value for winnings (symbol_count, symbol_value)

**Running the Game**

Ensure you have Python installed on your system.
Run the script using the command: python slot_machine.py

_Additional Notes_
The game includes basic input validation to ensure that the user inputs valid values for deposit, lines, and bet amounts.
The balance is updated after each spin, and the game continues until the player decides to quit.
