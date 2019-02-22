from decimal import Decimal

class PossessionStat:
    weight = Decimal(0.05)

    statQuery = ("SELECT AVG(PossessionPercent) "
                "FROM TeamGame "
                "WHERE EspnTeamId = %s ;")

    def getStat(self, teamId, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Possession Stat Query")
        print(teamId)
        print("-------------------------")
        try:
            cursor.execute(self.statQuery, (teamId, ))
            print("Completed----------------")
            print(cursor.statement)
            print("--------------------------")
        except:
            print("ERROR---------------------")
            print(cursor.statement)
            print("---------------------------")
            raise
        
        possession = cursor.fetchone()[0]
        print(str(possession) + "% possession for team: " + teamId)

        return possession
        

    def getWeightedStat(self, game, databaseConnection):
        homeTeamAvgPossession = self.getStat(game.getHomeTeamId(), databaseConnection)
        awayTeamAvgPossession = self.getStat(game.getAwayTeamId(), databaseConnection)

        statScore = (homeTeamAvgPossession - awayTeamAvgPossession) * self.weight
        print("Final Possesion Stat Score: " + str(statScore))
        return float(statScore)