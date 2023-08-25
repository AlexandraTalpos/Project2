import requests

def main():
    api_key = ' 65ae31c5'  

    
    movie_title = input("Introduceți titlul unui film: ")

    
    url = f'http://www.omdbapi.com/?i=tt3896198&apikey=65ae31c5'

    response = requests.get(url)

    # Verificam dacă răspunsul este de succes 
    if response.status_code == 200:
        movie_data = response.json()

        # Afișam informațiile despre film
        print("Informații despre film:")
        print(f"Titlu: {movie_data['Title']}")
        print(f"An: {movie_data['Year']}")
        print(f"Regizor: {movie_data['Director']}")
        print(f"Rating: {movie_data['imdbRating']}")
    else:
        print("Cererea către API a eșuat.")

if __name__ == "__main__":
    main()
