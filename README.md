# ChessClassification
This project came about by wanting to compare my playstyle in chess to those of the top players in the world. 
Fundamentally, this project is a trained neural net (.99+) that classifies chess positions based on the player. 
It takes as an input an 8x8 array that represents a chess board (noting format below), 
and outputs a one hot encoded array for each of the top 50 grandmasters (actually 47 because 3 of the top 50 players on chess.com are IMs)
Only blitz (3 minute) games are used at this time but in the future I may include other formats/make models based on faster/slower formats

Data is from chess.com API, formatted from https://www.kaggle.com/datasets/dimitrioskourtikakis/gm-games-chesscom
data is originally in pgn format, which is parsed via the script in parse_game.py

Upcoming features include an interactive board via pygame(or some other front end python animation technology) and a web 
based implementation for my website.
