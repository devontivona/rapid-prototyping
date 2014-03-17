import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_definition import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Britney Spears")
new_artist.albums = [Album("Femme Fatale", "Pop", "RCA Records", "CD")]
 
# add more albums
more_albums = [Album("Circus", "Pop", "Jive Records", "CD"),
               Album("Britney Jean",  "Pop", "Jive Records", "CD"),
               Album("The Singles Collection", "Pop", "Jive Records", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("The Weeknd"),
    Artist("James Blake"),
    Artist("Kanye West")
    ])
session.commit()