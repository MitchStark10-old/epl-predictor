class PredictionService:

    statServices = []

    #Method Logic: Loop through each statService with the game to get a value
    #Positive value will favor the home team
    #Negative value will favor the away team
    #Final magnitude should represent goal differential
    def predictGame(game):
        print("Done")