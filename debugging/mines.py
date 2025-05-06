#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.moves = 0

    def print_board(self, reveal=False):
        clear_screen()
        print("\n=== MINESWEEPER ===\n")
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()
        print("\nMoves made:", self.moves)

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("Invalid coordinates!")
            return True
        
        if self.revealed[y][x]:
            print("This cell has already been revealed!")
            return True

        if (y * self.width + x) in self.mines:
            self.game_over = True
            return False

        self.revealed[y][x] = True
        self.moves += 1
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False
        return True

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                x = int(input("\nEnter x coordinate (0-{}): ".format(self.width-1)))
                y = int(input("Enter y coordinate (0-{}): ".format(self.height-1)))
                
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\nGame Over! You hit a mine.")
                    break
                
                if self.check_win():
                    self.print_board(reveal=True)
                    print("\nCongratulations! You won!")
                    break
                    
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()