import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cell = tk.Entry(self.master, width=4, font=('Arial', 16))
                cell.grid(row=i, column=j)
                self.cells[i][j] = cell

        solve_button = tk.Button(self.master, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4, pady=10)

    def solve_sudoku(self):
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                if value.isdigit():
                    self.board[i][j] = int(value)
                else:
                    self.board[i][j] = 0

        if self.solve():
            self.update_gui()
        else:
            messagebox.showerror("Error", "Oops! No solution found.")

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0

        return False

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid_move(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def update_gui(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(self.board[i][j]))

def main():
    root = tk.Tk()
    solver = SudokuSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
