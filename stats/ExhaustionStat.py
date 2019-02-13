from dateutil import parser
from datetime import datetime, timedelta

class ExhaustionStat:
    weight = 0.1

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


        gamesInLastWeek = 0
        oneWeekAgo = datetime.now() - timedelta(days = 7)
        for gameDateString in gameDateList:
            gameDate = self.parseGameDateString(gameDateString[0])
            if gameDate > oneWeekAgo:
                gamesInLastWeek += 1
                print("Game date: " + str(gameDateString))
            
        print(str(gamesInLastWeek) + " games played in last week for team: " + teamId)
        return gamesInLastWeek
        
    def getWeightedStat(self, game, databaseConnection):
        homeTeamGames = self.getStat(game.getHomeTeamId(), databaseConnection)
        awayTeamGames = self.getStat(game.getAwayTeamId(), databaseConnection)

        statScore = (awayTeamGames - homeTeamGames) * ExhaustionStat.weight
        return statScore


    def parseGameDateString(self, gameDateString):
        return parser.parse(gameDateString)