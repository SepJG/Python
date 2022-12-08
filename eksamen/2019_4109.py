GENRES = ("Action", "Adventure", "Adult", "Animation", "Comedy", "Crime", "Documentary", "Drama",
"Fantasy", "Family", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Short", "Thriller", "War",
"Western")

COUNTRIES = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Deps", "Argentina",
"Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus",
"Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei",
"Bulgaria", "Burkina", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Rep",
"Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Congo {Democratic Rep}", "Costa Rica",
"Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
"East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji",
"Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
"Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran",
"Iraq", "Ireland (Republic)", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan",
"Kenya", "Kiribati", "Korea North", "Korea South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
"Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia",
"Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
"Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
"Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
"Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
"Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda", "St Kitts & Nevis",
"St Lucia", "Saint Vincent & the Grenadines", "Samoa", "San Marino", "Sao Tome & Principe", "Saudi Arabia",
"Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
"Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden",
"Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad & Tobago",
"Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
 "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
"Yemen", "Zambia", "Zimbabwe")

# Oppgave 3.1 (5%)
# Skriv funksjonen input_text med tre parametere prompt, min_char og max_chars. Funksjonen skal spørre
# om tekst-input fra brukeren med et spørsmål angitt av parameteren prompt som skal være av minimum
# lengde min_char og maksimum lengde max_char angitt i antall karakterer. Funksjonen skal fortsette å spørre
# brukeren om å skrive inn et svar inntil svaret har passe lengde. Hvis svaret er for kort, skal "Text is too short!"
# med et innrykk skrives til skjerm. Hvis svaret er for langt, skal "Text is too long!" med innrykk skrives til skjerm.
# Funksjonen skal returnere en tekststreng.

def input_text(prompt, min_char, max_char):
  streng = input(prompt)
  lengde = len(streng)

  if lengde < min_char:
    print("\tText is too short!")
    return input_text(prompt, min_char, max_char)
  
  if lengde > max_char:
    print("\tText is too long!")
    return input_text(prompt, min_char, max_char)

  return streng

# print(input_text("Title of the film: ", 3, 20))


# Oppgave 3.2 (5%)
# Skriv funksjonen input_num som har tre parametere prompt, min_num og max_num. Funksjonen skal
# spørre brukeren om å skrive inn et heltall med spørsmål spesifisert av prompt. Funksjonen skal forsette å
# spørre brukeren inntil tallet er større eller lik min_num, mindre eller lik max_num og at brukeren ikke skriver
# inn noen annet enn et heltall (f.eks. tekst eller flyttall).
# Hvis input fra bruker ikke er et heltall, skal "Must be an integer" med innrykk bli skrevet til skjermen. Hvis input
# fra bruker er et tall mindre enn min_num eller større enn max_num, skal "Must be a number between
# [min_num] og [max_num] med innrykk skrives til skjerm.
# Funksjonen skal returnere et heltall.

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def input_num(prompt, min_num, max_num):
    while True:
        streng = input(prompt)
        if not is_int(streng):
            print("\tMust be an integer")
            continue
            
        num = int(streng)
        if num < min_num or num > max_num:
            print(f"\tMust be a number between {min_num} and {max_num}")
            continue

        return num

# print(input_num("Age rating (0 - 18): ", 0, 18))


# Oppgave 3.3 (5%)
# Skriv funksjonen input_selection som har to parametere prompt og selections. Funksjonen skal hente tekstinput fra brukeren med et spørsmål spesifisert av prompt. Funksjonen skal spørre brukeren om input helt til
# brukeren har gitt et svar som befinner seg i tuplet selections. Hvis brukeren skriver et svar som ikke er lik noen
# av elementene i tuplet, skal funksjonen skrive til skjerm "Not a valid choice!" med innrykk". Videre skal
# funksjonen skrive til skjerm "Options that start with XX" der XX er de to første bokstavene av det brukeren
# skrev inn. Funksjonen skal så liste ut alle elementene i selections som starter med de to første bokstavene av
# det brukeren skrev inn. Funksjonen skal returnere en tekststreng.

def input_selection(prompt, selections):
    sel = input(prompt)
    if sel in selections:
        return sel

    print(sel)
    print("\tNot a valid choice!")

    # min call handles the case where sel has a lenght less than
    # 2, which would cause error otherwise
    start = sel[:min(2, len(sel))]
    
    print(f"Options that start with {start}:")
    for selection in selections:
        if selection.startswith(start):
            print(selection)
    
    return input_selection(prompt, selections)

