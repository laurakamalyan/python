import random
import os
import time


class game_xo:

    def __init__(self):
        self.winner = ""
        self.circle_count = 0
        self.count = 9  # count of empty fields

        self.list2 = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
        ]
        self.length = len(self.list2)

        self.gamer = 1

    def show(self):
        for i in range(self.length):
            for j in range(self.length):
                print(self.list2[i][j], end=" ")
            print()

    def xo(self):
        while self.circle_count != 10:
            # win by row
            for i in range(self.length):
                if self.list2[i][0] == self.list2[i][1] == self.list2[i][2] == "X" or self.list2[i][0] == self.list2[i][1] == self.list2[i][2] == "O":
                    self.winner = str(self.list2[i][0])
                    break

            # win by column
            for i in range(self.length):
                if self.list2[0][i] == self.list2[1][i] == self.list2[2][i] == "X" or self.list2[0][i] == self.list2[1][i] == self.list2[2][i] == "O":
                    self.winner = str(self.list2[0][i])
                    break

            # win by main diagonal
            if self.list2[0][0] == self.list2[1][1] == self.list2[2][2] == "X" or self.list2[0][0] == self.list2[1][1] == self.list2[2][2] == "O":
                self.winner = str(self.list2[0][0])

            # win by auxiliary diagonal
            elif self.list2[0][2] == self.list2[1][1] == self.list2[2][0] == "X" or self.list2[0][2] == self.list2[1][1] == self.list2[2][0] == "O":
                self.winner = str(self.list2[0][2])

            # if there is a winner stop the game
            if self.winner != "":
                break

            # if all fields are filled stop the game
            if self.count == 0:
                break

            # fill the fields
            if self.gamer == 1:  # x gamer
                x1 = int(input("Input 0, 1 or 2: "))  # random.randint(0, length - 1)
                x2 = int(input("Input 0, 1 or 2: "))  # random.randint(0, length - 1)
                # stop the game if out of range
                if x1 not in [0, 1, 2] or x2 not in [0, 1, 2]:
                    print("Error. Input only 0, 1 or 2")
                    break

                if self.list2[x1][x2] != "*":
                    # input again if field already filled
                    while self.list2[x1][x2] != "*":
                        x1 = int(input("Input again. 0, 1 or 2: "))  # random.randint(0, length - 1)
                        x2 = int(input("Input again. 0, 1 or 2: "))  # random.randint(0, length - 1)
                        if x1 not in [0, 1, 2] or x2 not in [0, 1, 2]:
                            print("Error. Input only 0, 1 or 2")
                            break
                    self.list2[x1][x2] = "X"
                    self.count -= 1

                else:
                    self.list2[x1][x2] = "X"
                    self.count -= 1
                print("gamer 1: ", x1, x2)
                self.gamer = 0  # change the gamer
            else:  # o gamer
                o1 = random.randint(0, len(self.list2) - 1)
                o2 = random.randint(0, len(self.list2) - 1)

                if self.list2[o1][o2] != "*":
                    # input again if field already filled
                    while self.list2[o1][o2] != "*":
                        o1 = random.randint(0, len(self.list2) - 1)
                        o2 = random.randint(0, len(self.list2) - 1)
                    self.list2[o1][o2] = "O"
                    self.count -= 1

                else:
                    self.list2[o1][o2] = "O"
                    self.count -= 1
                print("gamer 2: ", o1, o2)
                self.gamer = 1  # change the gamer

            self.circle_count += 1

            time.sleep(2)
            os.system("cls")
            self.show()
            print()

        return self.winner


gamer = game_xo()
winner = gamer.xo()

if winner == "":
    print("Dead heat.")
elif winner == "X":
    print("Win gamer 1.")
else:
    print("Win gamer 2.")



