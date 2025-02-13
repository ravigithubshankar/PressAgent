import os
import groq
from dotenv import load_dotenv
import requests


# Load environment variables
load_dotenv()

# Set up Groq API key
groq_api_key = os.getenv("groq_api_key")
client = groq.Client(api_key=groq_api_key)




def get_user_input():
    print("🎉 Welcome to PressAgent!👋")
    company_name = input("Enter company name 🏢 : ")
    press_kit_topic = input("Enter press kit topic 📰 : ")
    target_media = input("Enter target media 🎯📡 : ")
    tone = input("Enter tone (e.g., professional, creative) 🎵✨ : ")
    #language=input("Enter target language (e.g., en for English, es for Spanish, fr for French):")

    # Confirm user input
    print("\nPlease confirm the following information:")
    print(f"Company Name: {company_name}")
    print(f"Press Kit Topic: {press_kit_topic}")
    print(f"Target Media: {target_media}")
    print(f"Tone: {tone}")
   # print(f"Traget Language: {language}")
    confirmation = input("Is the above information correct? (Y/N): ")

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
    Generate press kit content using the Groq API.
    """
    prompt = f"""
Create a detailed and engaging press kit for the company '{user_input['company_name']}' about '{user_input['press_kit_topic']}'.
The press kit should include:
1. A creative and impactful press release draft that highlights key achievements and innovations.
2. A compelling company overview with unique phrasing and vivid descriptions.
3. A tailored PR message for '{user_input['target_media']}' that uses dynamic and fresh language to captivate the audience.
4. A persuasive email draft for outreach.

Ensure the tone is {user_input['tone']} and the language is innovative, engaging, and memorable. Use professional yet imaginative phrasing to make the content stand out. And also specify the company ceo names when ever specifying the content .
also Ensure the content has a clear introduction and conclusion for better structure and Focus on enhancing tone, structure, and SEO for maximum impact.
"""


    try:
        # Use Groq API to generate content
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Use the correct model name as per Groq documentation
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.8,
            top_p=0.9
        )
        print("Response received:", response)  # Debugging the response structure
        return response.choices[0].message.content.strip()
        
    
    except Exception as e:
        print(f"Error generating press kit content: {e}")
        return None

def get_supplementary_data(topic):
    # Example using SerpAPI (you need to sign up and get an API key)
    api_key = os.getenv("SERPAPI_API_KEY")
    url = f"https://serpapi.com/search.json?q={topic}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    # Extract relevant information
    news_results = data.get("news_results", [])
    supplementary_data = [result["title"] for result in news_results[:2]]  # Get top 2 news titles

    return supplementary_data

