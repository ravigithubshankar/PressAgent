from fpdf import FPDF
from shared_functions import get_user_input,generate_press_kit_content
from shared_functions import get_supplementary_data
from AI_review import review_press_kit

def generate_pdf(content, filename="press_kit.pdf"):
    content = (
        content.replace("\u2013", "-")  # Replace en dash with a hyphen
        .replace("\u201c", '"')       # Replace left double quotation mark
        .replace("\u201d", '"')       # Replace right double quotation mark
        .replace("\u2026", "...")     # Replace ellipsis
    )

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
   # pdf.add_font("DejaVu","","")
    pdf.multi_cell(0, 10, content)
    pdf.output(filename)

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

    # Generate PDF
    generate_pdf(press_kit_content)
    print("\nPress Kit has been generated as 'press_kit.pdf'.")

#if __name__ == "__main__":
  #  main()
