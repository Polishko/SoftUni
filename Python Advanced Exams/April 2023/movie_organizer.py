def movie_organizer(*info):
    movies = {}
    for movie_info in info:
        name, genre = movie_info[0], movie_info[1]

        if genre not in movies:
            movies[genre] = []
        movies[genre].append(name)

    result = []
    for genre_content in sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{genre_content[0]} - {len(genre_content[1])}")
        for movie in sorted(genre_content[1]):
            result.append(f"* {movie}")

    return "\n".join(result)
