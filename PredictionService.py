from stats.ExhaustionStat import ExhaustionStat

class PredictionService:

    statServices = [ExhaustionStat()]

    #Method Logic: Loop through each statService with the game to get a value
    #Positive value will favor the home team
    #Negative value will favor the away team
    #Final magnitude should represent goal differential
    def predictGame(self, game, databaseConnector):
        goalDifferential = 0
        for statService in self.statServices:
            goalDifferential += statService.getWeightedStat(game, databaseConnector)
        return goalDifferential