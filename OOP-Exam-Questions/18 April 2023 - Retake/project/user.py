class User:
    _Max_Rating = 10
    _Decrease_Rating = 2.0
    _Increase_Rating = 0.5

    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating: float = 0
        self.is_blocked: bool = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value.strip() == "":
            raise ValueError("First name cannot be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value.strip() == "":
            raise ValueError("Last name cannot be empty!")
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if value.strip() == "":
            raise ValueError("Driving license number is required!")
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        if new_rating < 0:
            raise ValueError("Users rating cannot be negative!")
        self.__rating = new_rating

    def increase_rating(self):
        new_value = self.rating + self._Increase_Rating
        self.rating = min(self._Max_Rating, new_value)

    def decrease_rating(self):
        new_value = self.rating - self._Decrease_Rating
        if new_value < 0:
            self.rating = 0
            self.is_blocked = True
        else:
            self.rating = new_value

    def __str__(self):
        return f"{self.first_name} {self.last_name} " \
               f"Driving license: {self.driving_license_number} Rating: {self.rating}"
