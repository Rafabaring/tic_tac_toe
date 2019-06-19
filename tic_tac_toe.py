import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" "
                     ," ", " ", " "
                     ," ", " ", " "
                     ," ", " ", " "]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("---","---","---")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("---","---","---")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    # def update_cell(self, cell_no, player):
    #     self.cells[cell_no] = player

    def check_move(self, cell_no, player):
        while self.cells[cell_no] != " ":
            print('try another cell')
            cell_no = int(input("Taken position, try another one --> "))

        self.cells[cell_no] = player


    def complete_game(self):
        final_result = []
        for i in self.cells[1:]:
            if i != " ":
                final_result.append(i)

        if len(final_result) == 9:
            print("DRAW")


    def check_score(self, player):
        # check horizontal winning
        for i in [1, 4, 7]:
            if self.cells[i] == player:
                if self.cells[i + 1] == player:
                    if self.cells[i + 2] == player:
                        return True


        # vertical winning
        for i in [1, 2, 3]:
            if self.cells[i] == player:
                if self.cells[i + 3] == player:
                    if self.cells[i + 6] == player:
                        return True


        # Diagonal winning top left - bottom right
        if self.cells[1] == player:
            if self.cells[5] == player:
                if self.cells[9] == player:
                    return True

        # Diagonal winning top right - bottom left
        if self.cells[3] == player:
            if self.cells[5] == player:
                if self.cells[7] == player:
                    return True



# Criando o objeto
board = Board()


def refresh_screen():
    os.system("clear")
    print("Hello, play tic tac toe \n")

    board.display()

    print("")


# While loop pro jogo se repetir
while True:
    refresh_screen()
    board.complete_game()

    # Get X input
    x_choice = int(input("x input value --> "))
    board.check_move(x_choice, 'X')

    end_game = board.check_score('X')
    if end_game == True:
        refresh_screen()
        print("Congratulations, X wins")
        break



    refresh_screen()
    board.complete_game()


    # Get O input
    o_choice = int(input("o input value --> "))
    board.check_move(o_choice, 'O')

    end_game = board.check_score('O')
    if end_game == True:
        refresh_screen()
        print("Congratulations, O wins")
        break
