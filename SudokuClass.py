# Algorithms and Data Structures - First Programming Project
# Núria Mitjavila & Marta Ortigas - Sudoku 9x9, Backtracking
# 25 february 2023
import random

# Start the class to solve the Sudoku using backtracking
class SudokuSolver:

    # Start the function that will print the input
    def printInput(self, table):
        print()
        print("This is the given Sudoku:")
        print("-------------------------")
        count = 0
        for x in table:
            if count == 3:
                print("--------+-------+--------")
                count = 0
            count += 1
            for y in range(0, 9):
                if y == 0 or y == 3 or y == 6:
                    print("|", end=" ")
                if x[y] == '.':
                    print("□", end=" ")
                else:
                    print(x[y], end=" ")
            print("|", end=" ")
            print()
        print("-------------------------")

    # Start the function that will check if the value is valid through the row
    def rowCheck(self, table, row, value):
        for x in range(0, 9):
            if value == table[row][x]:
                return False
        return True

    # Start the function that will check if the value is valid through the column
    def columnCheck(self, table, column, value):
        for x in range(0, 9):
            if value == table[x][column]:
                return False
        return True

    # Start the function that will check if the value is valid through the square
    def squareCheck(self, table, row, column, value):
        row = (row // 3) * 3 + 1
        column = (column // 3) * 3 + 1
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if table[row + x][column + y] == value:
                    return False
        return True

    # Start the function that will chech if there is or not a value in the table
    def point(self, table):
        for x in range(0, 9):
            for y in range(0, 9):
                if table[x][y] == ".":
                    return x, y
        return -1, -1

    # Start the function that will solve the Sudoku, checking the previous functions
    def solution(self, table):
        x, y = self.point(table)
        if x == -1 and y == -1:
            return True
        for number in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.rowCheck(table, x, number) and self.columnCheck(table, y, number) and self.squareCheck(table, x, y, number):
                table[x][y] = number
                if self.solution(table):
                    return True
                table[x][y] = "."
        return False

    # Start the function that will print the solution
    def printTable(self, table):
        print()
        print("This is the solution:")
        print("-------------------------")
        count = 0
        for x in table:
            if count == 3:
                print("--------+-------+--------")
                count = 0
            count += 1
            for y in range(0, 9):
                if y == 0 or y == 3 or y == 6:
                    print("|", end=" ")
                print(x[y], end=" ")
            print("|", end=" ")
            print()
        print("-------------------------")
        return ''



# Start the class to create a Sudoku
class SudokuCreator:

    # Create a function to generate the base pattern
    def generate(self, row, column):
        return (3 * (row % 3) + row // 3 + column) % 9

    # Create a function to shuffle the list
    def random(self, llista):
        return random.sample(llista, len(llista))

    # Create a sudoku with easy difficulty
    def create_board(self, difficulty):
        row = []
        for x in self.random(range(3)):
            for y in self.random(range(3)):
                row.append(x * 3 + y)
        column = []
        for x in self.random(range(3)):
            for y in self.random(range(3)):
                column.append(x * 3 + y)
        number = self.random(range(1, 10))
        table = []
        for r in row:
            row_list = []
            for c in column:
                row_list.append(number[self.generate(r, c)])
            table.append(row_list)
        squares = 9 * 9
        if difficulty == 'easy':
            empty = squares * 1 // 4
        elif difficulty == 'medium':
            empty = squares * 2 // 4
        else:
            empty = squares * 3 // 4
        for x in random.sample(range(squares), empty):
            table[x // 9][x % 9] = '.'
        return table


def main():
    # Ask the user to input the sudoku
    print("Choose if you want the program to create a sudoku or you want to solve one")
    print("Write 1 to create a sudoku")
    print("Write 2 to solve a sudoku")
    option = input()
    sol = SudokuSolver()

    # Create a sudoku if the user wants
    if option == '1':
        sudoku = SudokuCreator()
        print("Please, input a level of difficulty (easy, medium, hard):")
        level = input()

        # Create a sudoku depending on the level of difficulty
        if level == 'easy':
            board = sudoku.create_board('easy')
            sol.printInput(board)
        elif level == 'medium':
            board = sudoku.create_board('medium')
            sol.printInput(board)
        elif level == 'hard':
            board = sudoku.create_board('hard')
            sol.printInput(board)
        else:
            print("Please, choose a valid level of difficulty")

    # Solve a sudoku if the user wants
    elif option == '2':
        # Create a blank table as a list
        table = []
        print("Please, input the sudoku (use a dot for the blanck spaces):")
        for x in range(0, 9):
            table.append(list(input()))
        sol.printInput(table)

        # Check if there is a solution and print it
        if sol.solution(table):
            print(sol.printTable(table))
        else:
            print()
            print("There is no solution for this Sudoku!")


    # If the user doesn't choose a valid option
    else:
        print("Please, choose a valid option")
        main()


if __name__ == '__main__':
    main()
