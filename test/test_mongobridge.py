# Edited by Evan Burch
from unittest import TestCase
from datalayer.mongobridge import MongoBridge


class TestMongoBridge(TestCase):

    def setUp(self) -> None:
        self.mongo_bridge = MongoBridge("mongodb://localhost:27017/", "BristolData", "Artists")
        self.mongo_bridge_default = MongoBridge()

    def test_get_all_artists(self):
        artists = self.mongo_bridge.get_all_artists()
        self.assertEqual(179, len(artists))
    #    self.assertEqual(1826136, artists[60]["artistID"])
    #    self.assertEqual(628155, artists[178]["artistID"])
        a0 = next(item for item in artists if item["artistID"] == 1826136)["artistName"]
        self.assertEqual("Stephen Tarter", a0)
        a1 = next(item for item in artists if item["artistID"] == 628155)["artistName"]
        self.assertEqual("A. P. Carter", a1)

    def test_get_all_artists2(self):  # Same test as above but uses the default constructor
        artists = self.mongo_bridge_default.get_all_artists()
        self.assertEqual(179, len(artists))
        #    self.assertEqual(1826136, artists[60]["artistID"])
        #    self.assertEqual(628155, artists[178]["artistID"])
        a0 = next(item for item in artists if item["artistID"] == 938856)["artistName"]
        self.assertEqual("Vernon Dalhart", a0)
        a1 = next(item for item in artists if item["artistID"] == 938882)["artistName"]
        self.assertEqual("Andrew Jenkins", a1)

    def test_get_artists_from_list(self):
        ids = [938895, 2634203, 1141486, 908705, 2411933, 2304638, 3895080, 1448909, 1448911, 1141474, 2916175, 353265, 1141476, 938862, 1141491, 1141484, 1141487, 307357, 1141480, 516930, 1001138, 1141475, 269365, 1141488, 1141483, 1141489, 2867358, 2867360, 2189637, 908699, 1420640, 2867359, 1826135]
        artists = self.mongo_bridge.get_artists_from_list(ids)
        self.assertEqual(33, len(artists))
        # tests whether the artistID at artists[2] is 1141486
        self.assertEqual(1141486, artists[2]["artistID"])

    def test_get_artists_from_list2(self):  # Same test as above but uses the default constructor
        ids = [2867359, 1420640, 908699, 2189637, 2867360, 2867358, 1141489, 1141483, 1141488, 269365, 1141475, 1001138, 516930, 1141480, 307357, 1141487, 1141484, 1141491, 938862, 1141476, 353265, 2916175, 1141474, 1448911, 1448909, 3895080, 2304638, 2411933, 908705, 1141486, 2634203, 938895]
        artists = self.mongo_bridge_default.get_artists_from_list(ids)
        self.assertEqual(32, len(artists))
        # tests whether the artistID at artists[4] is 2867360
        self.assertEqual(2867360, artists[4]["artistID"])

    def test_get_artist_by_id(self):
        # Artist exists
        artist = self.mongo_bridge.get_artist_by_id(269365)
        self.assertEqual(269365, artist["artistID"])
        self.assertEqual("Jimmie Rodgers", artist["artistName"])
        self.assertEqual(0, artist["level"])
        self.assertEqual("James Charles Rodgers", artist["realname"])

        # Artist does not exist
        artist2 = self.mongo_bridge.get_artist_by_id(0)
        self.assertIsNone(artist2)

    def test_get_artist_by_id2(self):  # Same test as above but uses the default constructor
        # Artist exists
        artist = self.mongo_bridge_default.get_artist_by_id(5766040)
        self.assertEqual(5766040, artist["artistID"])
        self.assertEqual("Jim Seany", artist["artistName"])
        self.assertEqual(0, artist["level"])
        self.assertEqual("Ernest Van Stoneman", artist["realname"])

        # Artist does not exist
        artist2 = self.mongo_bridge_default.get_artist_by_id(0)
        self.assertIsNone(artist2)
