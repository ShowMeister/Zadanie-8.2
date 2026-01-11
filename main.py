import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows[1:]:  
    cols = row.find_all('td')
    if len(cols) == 5:
        data.append({
            'POS': cols[0].text.strip(),
            'TITLE': cols[1].text.strip(),
            'ARTIST': cols[2].text.strip(),
            'YEAR': int(cols[3].text.strip()),
            'HIGH POSN': int(cols[4].text.strip())
        })

df = pd.DataFrame(data)

print("Dane wczytane ze strony:")
print(df.head())

df.columns = ['TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']
# Usuń kolumnę POS (pozycja na liście)
df = df[['TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']]

print("\n1. Ilu pojedynczych artystów znajduje się na liście?")
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
