# AI Explainer App
This folder implements a simple AI Concept Explainer application. It leverages a free model from Hugging Face via a LangChain interface to provide personalized explanations of technical concepts.

## How to use it
To get this application up and running, follow these steps:

### 1. Set up your Environment

This project uses a `.env` file to manage sensitive information like API tokens.

*   **Create a `.env` file**: In the root of this `ai_explainer_app` directory, create a file named `.env`.
*   **Obtain a Hugging Face API Token**:
    1.  Go to huggingface.co and log in or sign up.
    2.  Navigate to your profile settings and then "Access Tokens".
    3.  Create a new token with at least "read" access.
*   **Add the token to your `.env` file**:

    ```
    HUGGINGFACEHUB_API_TOKEN="hf_YOUR_ACTUAL_TOKEN_GOES_HERE"
    ```
    Replace `"hf_YOUR_ACTUAL_TOKEN_GOES_HERE"` with the token you copied from Hugging Face.

### 2. Install Dependencies

Ensure you have all the necessary Python libraries installed. Navigate to this directory in your terminal and run:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Once dependencies are installed and your `.env` is configured, you can launch the Gradio application:

```bash
python3 ai_app.py
```

This will start a local web server, and Gradio will provide a URL (e.g., `http://127.0.0.1:7860`) in your terminal. Open this URL in your web browser to interact with the AI Concept Explainer.

## Model Used

The application currently uses `google/flan-t5-small` from the Hugging Face Inference API for text generation. This model was chosen for its general availability on the free tier and its suitability for explanation tasks.

