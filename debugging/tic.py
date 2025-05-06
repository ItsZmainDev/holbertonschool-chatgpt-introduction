def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input("Entrez la ligne (0, 1, ou 2) pour le joueur " + player + ": "))
            col = int(input("Entrez la colonne (0, 1, ou 2) pour le joueur " + player + ": "))
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Position invalide ! Les coordonnées doivent être entre 0 et 2.")
                continue
                
            if board[row][col] != " ":
                print("Cette case est déjà occupée ! Essayez une autre position.")
                continue
                
            board[row][col] = player
            
            winner = check_winner(board)
            if winner:
                print_board(board)
                print("Le joueur " + winner + " a gagné !")
                break
                
            if is_board_full(board):
                print_board(board)
                print("Match nul !")
                break
                
            player = "O" if player == "X" else "X"
            
        except ValueError:
            print("Entrée invalide ! Veuillez entrer un nombre entre 0 et 2.")

if __name__ == "__main__":
    tic_tac_toe()
