from zero import ZeroServer
from csv_mang import get_data , store_data , verify_credentials , get_turn ,write_turn
app = ZeroServer(port=5559)


current_player = 1

@app.register_rpc
def check_for_winner() ->str:
    winner = None
    board = get_data()
    print(board)

    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            winner = row[0]
            break

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            winner = board[0][col]
            break

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]

    if all([all(row) for row in board]) and winner is None:
        winner = "tie"
   # print(winner)
    if winner:
        return winner

@app.register_rpc
def make_board(cords : tuple) ->list:
    board = get_data()
    print(cords)
    turn = str(get_turn())
    print(turn)
    print( turn==str(cords[2]))
    if verify_credentials(cords[2],cords[3]) and turn==str(cords[2]) :
        
        current_player = turn
    else :
        return None

    if board[cords[0]][cords[1]] == 0:
        if current_player == '1':
            board[cords[0]][cords[1]] = "X"
            write_turn(2)
            
        else:
            board[cords[0]][cords[1]] = "O"
            write_turn(1)
           
    else :
        return None
    print(board)
    store_data(board)
    return board

        

if __name__ == "__main__":
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    store_data(board)
    app.run()