# print(input_selection("Country: ", COUNTRIES))


# Oppgave 3.4 (5%)
# Skriv funksjonen enter_title som har ingen parametere. Funksjonen skal benytte seg av funksjonene i de
# tidligere oppgavene (3.1-3.3) for å spørre om input fra brukeren om følgende:
# "Title: " (tittel på film) på mellom 1 og 100 tegn.
# "Year: " (året filmen ble utgitt) angitt mellom år 1900 og 2019.
# "Genre: " (sjanger for filmen) angitt som en av sjangrene i tuplet GENRES.
# "Age rating (0-18): " (aldersgrense for filmen) angitt mellom 0 og 18 år.
# "Country: " (landet filmen ble laget) angitt som et lovlig land i tuplet COUNTRIES.
# "Score (0-100): " (vurdering av filmen) angitt mellom 0 og 100.
# "Comment: " (kort kommentar til vurdering av filmen) på mellom 10 og 100 tegn.
# Funksjonen skal returnere et tuppel av resultatet av input fra brukeren på de sju punktene ovenfor


def enter_title():
    title = input_text("Title: ", 1, 100)
    year = input_num("Year: ", 1900, 2019)
    genre = input_selection("Genre: ", GENRES)
    age_rating = input_num("Age rating: ", 0, 18)
    country = input_selection("Country: ", COUNTRIES)
    score = input_num("Score: ", 0, 100)
    comment = input_text("Comment: ", 10, 1000)
    return title, year, genre, age_rating, country, score, comment

# print(enter_title())


# Oppgave 3.5 (5%)
# Skriv funksjonen add_movies som har en parameter db som er en dictionary som tar vare på filminformasjon
# som spesifisert i starten av oppgaven. Funksjonen skal spørre brukeren "Do you want to enter another movie
# (y/n)?" og så lenge brukeren svarer "y" eller "Y" skal brukeren blir spurt om å legge inn filminformasjon ved
# hjelp av funksjonen enter_title (som spesifisert i forrige oppgave), som videre skal legges til
# dictionarien db. Filminformasjon i db er strukturert slik at tittelen til filmen er nøkkel (ID), og resten av
# informasjonen skal legges til som et tuppel. Hvis filmen finnes fra før i databasen, skal følgende skrives til
# skjerm "Movie XXX has been updated". XXX er tittelen på filmen. Hvis filmen ikke finnes fra før, skal følgende
# skrives til skjerm: "Movie XXX has been added".
# Funksjonen skal returnere en oppdatert dictionary db.

def add_movies(db):
  while(True):
    answer=input("Do you want to enter a movie (y/n)? ")
    if answer[0].upper()=="Y":
      movie=enter_title()
      if movie[0] in db:
        print(f"Movie '{movie[0]}' has been updated\n")
      else:
        print(f"Movie '{movie[0]}' has been added\n")
      db[movie[0]]=movie[1:len(movie)]
    else: 
      return db
db = {}
# db=add_movies(db)
# print(db)


# Oppgave 3.6 (5%)
# Skriv funksjonen save_movies som har en parameter db som er en dictionary som spesifisert i begynnelsen
# av oppgaven. Funksjonen skal spørre brukeren om filnavn med følgende tekst "Save database to filename: "
# der filnavnet skal minst være mellom 5 og 20 tegn. Innholdet av db skal lagres til fil med strukturen bevart. Hvis
# lagring til fil går bra, skal følgende skrives ut til skjerm "The database was saved to XXX", der XXX er navnet
# på fila. Hvis noe går galt med lagring av fil, skal følgende skrives ut til skjerm "Database could not be saved to
# XXX", der XXX er navnet på fila. Funksjonen har ingen retur

import pickle
def save_movies(db):
  try:
    filename=input_text("Save database to filename: ",5,20)
    f=open(filename, "wb")
    pickle.dump(db,f)
    print(f"The database was saved to {filename}")
  except:
    print(f"\tDatabase could not be saved to {filename}")
  finally:
    f.close()

# save_movies(db)


