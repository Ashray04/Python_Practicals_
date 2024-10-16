import random

def display(grid, size):
    print(" --- " + "--- " * (size - 1))
    for i in range(size):
        for k in range(1, size + 1):
            print("| " + grid[i][k] + " ", end="")
        print("|")
        print(" --- " + "--- " * (size - 1))


def make_grid(size):
    result = []
    for _ in range(size):
        result.append(dict(zip(range(1, size + 1), " " * size)))
    return result


def check_result(grid, size):
    for row in range(size):
        if all(grid[row][col] == grid[row][1] and grid[row][1] != " " for col in range(1, size + 1)):
            return grid[row][1]

    for col in range(1, size + 1):
        if all(grid[row][col] == grid[0][col] and grid[0][col] != " " for row in range(size)):
            return grid[0][col]

    if all(grid[i][i+1] == grid[0][1] and grid[0][1] != " " for i in range(size)):
        return grid[0][1]

    if all(grid[i][size-i] == grid[0][size] and grid[0][size] != " " for i in range(size)):
        return grid[0][size]

    return None


def start(grid, size):
    names = ["", ""]
    names[0] = input("Enter Name Of Player 1: ").upper()
    names[1] = input("Enter Name Of Player 2: ").upper()
    
    player1 = names[0][0]
    player2 = names[1][0]
    
    if player1 == player2:
        names[1] = input("Enter Pet Name Of Player 2: ").upper()
    
    if random.randint(0, 1):
        names[0], names[1] = names[1], names[0]
        player1, player2 = player2, player1
    
    previous = player2
    chance = 0
    
    while chance < size * size:
        current_player = player1 if previous == player2 else player2
        previous = current_player
        
        while True:
            try:
                input_tuple = tuple(map(int, input(f"{current_player}, enter two integers (row col): ").split()))
                if (1 <= input_tuple[0] <= size and 1 <= input_tuple[1] <= size) and grid[input_tuple[0] - 1][input_tuple[1]] == " ":
                    grid[input_tuple[0] - 1][input_tuple[1]] = current_player
                    break
                else:
                    print("Invalid input or position already taken. Try again.")
            except (ValueError, IndexError):
                print("Please enter valid integers within the grid range.")
        
        display(grid, size)
        winner = check_result(grid, size)
        if winner :
            if winner == player1 :
                winner = names[0]
            else :
                winner = names[1]
        if winner:
            print(f"{winner} wins the game!")
            return
        chance += 1
    
    print("It's a draw!")


def initialise():
    size = int(input("Size = "))
    grid = make_grid(size)
    display(grid, size)
    return grid, size


specs = initialise()
start(specs[0], specs[1])

    
