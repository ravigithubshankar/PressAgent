# 🚀 PressAgent

Automated Press Kit Generation and Quality Review AI Agent

PressAgent is your go-to AI-powered tool for generating professional, engaging, and SEO-optimized press kits with ease! It also integrates a robust quality review system for perfecting your content.

# 🌟 Features

 ✅ Automated Press Kit Generation: Includes press releases, company overviews, PR messages, and email drafts 📝.
 
 ✅ Multilingual Support: Generate content in multiple languages for global reach 🌍.
 
 ✅ Quality Review Phase: Includes detailed reviews for content consistency, tone, structure, and SEO optimization 📈.
 
 ✅ Supplementary Data Integration: Option to include additional data for enriching the press kit 📚 .
 
 ✅ PDF Generation: Final press kits are exported as professional PDFs 🧑‍💻 .


# 🛠️ Installation

## Clone the Repository

    git clone https://github.com/ravigithubshankar/PressAgent.git  
    cd PressAgent  
    
## Set Up Dependencies

    pip install -r requirements.txt  
    
## Configure Environment Variables
### Create a .env file and add your API keys:
    groq_api_key=YOUR_GROQ_API_KEY  
    SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY  

# ⚡ Execution Steps

## 1. Run the Main Script
    python cli.py  
    
2.Follow Interactive Prompts

* Enter your company name, press kit topic, target media, and tone 🎤.
* Confirm the information ✅.
* Optionally include supplementary data 📂.

3. Review and Approve

* Evaluate the draft with the mid-review option 🔄.
* Approve the final configuration ✍️.

4. Quality Review Phase

* View content consistency, tone, layout, and SEO scores 📊.
* Modify based on AI feedback if needed 💡.

5. Generate the Final PDF
* Approve and save your press kit in PDF format 📄.

# 📦 Usage
## 1. Interactive Mode:

* 🚦 Launch the CLI and follow step-by-step prompts to generate a customized press kit.

## 2.Press Kit Components:
* 📝 Provide details like the company name, press kit topic, and tone.
* 🔄 Review and refine sections such as:
  * 📜 Press Release (Draft)
  *  🏢 Company Overview
  *  ✉️ PR Message
  *  📧 Email Draft
  * 📂 Supplementary Materials

## 3.Language Support:
* 🌐 Generate press kits in multiple languages by specifying your preferred language during the prompt phase.

## 4.Feedback Integration:
* 🧑‍💻 Utilize mid-review and quality review phases to incorporate changes and ensure high-quality content.

## 5.Export Options:
*📤 Approve the final press kit and export it as a polished PDF for immediate use.

# 🧰 APIs and Libraries Used
## Core Functionality
* ### 🤖 Groq API: Generates AI-powered content for the press kit.
* ### 📰 SerpAPI: Fetches supplementary data for additional context.
  
## Python Libraries:
* 🛠️ dotenv: Manages environment variables.
* 🌐 requests: Handles API requests.
* 🌍 googletrans: Translates content into multiple languages.
* 🖨️ reportlab: Creates professional PDFs.
* 💻 typer: Simplifies CLI interactions.
  
## Custom Modules:
* 🧪 AI_review.py: Implements content quality checks and feedback.
* 📄 pdf.py: Handles PDF generation.
* 🔧 shared_functions.py: Provides reusable utilities like user input handling and content generation.
* 📝 Midreviews.py: Facilitates mid-review of generated content.

### Generated pdf is uploaded have a look !
# 🤝 Contribution
We welcome contributions! Submit issues, feature requests, or pull requests directly to the repository.
