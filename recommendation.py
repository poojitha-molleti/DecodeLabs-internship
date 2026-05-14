def recommend_movies():
    print("Welcome Poojitha's Recommendation Engine ")
    print("Type 'exit' anytime to quit\n")

    movies = [
        {"name": "Inception", "genre": "sci-fi"},
        {"name": "Titanic", "genre": "romance"},
        {"name": "Dude", "genre": "love"},
        {"name": "Dhurandhar", "genre": "action"},
        {"name": "Interstellar", "genre": "sci-fi"},
        {"name": "Biker", "genre": "action"},
        {"name": "Mad", "genre": "comedy"},
        {"name": "StrangerThings", "genre": "horror"},
    ]

    while True:
        user_input = input("Enter your favorite genre: ").lower()

        if user_input == "exit":
            print(" Exiting recommendation system. Goodbye!")
            break

        recommendations = []

        for movie in movies:
            if movie["genre"] == user_input:
                recommendations.append(movie["name"])

        if recommendations:
            print("\n Recommended Movies:")
            for m in recommendations:
                print(f"- {m}")
            print()
        else:
            print(" No matches found. Try another genre.\n")

if __name__ == "__main__":
    recommend_movies()