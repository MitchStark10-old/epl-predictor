from stats.ExhaustionStat import ExhaustionStat

class PredictionService:

    statServices = [ExhaustionStat()]

    #Method Logic: Loop through each statService with the game to get a value
    #Positive value will favor the home team
    #Negative value will favor the away team
    #Final magnitude should represent goal differential
    def predictGame(self, game):
        print("Done")