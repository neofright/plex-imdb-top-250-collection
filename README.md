# plex-imdb-top-250-collection

Python script to create a Plex collection of movies in your library that are in the IMDB Top 250 Movies list.

Plex playlists don't allow filtering by watched status, however you can't order a collection based on IMDB rating...

## TODO:
- Radarr integration to scrape imdb lists?


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

## Notes:

If you want to use this for an IMDB user list instead, such as the excellent [Spike Lee's Essential Film List (Revised)](https://www.imdb.com/list/ls031959383/) you can easily do so.

Manually change the `collection_title` string (ia can't scrape the collection titles AFAIK), and just kludge the `imdb_top_250_movies` variable to call `ia.get_movie_list('ls031959383')` instead.