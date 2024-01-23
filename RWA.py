import wikipedia
import webbrowser
from bs4 import BeautifulSoup

def fetch_random_wikipedia_article():
    """
    Fetch a random Wikipedia article.

    Returns:
    A string containing the title and summary of the random Wikipedia article.
    """
    random_title = wikipedia.random()
    random_page = wikipedia.page(random_title, auto_suggest=False)

    title = random_page.title
    summary = random_page.summary

    return f"{title}\n\n{summary}"

def main():
    print("Welcome to the Random Wikipedia Article Viewer")

    while True:
        article_content = fetch_random_wikipedia_article()

        print(article_content)
        user_response = input("Do you want to read this article? (yes/no): ").lower()

        if user_response == 'no':
            print("Exiting the Random Wikipedia Article Viewer.")
            break
        elif user_response in ['yes', 'y']:
            # Open the article in the default web browser
            webbrowser.open_new_tab(wikipedia.page(article_content.split('\n')[0]).url)
            print("Opening the article in your default web browser.")

if __name__ == "__main__":
    main()
 