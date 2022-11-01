from typing import List, Tuple
from applayer.artist import Artist
from datalayer.mongobridge import MongoBridge
from multipledispatch import dispatch


class ArtistList(object):
    """
    The ArtistList class consists of two attributes:
        * __artist_objects: List[Artist] (must be Artist objects)
        * __artists: List[Tuple[int, str]] (ex. [(1141480, Alcoa Quartet), (1141491, Alfred G. Karnes)]
          this list must be sorted
    """
    @dispatch(list)
    def __init__(self, ids: List[int]):
        """
        The constructor uses data in mongo to create attributes based on the input ids list;
        Use a Mongobridge object to pull data from the Mongo database; the artists attribute
        must be a sorted list.
        """
        self.__mongo_bridge = MongoBridge()
        self.__artist_objects: List[Artist] = []
        self.__artists: List[Tuple[int, str]] = []

        self.__list_of_dicts = self.__mongo_bridge.get_artists_from_list(ids)
        for i in self.__list_of_dicts:
            self.__artist_objects.append(Artist(i))

        for i in self.__artist_objects:
            self.__artists.append((i.artistID, i.artistName))

        self.__artists.sort(key=lambda artists: artists[1])

    @dispatch()
    def __init__(self):
        """
        Read all of the data from mongo and attributes for all artists; See comment at head of the
        class; the artists attribute must be a sorted list.
        Use a Mongobridge object to pull data from the Mongo database
        """
        self.__mongo_bridge = MongoBridge()
        self.__artist_objects: List[Artist] = []
        self.__artists: List[Tuple[int, str]] = []

        self.__list_of_dicts = self.__mongo_bridge.get_all_artists()
        for i in self.__list_of_dicts:
            self.__artist_objects.append(Artist(i))

        for i in self.__artist_objects:
            self.__artists.append((i.artistID, i.artistName))

        self.__artists.sort(key=lambda artists: artists[1])

    @property
    def artists(self) -> List[Tuple[int, str]]:
        """
        Returns the list of artists as list of tuples of (artistid: int, name: str)
        :return: list of artists
        """
        return self.__artists

    @property
    def artist_objects(self) -> List[Artist]:
        """
        Returns the list of Artist objects
        :return:
        """
        return self.__artist_objects

    def __str__(self) -> str:
        """
        Prints a list of Artist objects separated by a comma ','
        ex: Alcoa Quartet (1141480), Alfred G. Karnes (1141491)
        Note that the formatting of the print of the Artist object is determined by
        the Artist class
        :return: str
        """
        #result: str = self.__artist_objects[0].__str__()
        result: str = ""
        for i in self.__artist_objects:
            result += i.__str__() + ", "
        if len(self.__artist_objects) > 0:
            result = result.rstrip(result[-1])
            result = result.rstrip(result[-1])
        return result
