import unittest
from Level import Level, MissingAttribute
from copy import copy
LEVEL= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,2,1,1,1,1,1,1,1,1,1,1,1],
    [1,3,3,3,3,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

METADATA = {
              "number-of-rows" : 20,
              "number-of-columns" :20,
              "number-of-objectives" : 3,
              "random-objectives" : False,
              "number-of-players" : 2
            }
class TestObject:
    def __init__(self):
        self._level = copy(LEVEL)
        self._metadata = copy(METADATA)
        self.levelName = "stub"
    def __str__(self):
        return self.levelName


class LevelTest(unittest.TestCase):

    def test_create(self):
        self.l = Level("testLevel")
        self.assertIsInstance(self.l, Level)

    def test_empty_level_string(self):
        self.l = Level("testLevel")
        self.assertEqual(str(self.l), "Level name: testLevel \n")

    def test_file_read_in(self):
        self.l = Level("testLevel")
        self.l._readInLevel()
        fileLevel = self.l.getLevel()

        fileMetadata = self.l.getMetadata()

        self.assertListEqual(fileLevel, LEVEL)
        self.assertDictEqual(fileMetadata, METADATA)

    def test_validate_metadata(self):
        def skelelton(key, value, error):
            orig = obj._metadata[key]
            obj._metadata[key] = value
            with self.assertRaises(error):
                Level._checkfieldsValid(obj)
            obj._metadata[key] = orig

        obj = TestObject()
        try:
            Level._validateRowsColumns(obj)
        except Exception:
            self.fail("Error! Exception throw")

        testCase = [{'key' : 'number-of-rows', 'value':'20', 'error' : TypeError}, {'key' : 'random-objectives', 'value': 'crap', 'error' : TypeError},
                    {'key' : 'number-of-columns', 'value':'20', 'error' : TypeError}, {'key' : 'number-of-rows', 'value' : -10, 'error': ValueError}]
        for test in testCase:
            skelelton(test['key'], test['value'], test['error'])

        obj._metadata.pop('number-of-rows')
        with self.assertRaises(MissingAttribute):
            Level._checkfieldsValid(obj)




if __name__ == '__main__':
    unittest.main()
