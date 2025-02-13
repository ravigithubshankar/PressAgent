from shared_functions import get_user_input,generate_press_kit_content
from shared_functions import get_supplementary_data

def review_press_kit(content):
      """
    Reviews the quality of the press kit content based on predefined criteria.

    Parameters:
    - content (str): The press kit content to review.

    Returns:
    - dict: A dictionary containing scores, feedback, and overall evaluation.
    """
    # Simple review based on length and keywords
    score = 0
    feedback = []

    if len(content) > 800:
        score += 2
    elif len(content)>500:
        score+=1
    else:
        feedback.append("Content is too short. Consider adding more details.")

    # 2. writing style and tone

    if "innovative" in content.lower() or "groundbreaking" in content.lower():
        score += 2
    elif "creative" in content.lower():
        score+=1
    else:
        feedback.append("Consider adding more compelling and creative  language to enhance appeal.")

    # 3. Layout and Structure
    if "introduction" in content.lower() and "conclusion" in content.lower():
        score+=2
    else:
        feedback.append("Ensure the content has a clear introduction and conclusion  for better structure.")

    #4. SEO Optimization
    important_keywords = ["innovation", "market leader", "cutting-edge", "strategy"]
    keyword_count = sum(content.lower().count(keyword) for keyword in important_keywords)
    if keyword_count >= 3:
        score += 2
    elif keyword_count > 0:
        score += 1
    else:
        feedback.append("Consider incorporating SEO-friendly keywords for better online visibility.")

    # Overall feedback summary
    overall_feedback = (
        "The press kit is strong overall, but there is room for improvement. "
        "Focus on enhancing tone, structure, and SEO for maximum impact."
        if feedback else "The press kit is excellent in all evaluated aspects."
        )
    return {
        "content_consistency": score if score >= 2 else "Needs Improvement",
        "writing_style": score if score >= 2 else "Average",
        "layout_structure": score if score >= 2 else "Good",
        "seo_optimization": score if score >= 2 else "Minimal",
        "overall_feedback": overall_feedback,
        "score": score,
        "feedback": feedback,
        }


    
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

    # Generate press kit content
    press_kit_content = generate_press_kit_content(user_input)
    print("\nGenerated Press Kit Content:")
    print(press_kit_content)

    # Review press kit
    review = review_press_kit(press_kit_content)
    print("\nQuality Review Report:")
    print(f"Score: {review['score']}/2")
    print("Feedback:")
    for fb in review['feedback']:
        print(f"- {fb}")

#if __name__ == "__main__":
 #   main()