# Oppgave 3.7 (5%)
# Skriv funksjonen load_movies som har en parameter FILES som er en liste med alle filene som befinner seg i
# nåværende filmappe. Funksjonen skal spørre brukeren om filnavn med teksten "Load database from filename:
# " og bruke funksjonen input_selection fra Oppgave 3.3 for å sjekke om filnavnet er en av filene som befinner
# seg i nåværende filmappe, og spørre på nytt hvis det ikke er det. Dictionarien med all filminformasjonen skal
# lastes inn til variabelen db. Hvis filoperasjonen gikk bra, skal følgende skrives til skjerm: "A database has
# been loaded from XXX", der XXX er navnet på fila. Hvis filoperasjonen ikke gikk bra, skal følgende skrives til
# skjerm: "Could not load database from XXX", der XXX er navnet på fila. Funksjonen returnerer dictionarien db.

def load_movies(FILES):
  try:
    filename=input_selection("Load database from filename: ",FILES)
    f=open(filename, "rb")
    db=pickle.load(f)
    print(f"A database has been loaded from {filename}")
    return db
  except:
    print(f"\tCould not load database from {filename}")
    return None
  finally:
    f.close()


# Oppgave 3.8 (5%)
# Skriv funksjonen show_movies som har en parameter db som er en dictionary som beskrevet først i
# oppgaven. Funksjonen skal skrive ut informasjon i db, der hver linje skal formateres på følgende måte (det
# skal være en space mellom hvert element):
# Årstall (fire siffer)
# Tittel (20 tegn til tittel, venstrejustert, og kutte til 20 tegn hvis tittel er lengre)
# Sjanger 10 tegn til sjanger, venstrejustert, og kutte til 10 tegn hvis sjanger er lengre)
# Land (15 tegn til land, venstrejustert, og kutte til 15 tegn hvis lang er lengre)
# "Age:" og Aldersgrense (tall høyrejustert 4 plasser)
# "Score:" og Vurderingsscore (tall høyrejustert 4 plasser)
# "%"

def show_movies(db):
  for movie in db:
    title = movie[:20]
    year = db[movie][0]
    genre = db[movie][1][:10]
    age = db[movie][2]
    country = db[movie][3][:15]
    score = db[movie][4]
    print(f"{year} {title:20s} {genre:10s} {country:15} Age:{age:4} Score:{score:4}%")


# Oppgave 3.9 (5%)
# Skriv funksjonen most_pop_genre som har en parameter db som er definert i starten av oppgaven.
# Funksjonen skal undersøke innholdet i dictionarien db for å finne hvilken sjanger som er mest populær (dvs.
# finnes flest filmer i). Funksjonen skal returnere navnet på sjangeren i db der det finnes mest filmer. Hvis det er
# flere genre som har like mange filmer, skal første genre man finner returneres.

# Help function
def count_genre(db):
  cg = {}
  for movie in db:
    genre = db[movie][1]
    cg[genre] = cg.get(genre,0)+1
  return cg

def most_pop_genre(db):
  cg = count_genre(db)
  max_count=0
  pop_genre=""
  for genre in cg:
    if cg[genre]>max_count:
      max_count=cg[genre]
      pop_genre=genre
  return pop_genre

# Oppgave 3.10 (5%)
# Skriv funksjonen top3_countries som har en parameter db som en dictionary som beskrevet i starten av
# oppgaven. Funksjonen skal gå igjennom db og finne de tre landene som har flest filmer i databasen. Hvis det
# er flere land som har likt antall filmer, skal man bare ta de første i lista. Funksjonen skal ikke returnere noe,
# men skal skrive ut navnet på de tre landene med mest filmer og antall filmer hvert land har. 20 tegn skal settes
# av til å skrive ut landet (se eksemplet under).

# help-funcion
def count_countries(db):
  cc = {}
  for movie in db:
    country = db[movie][3]
    cc[country] = cc.get(country,0)+1
  return cc

def top3_countries(db):
  cc = count_countries(db)
  L=[[0,-1],[0,-1],[0,-1]]
  for country in cc:
    for i in range(len(L)):
      if cc[country]>L[i][1]:
        if i<2:
          L[i+1][0]=L[i][0]
          L[i+1][1]=L[i][1]
        L[i][0]=country
        L[i][1]=cc[country]
        break
  for i in range(len(L)):
    print(f'{L[i][0]:20s}: {L[i][1]} movies')
