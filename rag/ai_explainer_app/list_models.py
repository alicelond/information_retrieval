import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file or is empty.")
else:
    try:
        genai.configure(api_key=api_key)
        print("Successfully configured API key.")
        print("\nModels that support 'generateContent':")
        found_gemini_pro = False
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                print(f"- {m.name}")
                if m.name == "models/gemini-pro":
                    found_gemini_pro = True

        if not found_gemini_pro:
            print("\n'models/gemini-pro' was NOT found among the models supporting 'generateContent'.")
            print("Consider trying 'gemini-1.0-pro' or another listed model if available.")
        else:
            print("\n'models/gemini-pro' was found and supports 'generateContent'.")

    except Exception as e:
        print(f"An error occurred while listing models: {e}")
        print("Please check your GOOGLE_API_KEY and network connection.")
