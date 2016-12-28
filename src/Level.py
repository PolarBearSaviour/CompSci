import json
import random

NOT_FOUND = -1
MAP_KEY = {"BLANK": 0, "WALL": 1, "SPAWN": 2, "OBJECTIVES": 3, "POWER-UPS" : 4, "TRAPS" : 5}
REQUIRED_fieldS = ['number-of-players', 'number-of-objectives',
                   'random-objectives']

NUMERIC_FIELD = ['number-of-players', 'number-of-objectives']
BOOLEAN_FIELDS = ['random-objectives']


class Level:
    def __init__(self, levelName):
        self.levelName = levelName
        self._level = []
        self._metadata = {}
        self._row = 0
        self._column = 0

    def _readInLevel(self):
        levelURL = 'levels/{0}/{0}.txt'.format(self.levelName)

        file = open(levelURL, 'r')
        for line in file:
            elements = line.split(',')
            data = [int(element) for element in elements]
            self._level.append(data)
            self._row += 1


        metadata = 'levels/{0}/{0}.json'.format(self.levelName)
        with open(metadata) as metadata:
            self._metadata = json.load(metadata)

    def _checkfieldsValid(self):
        for field in REQUIRED_fieldS:
            if not field in self._metadata:
                raise Exception("Missed out required field in metadata file!")

        for field in self._metadata:

            if field in NUMERIC_FIELD:
                int(self._metadata[field])
                if self._metadata[field] < 0:
                    raise Exception("Error field {0} must be greater than 0. In {1}.json".format(field, self.levelName))
                if not self._metadata[field] - int(self._metadata[field]) == 0:
                    raise Exception("Error field {0} must be an integer. In {1}.json".format(field, self.levelName))

            if field in BOOLEAN_FIELDS:
                if not self._metadata[field] == True and not self._metadata[field] == False:
                    raise Exception("Error field {0} must be a boolean value. In {1}.json".format(field, self.levelName))

    def _findElementInLevel(self, element, mutliple = False):
        positions = list()
        for i, row in enumerate(self._level):
            for j, col in enumerate(row):
                if col == element:
                    if mutliple:
                        positions.append([i, j])
                    else:
                        return [i,j]
        if not positions:
            return NOT_FOUND
        else:
            return positions

    def _randomlyInsertValues(self, values, numberOfValues):
        for item in range(numberOfValues):
            occupied = True
            while occupied:
                row = random.randint(0, 28)
                col = random.randint(0, 28)
                occupied = not self._level[row][col] == 0
            self._level[row][col] = item

    def _parseMetadata(self):
        self._checkfieldsValid()

        spawns = self._findElementInLevel(MAP_KEY['SPAWN'], True)
        if spawns == NOT_FOUND:
            raise Exception("Error not enough spawns on map for players")

        if not self._metadata["number-of-players"] == len(spawns):
            raise Exception("Error not enough spawns on map for players")

        if not self._metadata['random-objectives']:
            objectives = self._findElementInLevel(MAP_KEY['OBJECTIVES'], True)
            if not len(objectives) == self._metadata['number-of-objectives']:
                raise Exception("Error mismatching number of objectives!")

        elif self._metadata['random-objectives']:
            self._randomlyInsertValues(MAP_KEY['OBJECTIVES'], self._metadata['number-of-objectives'])





    def init(self):
        self._readInLevel()
        if(self._metadata):
            self._parseMetadata()
        else:
            raise Exception("Error please fill out metadata file!")

def main():
    l = Level('firstLevel')
    l.init()
if __name__ == '__main__':
    main()
