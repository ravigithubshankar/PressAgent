import os
import groq
from dotenv import load_dotenv
from AI_review import review_press_kit
from pdf import generate_pdf
from shared_functions import get_user_input,generate_press_kit_content,get_supplementary_data
load_dotenv()
from Midreviews import mid_review

groq_api_key=os.getenv("groq_api_key")
client=groq.Client(api_key=groq_api_key)

def get_user_feedback(prompt):
    feedback = input(prompt).strip().lower()
    return feedback

def main():
    user_input=get_user_input()

    print("\n 🚀 Proceeding with the following information:")
    print(user_input)
    #tone=user_input.get("tone","Professional")
    supplementary_data=get_supplementary_data(user_input["press_kit_topic"])
    print("\n 🌟 Supplementary Data:")
    for data in supplementary_data:
        print(f" ✨ - {data}")

    include_data=get_user_feedback(" 📌 Do you want to include this supplementary data in the press kit ? (Y/N):")
    if include_data=="y":
        user_input["supplementary_data"]=supplementary_data
    else:
        user_input["supplementary_data"]=[]

    
    

    press_kit_content=generate_press_kit_content(user_input)
    print("\n 📄 Generated press kit conference")
    print(press_kit_content)

    press_kit_content=mid_review(press_kit_content,"Press Kit Content")
    if not press_kit_content:
        print(" ❌ Press kit generation cancelled by user.")
        return
    
    print("\n🔧 [Final Configuration Confirmation]")
    print("📚 [Final Structure Preview]")
    print("1️⃣ Press Release (Draft)")
    print("2️⃣ Company Overview")
    print("3️⃣ PR Message")
    print("4️⃣ Email Draft")
    print("5️⃣ Supplementary Materials (if applicable)")
    final_configuration = get_user_feedback("✅ Do you confirm this final configuration? (Y/N): ")
    

    print("\n🔍 [Quality Review Phase]")
    review = review_press_kit(press_kit_content)
    print("\n📊  [Quality Review Report]")
    print(f"1️⃣  Content Consistency: {review.get('content_consistency', 'N/A')}/10 🧩")
    print(f"2️⃣  Writing Style and Tone: {review.get('writing_style', 'N/A')}/10 🖋️")
    print(f"3️⃣  Layout and Structure: {review.get('layout_structure', 'N/A')}/10 🗂️")
    print(f"4️⃣  SEO Optimization: {review.get('seo_optimization', 'N/A')}/10 🌐")
    print("📝  Overall Feedback:")
    print(review.get("overall_feedback", "No feedback provided."))
   # print("\Quality Review Report:")
    #print(f"Score:{review['score']}/10")
    #print("FeedBack:")

    for fb in review["feedback"]:
        print(f"📌 - {fb}")





    final_feedback=get_user_feedback(" 👍 Do you approve the final press kit? (Y/N):")
    if final_feedback=="y":
        generate_pdf(press_kit_content)
        print("\n ✅ Press kit has been generated as 'press_kit.pdf'.🎉")
    else:
        print("Press kit generation cancelled by user.")
if __name__ == "__main__":
    main()



