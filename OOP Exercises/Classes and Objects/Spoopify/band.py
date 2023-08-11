from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for item in self.albums:
            if item.name == album_name:
                if item.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(item)

                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self) -> str:
        result = [f"Band {self.name}"]

        for item in self.albums:
            result.append(f"{item.details()}")

        return "\n".join(result)
