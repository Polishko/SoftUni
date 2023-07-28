class User:
    _Min_User_Age = 6
    
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list = []
        self.movies_owned: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < User._Min_User_Age:
            raise ValueError(f"Users under the age of {User._Min_User_Age} are not allowed!")
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]

        if self.movies_liked:
            [result.append(m.details()) for m in self.movies_liked]
        else:
            result.append("No movies liked.")

        result.append("Owned movies:")

        if self.movies_owned:
            [result.append(m.details()) for m in self.movies_owned]
        else:
            result.append("No movies owned.")

        return "\n".join(result)
