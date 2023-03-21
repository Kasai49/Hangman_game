import PySimpleGUI as sg
from hangman import easy_words, all_words, startoverlay

def main():
    layout = [
        [sg.Text("Choose your word list:")],
        [sg.Radio("Common English Words", group_id="words", key="common", default=True)],
        [sg.Radio("All English Words", group_id="words", key="all")],
        [sg.Text("Choose your difficulty:")],
        [sg.Radio("Easy", group_id="diff", key="easy", default=True)],
        [sg.Radio("Normal", group_id="diff", key="normal")],
        [sg.Radio("Hard", group_id="diff", key="hard")],
        [sg.Button("Start Game",bind_return_key=True)]
    ]

    window = sg.Window("Hangman Game", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Start Game":
            if values["common"]:
                word = easy_words()
            elif values["all"]:
                word = all_words()
            if values["easy"]:
                lives = 10
            elif values["normal"]:
                lives = 7
            elif values["hard"]:
                lives = 5

            shown = startoverlay(word)
            game_layout = [
                [sg.Text(" ".join(shown), font=("Courier New", 20), key="shown")],
                [sg.Text(f"Remaining Lives: {lives}", key="lives")],
                [sg.Input(key="guess", size=(10,1), enable_events=True), sg.Button("Guess",bind_return_key=True)]
            ]
            game_window = sg.Window("Hangman", game_layout)

            while True:
                event, values = game_window.read()

                if event == sg.WIN_CLOSED:
                    break

                if event == "Guess":
                    guess = values["guess"]
                    checker = 0

                    if guess == "".join(word):
                        sg.popup("YOU WON")
                        game_window.close()
                        break
                    elif guess != "":
                        for nr, i in enumerate(word):
                            if i == guess:
                                shown[nr] = i
                                checker += 1
                        
                        if checker > 0:
                            if word == shown:
                                sg.popup("YOU WON")
                                game_window.close()
                                break
                            else:
                                game_window["shown"].update(" ".join(shown))
                                game_window["guess"].update("")
                        else:
                            lives -= 1
                            if lives == 0:
                                sg.popup("YOU LOST. The word was: " + (''.join(word)))
                                game_window.close()
                                break
                            else:
                                game_window["shown"].update(" ".join(shown))
                                game_window["lives"].update(f"Remaining Lives: {lives}")
                                game_window["guess"].update("")

if __name__ == "__main__":
    main()
