# Homework 3 - Board Game System
# Name: Emma Barnes
# Date: 04/05/2026

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)


def movePlayer(data):
    """Example function to simulate moving a player."""
    
    if data[0] == "Turn: Player1":
        player1_list = list(data[1])
        if player1_list[1] == ":":
            spot = player1_list[0]
            int_spot = int(spot) + 1
            player1_list[0] = str(int_spot)
            data[1] = "".join(player1_list)
            str_play1 = "".join(player1_list)
        else:
            spot = player1_list[1]
            if spot == "9":
                player1_list[1] = "0"
                spot = player1_list[0]
                int_spot = int(spot) + 1
                player1_list[0] = str(int_spot)
                data[1] = "".join(player1_list)
                str_play1 = "".join(player1_list)
            else:
                int_spot = int(spot) + 1
                player1_list[1] = str(int_spot)
                data[1] = "".join(player1_list)
                str_play1 = "".join(player1_list)

        turn_list = list(data[0])
        turn = turn_list[12]
        turn = 2
        turn_list[12] = str(turn)
        data[0] = "".join(turn_list)
        displayGame(data)

        with open('events.txt', 'r') as file:
            lines = file.readlines()

            lines[0] = "Turn: Player2\n"
            lines[1] = str_play1 + "\n"
            with open('events.txt', 'w') as file:
                file.writelines(lines)
    elif data[0] == "Turn: Player2":
        player2_list = list(data[2])
        if player2_list[1] == ":":
            spot = player2_list[0]
            int_spot = int(spot) + 1
            player2_list[0] = str(int_spot)
            data[1] = "".join(player2_list)
            str_play2 = "".join(player2_list)
        else:
            spot = player2_list[1]
            if spot == "9":
                player2_list[1] = "0"
                spot = player2_list[0]
                int_spot = int(spot) + 1
                player2_list[0] = str(int_spot)
                data[2] = "".join(player2_list)
                str_play2 = "".join(player2_list)
            else:
                int_spot = int(spot) + 1
                player2_list[1] = str(int_spot)
                data[2] = "".join(player2_list)
                str_play2 = "".join(player2_list)

        turn_list = list(data[0])
        turn = turn_list[12]
        turn = 3
        turn_list[12] = str(turn)
        data[0] = "".join(turn_list)
        displayGame(data)

        with open('events.txt', 'r') as file:
            lines = file.readlines()

            lines[0] = "Turn: Player3\n"
            lines[2] = str_play2 + "\n"
            with open('events.txt', 'w') as file:
                file.writelines(lines)

    elif data[0] == "Turn: Player3":
        player3_list = list(data[5])
        if player3_list[1] == ":":
            spot = player3_list[0]
            int_spot = int(spot) + 1
            player3_list[0] = str(int_spot)
            data[1] = "".join(player3_list)
            str_play3 = "".join(player3_list)
        else:
            spot = player3_list[1]
            if spot == "9":
                player3_list[1] = "0"
                spot = player3_list[0]
                int_spot = int(spot) + 1
                player3_list[0] = str(int_spot)
                data[5] = "".join(player3_list)
                str_play3 = "".join(player3_list)
            else:
                int_spot = int(spot) + 1
                player3_list[1] = str(int_spot)
                data[5] = "".join(player3_list)
                str_play3 = "".join(player3_list)

        turn_list = list(data[0])
        turn = turn_list[12]
        turn = (int(turn) + 1) %3
        turn_list[12] = str(turn)
        data[0] = "".join(turn_list)
        displayGame(data)

        with open('events.txt', 'r') as file:
            lines = file.readlines()

            lines[0] = "Turn: Player1\n"
            lines[5] = str_play3 + "\n"
            with open('events.txt', 'w') as file:
                file.writelines(lines)





def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    #print(gameData)
    displayGame(gameData)

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        movePlayer(gameData)
    


if __name__ == "__main__":
    main()
