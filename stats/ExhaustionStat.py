class ExhaustionStat:
    weight = 0.05

    statQuery = ("SELECT GameDate "
                "FROM EspnGame "
                "WHERE (HomeTeamId = %s OR AwayTeamId = %s);")

    def getStat(self, teamId, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Game Date Query")
        print(teamId)
        print("-------------------------")
        try:
            input = (teamId, teamId)
            cursor.execute(self.statQuery, input)
            print("Completed----------------")
            print(cursor.statement)
            print("--------------------------")
        except:
            print("ERROR---------------------")
            print(cursor.statement)
            print("---------------------------")
            raise
        gameDateList = cursor.fetchall()

        for gameDate in gameDateList:
            print("Game date: " + str(gameDate))
            #Parse game date and check if it was in the past week
            
        return 0
        
    def getWeightedStat(self, game, databaseConnection):
        homeTeamGames = self.getStat(game.getHomeTeamId(), databaseConnection)
        awayTeamGames = self.getStat(game.getAwayTeamId(), databaseConnection)

        statScore = (awayTeamGames - homeTeamGames) * ExhaustionStat.weight
        return statScore