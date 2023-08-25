import sqlite3

def main():
    connection = sqlite3.connect("exemplu.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM filme")
    filme = cursor.fetchall()

    print("Lista de filme:")
    for film in filme:
        print(f"ID: {film[0]}")
        print(f"Titlu: {film[1]}")
        print(f"An: {film[2]}")
        print(f"Regizor: {film[3]}")
        print("=" * 20)

    # Închid conexiunea la baza de date
    connection.close()

if __name__ == "__main__":
    main()
