Movies = []
class Movie:
    def __init__(self, id, title, director, year, genre):
        self.id = id
        self.title = title
        self.director = director
        self.release_year = year
        self.genre = genre

def add_movie():
    id = input("Enter ID: ")
    for m in Movies:
        if m.id == id:
            print("Movie already exists!!")
            return
    title = input("Enter title: ")
    director = input("Enter director: ")
    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("Invalid Year!")
        return
    genre = input("Enter genre: ")

    movie = Movie(id, title, director, year, genre)
    Movies.append(movie)

    print("Movie added")

def view_movies():
    if len(Movies) == 0:
        print("No movies yet")
    else:
        print("\n Movie lists")
        for i, movie in enumerate(Movies, start=1):
            print(i, movie.id, movie.title, movie.director, movie.release_year, movie.genre)

def delete_movie():
        id = input("Enter movie ID to delete: ")
        for movie in Movies:
            if movie.id == id:
                Movies.remove(movie)
                print("movie removed successfully")
                return
        print("No movie found")

def search_movie():
    title = input("Enter movie title to search: ").lower()
    found = False

    for movie in Movies:
        if movie.title.lower() == title:
            print(movie.id, movie.title, movie.director, movie.release_year, movie.genre)
            found = True
    if not found:
        print("Movie not found")

def update_movie():
    id = input("Enter movie ID to update: ")
    for movie in Movies:
        if movie.id == id:
            print("press enter, if not updating")

            new_title = input("New title: ")
            new_director = input("New director: ")
            new_year = input("New year: ")
            new_genre = input("New genre: ")

            if new_title:
                movie.title = new_title
            if new_director:
                movie.director = new_director
            if new_year:
                try:
                    movie.release_year = int(new_year)
                except ValueError:
                    print("Invalid Year!, keeping the old year")
            if new_genre:
                movie.genre = new_genre
            print("Movie updated")
            return
    print("No movie found")



while True:
    print("\n=== Movie List===")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Update movie")
    print("5. Delete movie")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        view_movies()
    elif choice == "3":
        search_movie()
    elif choice == "4":
        update_movie()
    elif choice == "5":
        delete_movie()
    elif choice == "6":
        print("See you later")
        break
    else:
        print("Invalid choice")