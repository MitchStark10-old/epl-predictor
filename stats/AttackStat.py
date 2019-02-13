from decimal import Decimal

class AttackStat:
    weight = Decimal(0.25)

    statQuery = ("SELECT AVG(ShotsOnTarget) "
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
        
        shotsOnTarget = cursor.fetchone()[0]
        print(str(shotsOnTarget) + " average shots on target for team: " + teamId)
        return shotsOnTarget
        

    def getWeightedStat(self, game, databaseConnection):
        homeTeamAttack = self.getStat(game.getHomeTeamId(), databaseConnection)
        awayTeamAttack = self.getStat(game.getAwayTeamId(), databaseConnection)

        statScore = (homeTeamAttack - awayTeamAttack) * self.weight
        return float(statScore)