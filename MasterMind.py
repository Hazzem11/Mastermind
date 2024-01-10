import random

def score_Checker(e):


  white = 0
  black = 0
  e = False
  winner = False
  #check white score
  for i in code:
    if i in guess:
      white += 1

  #check black score
  for i in range(len(code)):
    if code[i] == guess[i]:
      black += 1

  #check winner
  if black == 4:
    winner = True

  if winner:
    print("You got 4 blacks", name)
    print("You wont the game with", k, "guesse(s) and", penalty,
          "penaltie(s). Congratulations!")
    e = True
  else:
    print("You got", black, "black(s), and", white, "white(s) for this guess.")
    #check lost
    if k == 15:
      print("Sorry", name, "you ran out of guesses and you lost the game with",
            penalty, "penaltie(s).")
      e == True
    if penalty == 5:
      print(
        name,
        ", you lost the game by reaching the maximum number of allowed penalties."
      )
      e == True

  return e


def main():
    global name, code, penalty, k, guess
    name = str(input("What is your name? "))
    print(
        "Welcome to MasterMind", name, "!\n"
                                       "The code maker is here. Available colors are: \n"
                                       "Red, Yellow, Blue, Green, Orange, Pink, Purple, Cyan, Silver, Teal\n"
                                       "You have 15 guesses, total of 5 penalties are allowed but avoid penalties\n"
                                       "The code maker selected 4 colors\n"
                                       "You can start guessing", name)
    code = []
    codeGenerators = [
        "RED", "YELLOW", "BLUE", "GREEN", "ORANGE", "PINK", "PURPLE", "CYAN",
        "SILVER", "TEAL"
    ]
    allColors = [
        "RED", "YELLOW", "BLUE", "GREEN", "ORANGE", "PINK", "PURPLE", "CYAN",
        "SILVER", "TEAL"
    ]
    n = 0
    for i in range(0, 4):
        r = random.randint(0, 9 - n)
        code.append(codeGenerators[r].upper())
        codeGenerators.pop(r)
        n += 1
    end = False
    penalty = 0
    k = 1
    old_color = ""
    mistake = False
    duplicate = False
    missing = False
    while k <= 15 and penalty < 5:
        if end:
            break
        print("Enter guess number", k, ":")
        guess = []
        for j in range(0, 4):
            color = str(input("Color: ")).upper()
            guess.append(color)
            if color == old_color and j != 0 and color != '':
                duplicate = True
            if color not in allColors and color != '':
                mistake = True
            if color == "":
                missing = True
            old_color = color
        if duplicate or mistake or missing:
            if duplicate and mistake == False and missing == False:
                print(
                    "Sorry", name,
                    ", repeated colors are not allowed in this game. One penalty is considered."
                )
            if mistake and missing == False and duplicate == False:
                print(
                    "Sorry ", name,
                    ", cannot recognize the colors you entered. One penalty is considered."
                )
            if missing and mistake == False and duplicate == False:
                print("Sorry", name,
                        ", you need to enter at least 4 colors for each guess. One penalty is considered."

                )
            if mistake and duplicate and missing == False:
                print(
                    "Sorry", name,
                    "repeated colors are not allowed in this game. Also, cannot recognize the colors you entered. One penalty is considered."
                )
            if missing and mistake and duplicate == False:
                print("Sorry", name,
                        ", you need to enter at least 4 colors for each guess. Also, cannot recognize the colors you entered. One penalty is considered."

                )
            if missing and duplicate and mistake == False:
                print("Sorry", name,
                      ", you need to enter at least 4 colors for each guess. Also, repeated colors are not allowed in this game. One penalty is considered."
                      )
            if missing and duplicate and mistake:
                print(
                    "Sorry", name,
                    "repeated colors are not allowed in this game. Also, cannot recognize the colors you entered. Also, you need to enter at least 4 colors for each guess. One penalty is considered."
                     )


            penalty += 1
            print("Total penalties = ", penalty)
            mistake = False
            duplicate = False
            missing = False
        else:
            k += 1
        end = score_Checker(end)

    return code


main()


