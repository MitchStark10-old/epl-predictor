class GameDao:

    addGameInsert = ("INSERT INTO EspnGame "
                    "(EspnGameId, GameDate, HomeTeamId, AwayTeamId, HomeTeamScore, AwayTeamScore, PredictedHomeTeamScore, PredictedAwayTeamScore, Competition) "
                    "VALUES (%(espnGameId)s, %(date)s, %(homeTeamId)s, %(awayTeamId)s, %(homeTeamScore)s, %(awayTeamScore)s, %(predictedHomeTeamScore)s, %(predictedAwayTeamScore)s, %(competition)s)")

    addGameUpdate = ("Update EspnGame \n"
                    "SET PredictedHomeTeamScore = %(predictedHomeTeamScore)s, \n"
                    "    PredictedAwayTeamScore = %(predictedAwayTeamScore)s \n"
                    "WHERE EspnGameId = %(espnGameId)s")


    existingGameQuery = ("SELECT COUNT(*) FROM EspnGame WHERE EspnGameId = %(espnGameId)s")

    def insertNewGame(game, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Insert New Game: ")
        print(game.__dict__)
        print("-------------------------")
        try:
            cursor.execute(GameDao.addGameInsert, game.__dict__)
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

    def updateGame(game, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Update Game: ")
        print(game.__dict__)
        print("-------------------------")
        try:
            cursor.execute(GameDao.addGameUpdate, game.__dict__)
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
        

    def checkIfGameExists(game, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Checking if game: " + game.getEspnGameId() + " exists")
        cursor.execute(GameDao.existingGameQuery, game.__dict__)
        gameCount = cursor.fetchone()[0]
        print("Existing Games with id: " + str(game.getEspnGameId()) + ": " + str(gameCount))
        return gameCount > 0