class ExhaustionStat:

    #TODO: Fix the weight value
    weight = 2

    statQuery = ("SELECT GameDate "
                "FROM EspnGame "
                "WHERE (HomeTeamId = %(espnTeamId)s OR AwayTeamId = %(espnTeamId)s);")

    def getStat(game, databaseConnection):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Insert New Game: ")
        print(game.__dict__)
        print("-------------------------")
        try:
            cursor.execute(statQuery, game.__dict__)
            dbConnection.commit()
            print("Completed----------------")
            print(cursor.statement)
            print("--------------------------")
        except:
            print("ERROR---------------------")
            print(cursor.statement)
            print("---------------------------")
            raise
        cursor.close()
        
    def getWeightedStat():
        return getStat() * weight