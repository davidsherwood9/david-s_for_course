import doctest
from typing import Union


class Cup:
    """
    This class is intended to determine parameters such as size and content of your cup
    """
    def __init__(self, size: Union[int, float], content: str):
        self.size = None
        self.init_size(size)

        if not isinstance(content, str):
            raise TypeError("Wrong data type")
        self.content = content    # What cup is containing

    def init_size(self, size: Union[int, float]):
        """
        size of the cup attribute initialization
        :param size:
        :return:
        """
        if not isinstance(size, (int, float)):
            raise TypeError("Wrong data type")
        if size <= 0:
            raise ValueError("Positive value is required")
        self.size = size    # Size of the cup (diameter [cm])

    def method_1(self):
        pass


Cup_with_coffee = Cup(9, "Coffee")    # for me
print(Cup_with_coffee.size)
print(Cup_with_coffee.content)


class Magazine:
    """
    Thus one is intended to introduce current magazine's properties
    """
    def __init__(self, pages: int, theme: str, rating: Union[int, float]):
        self.pages = None
        self.init_pages(pages)

        if not isinstance(theme, str):
            raise TypeError("Wrong data type")
        if len(theme) > 15:
            raise ValueError("Too many symbols")
        self.theme = theme  # Theme of the magazine

        if not isinstance(rating, int) and not isinstance(rating, float):
            raise TypeError("Wrong data type")
        if rating > 10:
            raise ValueError("Rating value can not be more than 10")
        if rating < 0:
            raise ValueError("Rating value can not be less than 0")
        self.rating = rating  # Rating value

    def init_pages(self, pages: int):
        """
        pages attribute initialization
        :param pages: num of pages of the magazine
        """
        if not isinstance(pages, int):
            raise TypeError("Wrong data type")
        if pages <= 0:
            raise ValueError("Count of pages can not be less than 0")
        self.pages = pages  # Number of pages

    def method_1(self):
        pass


Scopus_Magazine_1 = Magazine(297, "Engineering", 7.78)
print(Scopus_Magazine_1.theme)
print(Scopus_Magazine_1.rating)    # for me


class ManchesterUnited:
    """
    the greatest football team structural decomposition
    """
    def __init__(self, coach: str, num_of_ucl: int, num_of_players: int):
        self.num_of_ucl = None
        self.init_num_of_ucl(num_of_ucl)

        if not isinstance(coach, str):
            self.coach = coach  # Coach name
        if not isinstance(num_of_players, int):
            self.num_of_players = num_of_players  # Number of the team members
        self.coach = coach

    def init_num_of_ucl(self, num_of_ucl: int):
        """
        num_of_ucl attribute initialization
        :param num_of_ucl: num of UCL trophees
        """
        if not isinstance(num_of_ucl, int):
            raise TypeError("Wrong data type")
        self.num_of_ucl = num_of_ucl  # Number of UCL trophees

    def method_1(self):
        pass


MU1992 = ManchesterUnited("Sir Alexander Ferguson", 1, 28)
print(MU1992.coach)
print(MU1992.num_of_ucl)    # for me


if __name__ == "__main__":
    doctest.testmod()
