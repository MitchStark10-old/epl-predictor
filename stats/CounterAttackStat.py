from decimal import Decimal

class CounterAttackStat:
    weight = 1

    statQuery = ("SELECT AVG(ShotsOnTarget) / AVG(PossessionPercent) "
                "FROM TeamGame "
                "WHERE EspnTeamId = %s;")

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
        
        counterAttack = cursor.fetchone()[0]
        print(str(counterAttack) + " counter attack value for team: " + teamId)

        return counterAttack
        

    def getWeightedStat(self, game, databaseConnection):
        homeTeamCounterAttack = self.getStat(game.getHomeTeamId(), databaseConnection)
        awayTeamCounterAttack = self.getStat(game.getAwayTeamId(), databaseConnection)

        statScore = (homeTeamCounterAttack - awayTeamCounterAttack) * self.weight
        print("Final Counter Attack Stat Score: " + str(statScore))
        return float(statScore)