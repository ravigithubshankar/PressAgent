import requests
from cli import get_user_input
import os

def get_supplementary_data(topic):
        """
    Fetches supplementary data related to the given topic using SerpAPI.

    Parameters:
    - topic (str): The topic for which supplementary data is required.

    Returns:
    - list: A list of top 3 news titles related to the topic.
    """
    # Example using SerpAPI (you need to sign up and get an API key)
    api_key = os.getenv("SERPAPI_API_KEY")
    url = f"https://serpapi.com/search.json?q={topic}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    # Extract relevant information
    news_results = data.get("news_results", [])
    supplementary_data = [result["title"] for result in news_results[:3]]  # Get top 2 news titles

    return supplementary_data

def main():
    user_input = get_user_input()
    print("\nProceeding with the following information:")
    print(user_input)

    # Collect supplementary data
    supplementary_data = get_supplementary_data(user_input["press_kit_topic"])
    print("\nSupplementary Data:")
    for data in supplementary_data:
        print(f"- {data}")

    include_data = input("Do you want to include this supplementary data in the Press Kit? (Y/N): ")
    if include_data.lower() == 'y':
        user_input["supplementary_data"] = supplementary_data
    else:
        user_input["supplementary_data"] = []

    print("\nFinal User Input:")
    print(user_input)

#if __name__ == "__main__":
 #   main()se
