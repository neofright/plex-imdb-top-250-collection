#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import plexapi
from plexapi.myplex import MyPlexAccount
from imdb import Cinemagoer
   
## https://codereview.stackexchange.com/a/257530
def input_yes_no(prompt: str) -> bool:
    full_prompt = f'{prompt} ([Y]/N): '
    while True:
        answer = input(full_prompt).strip()
        if answer == '':
            return True

        answer = answer[0].lower()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        print('ERROR')

if __name__ == "__main__":
    load_dotenv()
    #######################################
    mfa_enabled = input_yes_no('Does your Plex account use 2FA?')
    if mfa_enabled:
        mfa_token = input('Enter Plex TOTP token: ')
    else:
        mfa_token = ""
    #######################################
    account = MyPlexAccount(os.environ.get('plex_username'), os.environ.get('plex_password') + mfa_token)
    plex = account.resource(os.environ.get('plex_server')).connect()  # returns a PlexServer instance
    #######################################
    ia = Cinemagoer()
    imdb_top_250_movies = ia.get_top250_movies()
    #######################################
    plex_movies = plex.library.section(os.environ.get('plex_library'))

    collection_title = "IMDb Top 250 Movies"
    missing_movies = []

    for imdb_top_250_movie in imdb_top_250_movies:
        movie_found = False
        try:
            plex_movie = plex_movies.getGuid('imdb://tt' + imdb_top_250_movie.movieID)
            movie_found = True
        except:
            missing_movies.append(imdb_top_250_movie)

        if movie_found:
            plex_movie.addCollection(collection_title)
            # plex_movie.removeCollection(collection_title)

    print('Missing Movies:')
    for missing_movie in missing_movies:
        print(missing_movie)