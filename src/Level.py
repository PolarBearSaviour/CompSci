import json
import random
import os
from constants import MAP_KEY
NOT_FOUND = -1
REQUIRED_FIELDS = ('number-of-players', 'number-of-objectives',
                   'random-objectives', 'number-of-rows',
                   'number-of-columns')

NUMERIC_FIELD = ('number-of-players', 'number-of-objectives', 'number-of-rows',
                'number-of-columns')

BOOLEAN_FIELDS = ('random-objectives', 'random-spawns')

class MismatchingMetadata(Exception):
    pass

class MissingAttribute(Exception):
    pass


class Level:
    """
        This class represents a level in the game. The class reads in the
        information from a file and validates it. Making sure there are the correct number
        of spawns, rows, columns amd objectives.
    """
    def __init__(self, levelName):
        self.levelName = levelName
        self._level = []
        self._metadata = {}

    def __str__(self):
        string = "Level name: {0} \n".format(self.levelName)
        if self._level:
            for key, value in self._metadata.items():
                string += "{0}:{1} \n".format(key, value)
            for row in self._level:
                for column in row:
                    string += str(column)
                string += "\n"
        return string

    def _readInLevel(self):
        """
            Reads in level from file. For internal use
            only
        """
        currentPath = os.path.dirname(__file__)
        #creates URL for the level assets
        levelURL = os.path.relpath('../levels/{0}/{0}.txt'.format(self.levelName), currentPath)

        f = open(levelURL, 'r')

        # Reads in each line and converts them into an integer
        for line in f:
            elements = line.split(',')
            data = [int(element) for element in elements]
            self._level.append(data)

        f.close()
        #creates URL for the metadata of the level
        metadataURL = os.path.relpath('../levels/{0}/{0}.json'.format(self.levelName), currentPath)

        with open(metadataURL) as metadataFile:
            self._metadata = json.load(metadataFile)

    def _checkfieldsValid(self):
        """
            Validates each field in the metadata dictionary. Making
            sure they are of the correct type and all required fields
            are there.
        """
        # Makes sure all the required feilds are in the metadata dictionary
        for field in REQUIRED_FIELDS:
            if not field in self._metadata:
                raise MissingAttribute("Error: Missed out required field {0}. In file {1}.json".format(field, self.levelName))

        # Makes sure all the fields are of the correct type
        for key, value in self._metadata.items():
            if key in NUMERIC_FIELD:
                if isinstance(value, int):
                    if value < 0:
                        raise ValueError("Error: value of {0} must be greater than zero. File: {1}.json".format(key, self.levelName))
                else:
                    raise TypeError("Error: value of {0} must be an integer. File: {1}".format(key, self.levelName))
            elif key in BOOLEAN_FIELDS:
                # Makes sure that the values in the json file were explicity true or false
                if not value == True and not value == False:
                    raise TypeError("Error: value of {0} must be a boolean (true or false). File: {1}.json".format(key, self.levelName))


    def _validateRowsColumns(self):
        """
            Makes sure the number of rows and columns specified in
            the json file matches the number in the text file
        """
        rowCounter = 0
        for row in self._level:

            # Counts the number of columns
            columnCounter = 0
            for column in row:
                columnCounter += 1

            # Throws error if number of columns does not match with the JSON file
            if columnCounter != self._metadata['number-of-columns']:
                raise MismatchingMetadata("Error: number of columns in {0}.json does not macth {0}.txt".format(self.levelName))

            rowCounter += 1

        # Throws an error if number of rows don't match
        if rowCounter != self._metadata['number-of-rows']:
            raise MismatchingMetadata("Error: number of rows in {0}.json does not macth {0}.txt".format(self.levelName))


    def _findElementInLevel(self, element):
        """
            Finds a given element in the level and will return the position.
            Will return -1 if not found or there mutliple then an array of
            positions
        """

        positions = [[i,j] for i, row in enumerate(self._level) for j, col in enumerate(row) if col == element]

        if not positions:
            return NOT_FOUND
        else:
            return positions

    def _randomlyInsertValues(self, value, numberOfValues):
        """
            Will randomly insert values into the Level. Throws
            error if value isn't an integer
        """
        if not isinstance(value, int):
            raise Exception("Error: value should be an integer")

        for item in range(numberOfValues):
            occupied = True
            while occupied:
                row = random.randint(0, 28)
                col = random.randint(0, 28)
                occupied = not self._level[row][col] == 0
            self._level[row][col] = value

    def _checkSuitableNumber(self, mapKey, metaKey):
        """
            Makes sure there is the correct number of a given item
            in the level (i.e. the txt and json files match up)
        """
        values = self._findElementInLevel(MAP_KEY[mapKey])
        if values == NOT_FOUND:
            raise MismatchingMetadata("Error: no {0} in {1}".format(mapKey, self.levelName))
        elif self._metadata[metaKey] != len(values):
            raise MismatchingMetadata("Error: not enough {0} in {1}".format(mapKey, self.levelName))

    def _parseMetadata(self):
        """
            Validates and then setup the level according to the
            instructions left in the JSON file.
        """
        self._checkfieldsValid()
        self._validateRowsColumns()
        self._checkSuitableNumber('SPAWN', 'number-of-players')

        if not self._metadata['random-objectives']:
            self._checkSuitableNumber('OBJECTIVES', 'number-of-objectives')
        elif self._metadata['random-objectives']:
            self._randomlyInsertValues(MAP_KEY['OBJECTIVES'], self._metadata['number-of-objectives'])

    def init(self):
        """
            Reads the level and parses the meta-data. To
            create the level
        """
        self._readInLevel()
        if self._metadata and self._level:
            self._parseMetadata()
        else:
            raise Exception("Error: please fill out {}.json".format(self.levelName) if self._level else "Error: {} already initiated".format(self.levelName))

    def getLevel(self):
        """
            Returns the 2D array representing
            the level.
        """
        # Makes sure the level has been read in
        if self._level:
            return self._level
        else:
            raise Exception("Error: {} is not initiated".format(self.levelName))


    def getMetadata(self):
        return self._metadata

    def accessMetadata(self, nameOfElement):
        """
            Returns a given piece of meta-data. Provding it
            is given a valid key
        """
        # Makes sure level has been read in first
        if self._level:
            return self._metadata[nameOfElement]
        else:
            raise Exception("Error: {} is not initiated".format(self.levelName))


def main():
    l = Level('firstLevel')
    l.init()
    level = l.getLevel()

if __name__ == '__main__':
    main()
