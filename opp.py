class Movie:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.has_watched = False

    def has_watched_movie(self):
            self.has_watched = True
            print(f"---------------You have seen {self.name}----------------")

        
    def __str__(self):
            watched = "Yes" if self.has_watched else "No"

            return (
                f"Movie_Name: {self.name}\n"
                f"Genre: {self.genre}\n"
                f"Movie Rating: {self.rating}\n"
                f"Has Watched: {watched}"
            )
    

movie1 = Movie("SPectre-007", "Action", 95)

print(movie1)

movie1.has_watched_movie()

print(movie1)