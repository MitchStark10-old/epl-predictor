from decimal import Decimal

class HomeFieldAdvStat:
    weight = 0.2

    def getWeightedStat(self, game, databaseConnection):
        return self.weight