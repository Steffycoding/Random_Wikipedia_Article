import wikipedia

def fetch_random_wikipedia_article():
    """
    Fetch a random Wikipedia article.

    Returns:
    A string containing the title and summary of the random Wikipedia article.
    """
    article_title = wikipedia.random()
    article_summary = wikipedia.summary(article_title)

    return f"{article_title}\n\n{article_summary}"

def main():
    print("Welcome to the Random Wikipedia Article Viewer")

    while True:
        article_content = fetch_random_wikipedia_article()

        print(article_content)
        user_response = input("Do you want to read this article? (yes/no): ").lower()

        if user_response != 'yes':
            print("Exiting the Random Wikipedia Article Viewer.")
            break

if __name__ == "__main__":
    main()
