from lessons.car.car import Car, Bus

# магические методы, dunder(double underscore) methods
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.__songs = songs

    def __str__(self):
        return f"<Playlist name:{self.name}, songs: {len(self.__songs)}>"

    def __len__(self):
        return len(self.__songs)

    def __contains__(self, item):
        return item in self.__songs

    def __bool__(self):
        return len(self.__songs) > 1

if __name__ == "__main__":
    playlist_pop = Playlist(
        "pop",
        ["Shape of my heart"]
    )
    print(playlist_pop.name)
    print(playlist_pop)
    print("Длина плейлиста:", len(playlist_pop))
    print("Shape of my heart" in playlist_pop)
    if playlist_pop:
        print("в плейлисте больше 1 песни")
    else:
        print("в плейлисте меньше 2 песни")

    print("=== другие вещи ===")
    car_1 = Car("black", "BMW")
    car_1.drive_to("Bishkek")


