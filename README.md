# plex-imdb-top-250-collection

Python script to create a Plex collection of movies in your library that are in the IMDB Top 250 Movies list.

Plex playlists don't allow filtering by watched status, however you can't order a collection based on IMDB rating...

## TODO:

- Prevent iterating over entire plex library for each imdb movie.


## Usage:

Create a .env file with the following contents (substituting real values):



    plex_server = ''

    plex_username = ''

    plex_password = ''

    plex_library = 'Movies'



Note that `plex_server` is the server _name_ and not the URL.



## Requirements:

cinemagoer



plexapi



python-dotenv



