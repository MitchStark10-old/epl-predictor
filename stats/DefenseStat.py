from decimal import Decimal

class DefenseStat:
    weight = Decimal(0.35)

    statQuery = ("SELECT AVG(ShotsOnTarget) FROM TeamGame WHERE EspnGameId IN ( "
                    "SELECT EspnGameId "
                    "FROM EspnGame "
                    "WHERE (HomeTeamId = %s OR AwayTeamId = %s) "
                ") AND EspnTeamId <> %s")

    def getStat(self, teamId, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Possession Stat Query")
        print(teamId)
        print("-------------------------")
        try:
            cursor.execute(self.statQuery, (teamId, teamId, teamId, ))
            print("Completed----------------")
            print(cursor.statement)
            print("--------------------------")
        except:
            print("ERROR---------------------")
            print(cursor.statement)
            print("---------------------------")
            raise
        
        defense = cursor.fetchone()[0]
        print(str(defense) + "% possession for team: " + teamId)

        return defense
        

    def getWeightedStat(self, game, databaseConnection):
        homeTeamDefense = self.getStat(game.getHomeTeamId(), databaseConnection)
        awayTeamDefense = self.getStat(game.getAwayTeamId(), databaseConnection)

        statScore = (homeTeamDefense - homeTeamDefense) * self.weight
        return float(statScore)