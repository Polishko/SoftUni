from project.song import Song


class Album:
    def __init__(self, name: str, *song: Song):
        self.name = name
        self.published = False
        self.songs = list(song)

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        copy_songs = self.songs.copy()
        for item in copy_songs:
            if item.name == song_name:
                self.songs.remove(item)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        result = [f"Album {self.name}"]

        for item in self.songs:
            result.append(f"== {item.get_info()}")

        return "\n".join(result)
