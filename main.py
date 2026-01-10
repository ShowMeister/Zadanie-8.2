import pandas as pd

data = {
    'TITLE': ['GREATEST HITS', 'GOLD - GREATEST HITS', "SGT PEPPER'S LONELY HEARTS CLUB BAND", '21', 
              "WHAT'S THE STORY MORNING GLORY", 'THRILLER', 'THE DARK SIDE OF THE MOON', 'BROTHERS IN ARMS',
              'BAD', 'GREATEST HITS II', 'RUMOURS', 'THE IMMACULATE COLLECTION', 'BACK TO BLACK', 'STARS',
              'COME ON OVER', 'LEGEND', 'BACK TO BEDLAM', 'URBAN HYMNS', 'BAT OUT OF HELL', '1',
              'BRIDGE OVER TROUBLED WATER', 'DIRTY DANCING', 'SPIRIT', 'CRAZY LOVE', 'NO ANGEL',
              'WHITE LADDER', '25', 'TALK ON CORNERS', 'SPICE', 'THE FAME', 'A RUSH OF BLOOD TO THE HEAD',
              'LIFE FOR RENT', 'ONLY BY THE NIGHT', 'BEAUTIFUL WORLD', 'HOPES AND FEARS', 'THE JOSHUA TREE',
              'THE WAR OF THE WORLDS', 'SCISSOR SISTERS', 'BUT SERIOUSLY', 'X&Y', 'JAGGED LITTLE PILL',
              'TUBULAR BELLS', 'THE MAN WHO', 'TRACY CHAPMAN', 'PARACHUTES', 'GREATEST HITS',
              'GREASE', "I'VE BEEN EXPECTING YOU", 'X', 'COME AWAY WITH ME', 'GRACELAND',
              'THE SOUND OF MUSIC', 'LADIES & GENTLEMEN - THE BEST OF', 'TANGO IN THE NIGHT',
              'THE MARSHALL MATHERS LP', 'SWING WHEN YOU\'RE WINNING', 'PROGRESS', 'EYES OPEN',
              'NEVER FORGET - THE ULTIMATE COLLECTION', 'AUTOMATIC FOR THE PEOPLE'],
    'ARTIST': ['QUEEN', 'ABBA', 'BEATLES', 'ADELE', 'OASIS', 'MICHAEL JACKSON', 'PINK FLOYD', 'DIRE STRAITS',
               'MICHAEL JACKSON', 'QUEEN', 'FLEETWOOD MAC', 'MADONNA', 'AMY WINEHOUSE', 'SIMPLY RED',
               'SHANIA TWAIN', 'BOB MARLEY & THE WAILERS', 'JAMES BLUNT', 'VERVE', 'MEAT LOAF', 'BEATLES',
               'SIMON & GARFUNKEL', 'ORIGINAL SOUNDTRACK', 'LEONA LEWIS', 'MICHAEL BUBLE', 'DIDO',
               'DAVID GRAY', 'ADELE', 'CORRS', 'SPICE GIRLS', 'LADY GAGA', 'COLDPLAY',
               'DIDO', 'KINGS OF LEON', 'TAKE THAT', 'KEANE', 'U2', 'JEFF WAYNE', 'SCISSOR SISTERS',
               'PHIL COLLINS', 'COLDPLAY', 'ALANIS MORISSETTE', 'MIKE OLDFIELD', 'TRAVIS', 'TRACY CHAPMAN',
               'COLDPLAY', 'ABBA', 'ORIGINAL SOUNDTRACK', 'ROBBIE WILLIAMS', 'ED SHEERAN', 'NORAH JONES',
               'PAUL SIMON', 'ORIGINAL CAST RECORDING', 'GEORGE MICHAEL', 'FLEETWOOD MAC', 'EMINEM',
               'ROBBIE WILLIAMS', 'TAKE THAT', 'SNOW PATROL', 'TAKE THAT', 'REM'],
    'YEAR': [1981, 1992, 1967, 2011, 1995, 1982, 1973, 1985, 1987, 1991, 1977, 1990, 2006, 1991,
             1997, 1984, 2004, 1997, 1977, 2000, 1970, 1987, 2007, 2009, 2000, 1998, 2015, 1997,
             1996, 2008, 2002, 2003, 2008, 2006, 2004, 1987, 1978, 2004, 1989, 2005, 1995, 1973,
             1999, 1988, 2000, 1975, 1977, 1998, 2014, 2002, 1986, 1965, 1998, 1987, 2000, 2001,
             2010, 2006, 2005, 1992],
    'HIGH_POSN': [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1,
                  1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
}

df = pd.DataFrame(data)

# Zamień nagłówki na polskie
df.columns = ['TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']

print("1. Ilu pojedynczych artystów znajduje się na liście?")
unique_artists = df['ARTYSTA'].nunique()
print(f"Liczba unikalnych artystów: {unique_artists}\n")

print("2. Które zespoły pojawiają się najczęściej na liście?")
artist_counts = df['ARTYSTA'].value_counts()
print(artist_counts.head(10))
print()

print("3. Zmień nagłówki kolumn na format: Pierwsza wielka, reszta małe litery")
df.columns = [col.capitalize() for col in df.columns]
print(f"Nowe kolumny: {list(df.columns)}\n")

print("4. Wyrzuć z tabeli kolumnę 'Max poz'")
df = df.drop('Max poz', axis=1)
print(f"Kolumny po usunięciu: {list(df.columns)}\n")

print("5. W którym roku wyszło najwięcej albumów znajdujących się na liście?")
year_counts = df['Rok'].value_counts()
print(f"Rok z najwięcej albumami: {year_counts.index[0]} ({year_counts.iloc[0]} albumów)")
print(year_counts.head(10))
print()

print("6. Ile albumów wydanych między 1960 a 1990 rokiem włącznie znajduje się na liście?")
albums_1960_1990 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)]
print(f"Liczba albumów z lat 1960-1990: {len(albums_1960_1990)}\n")

print("7. W którym roku wydany został najmłodszy album na liście?")
youngest_year = df['Rok'].max()
youngest_albums = df[df['Rok'] == youngest_year]
print(f"Najmłodszy album wydany w roku: {youngest_year}")
print(f"Album(y): {youngest_albums[['Tytuł', 'Artysta']].to_string(index=False)}\n")

print("8. Przygotuj listę najwcześniej wydanych albumów każdego artysty")
earliest_albums = df.loc[df.groupby('Artysta')['Rok'].idxmin()][['Artysta', 'Tytuł', 'Rok']]
earliest_albums = earliest_albums.sort_values('Artysta')
print(earliest_albums.to_string(index=False))
print()

print("9. Zapisz listę do pliku CSV")
earliest_albums.to_csv('najwczesniejsze_albumy_artystow.csv', index=False, encoding='utf-8')
print("Lista zapisana do pliku: najwczesniejsze_albumy_artystow.csv")

print("\n" + "="*50)
print("PODSUMOWANIE ANALIZY")
print("="*50)
print(f"Unikalnych artystów: {unique_artists}")
print(f"Najczęściej występujący artysta: {artist_counts.index[0]} ({artist_counts.iloc[0]} albumy)")
print(f"Rok z najwięcej albumami: {year_counts.index[0]}")
print(f"Albumy z lat 1960-1990: {len(albums_1960_1990)}")
print(f"Najmłodszy album: {youngest_year}")
