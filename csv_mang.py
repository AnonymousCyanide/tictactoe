import csv

def convert_to_int(board):
    converted_board = []
    for row in board:
        converted_row = []
        for item in row:
            try:
                converted_row.append(int(item))
            except ValueError:
                converted_row.append(item)  # If conversion fails, keep the original value
        converted_board.append(converted_row)
    return converted_board

def store_data(data):
    # Store the 2D list as a CSV file
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def get_data():
    read_data = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            read_data.append(row)
    board = convert_to_int(read_data)
    return board

def verify_credentials(username, password):
    with open('user.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == str(username) and row['password'] == password:
                return True
        return False
def write_turn(player):
    with open('turn.txt','w') as f:
        f.write(str(player))
def get_turn():
    turn = ''
    with open('turn.txt','r') as f:
        turn = f.read()
    return turn
