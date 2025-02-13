import os
import groq
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Initialize Groq API client using the API key from the environment variables
groq_api_key = os.getenv("groq_api_key")
client = groq.Client(api_key=groq_api_key)

def get_user_input():
    """
    Collects user input for press kit creation.
    Prompts the user to input key details like company name, topic, target media, and tone.
    Returns a dictionary with the collected data.
    """
    print("🎉 Welcome to PressAgent! 👋")
    company_name = input("Enter company name 🏢 : ")
    press_kit_topic = input("Enter press kit topic 📰 : ")
    target_media = input("Enter target media 🎯📡 : ")
    tone = input("Enter tone (e.g., professional, creative) 🎵✨ : ")

    # Display the collected information for confirmation
    print("\nPlease confirm the following information:")
    print(f"Company Name: {company_name}")
    print(f"Press Kit Topic: {press_kit_topic}")
    print(f"Target Media: {target_media}")
    print(f"Tone: {tone}")
    confirmation = input("Is the above information correct? (Y/N): ")

    # If confirmed, return the information; otherwise, restart the input process
    if confirmation.lower() == 'y':
        return {
            "company_name": company_name,
            "press_kit_topic": press_kit_topic,
            "target_media": target_media,
            "tone": tone
        }
    else:
        print("Please re-enter the information.")
        return get_user_input()

def generate_press_kit_content(user_input):
    """
    Generates press kit content using the Groq API based on the user input.
    The press kit includes a press release, company overview, tailored PR message, and an outreach email draft.
    
    Parameters:
    - user_input (dict): A dictionary containing details like company name, topic, target media, and tone.

    Returns:
    - str: Generated press kit content as a string, or None if an error occurs.
    """
    # Construct the prompt for the Groq API
    prompt = f"""
Create a detailed and engaging press kit for the company '{user_input['company_name']}' about '{user_input['press_kit_topic']}'.
The press kit should include:
1. A creative and impactful press release draft that highlights key achievements and innovations.
2. A compelling company overview with unique phrasing and vivid descriptions.
3. A tailored PR message for '{user_input['target_media']}' that uses dynamic and fresh language to captivate the audience.
4. A persuasive email draft for outreach.

Ensure the tone is {user_input['tone']} and the language is innovative, engaging, and memorable. Use professional yet imaginative phrasing to make the content stand out. Include the company CEO's name whenever relevant.
Also, ensure the content has a clear introduction and conclusion for better structure and focus on enhancing tone, structure, and SEO for maximum impact.
"""

    try:
        # Use the Groq API to generate the press kit content
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Specify the model as per Groq's documentation
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.8,
            top_p=0.9
        )
        # Extract and return the generated content from the API response
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating press kit content: {e}")
        return None

def get_supplementary_data(topic):
    """
    Fetches supplementary data related to the given topic using the SerpAPI.

    Parameters:
    - topic (str): The topic for which supplementary data is required.

    Returns:
    - list: A list of top news titles related to the topic.
    """
    # Fetch the SerpAPI key from environment variables
    api_key = os.getenv("SERPAPI_API_KEY")
    url = f"https://serpapi.com/search.json?q={topic}&api_key={api_key}"

    try:
        # Make a GET request to the SerpAPI for news search results
        response = requests.get(url)
        data = response.json()

        # Extract the top 2 news titles from the response
        news_results = data.get("news_results", [])
        supplementary_data = [result["title"] for result in news_results[:2]]

        return supplementary_data
    except Exception as e:
        print(f"Error fetching supplementary data: {e}")
        return []
