def add_songs(*args):
    songs = {}
    result = []

    for arg in args:
        if arg[0] not in songs:
            songs[arg[0]] = arg[1]
        else:
            songs[arg[0]].extend(arg[1])

    for song in songs:
        result.append(f"- {song}")
        if songs[song]:
            result.extend(songs[song])

    return "\n".join(result)
