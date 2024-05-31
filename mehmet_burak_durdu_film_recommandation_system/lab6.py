from recommandations import topMatches, sim_jaccard, getRecommendations, sim_cosine

def loadMovieGenre(data):
    veri = open(data).readlines()
    genres = ["Unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama",
              "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
    prefs = dict()
    #print(veri)
    for satir in veri:
        film_verileri = satir.split("|")
        film_adi = film_verileri[1]
        tur_offset = 5
        
        prefs.setdefault(film_adi, dict())
        for i in range(tur_offset, len(film_verileri)):
            if film_verileri[i] == "1":
                if "toy" in film_adi.lower():
                    print(film_adi, genres[i-tur_offset])
                prefs[film_adi][genres[i-tur_offset]] = 1
                
    return prefs

filmler = loadMovieGenre('filmler.txt')
film_listesi = ['Star Wars (1977)', 'Lion King, The (1994)', 'Godfather, The (1972)']

print('-'*20)
for film in film_listesi:
    print('-'*20)
    print(film, filmler[film])
    print(topMatches(filmler, film, 3, sim_jaccard))
    print(getRecommendations(filmler,film,sim_cosine ))




