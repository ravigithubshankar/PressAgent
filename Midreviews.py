from shared_functions import get_user_input,get_supplementary_data,generate_press_kit_content
from AI_review import review_press_kit
from pdf import generate_pdf

def mid_review(content, stage_name):

    #user_input=get_user_input()
    #tone=user_input.get("tone","Professional")
    print(f"\n[Content Generation and Mid-Review].")
    print(f"\[Draft Preview - Style 1: Professional Tone]")
    print(f"\n--- {stage_name} Preview ---")
    print(content)
    feedback = input("Do you want to proceed with this content? (Y/N/Modify): ").strip().lower()
    if feedback == "y":
        print("\n[Proceeding with the content.]")
        return content
    elif feedback == "modify":
        modifications = input("Enter your modifications: ")
        print("\n[Content has been modified].")
        return modifications
    else:
        return None
    

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

    # Generate press kit content using Groq
    press_kit_content = generate_press_kit_content(user_input)
    print("\nGenerated Press Kit Content:")
    print(press_kit_content)

    # Mid-review phase for press kit content

    press_kit_content = mid_review(press_kit_content, "Press Kit Content")
    if not press_kit_content:
        print("Press kit generation canceled by user.")
        return

    # Review press kit
    review = review_press_kit(press_kit_content)
    print("\nQuality Review Report:")
    print(f"Score: {review['score']}/2")
    print("Feedback:")
    for fb in review['feedback']:
        print(f"- {fb}")

    # Generate PDF
    generate_pdf(press_kit_content)
    print("\nPress Kit has been generated as 'press_kit.pdf'.")
