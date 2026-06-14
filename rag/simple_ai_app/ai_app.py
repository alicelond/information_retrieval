# Adding the libraries
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
# Generate web UI
import gradio as gr

# Adding API keys with dot env, keep .env in .gitignore
import os
from dotenv import load_dotenv 
load_dotenv()

# Adding a prompt template
prompt_template_str = """
Your task is to explain the concept of **{concept}** to me in a way that is:

1. Clear and intuitive
2. Concise (in under 100 words)
3. Tailored specifically to me and what I already know

Use the following information about me to personalize your explanations:

- Role: Software Engineer working on RAG systems and chatbot integration
- Background: Python proficiency, AI fundamentals (search methods, deep learning, ML)
- Current Project: Building RAG with MCP server integration
- Interests: Document ingestion, conversation management, hybrid search architectures, evaluation metrics

The personalization should be subtle and natural. Avoid forced references that don't genuinely enhance understanding.
"""

# Create a prompt template object
prompt_template = PromptTemplate.from_template(prompt_template_str)

# Create model interface
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Create explanation from model
def generate_explanation(input_text: str) -> str:
  # Call the model with the prompt
  response = model.invoke(prompt_template.format(concept=input_text))

  return response.content

demo = gr.Interface(
    fn=generate_explanation,
    inputs=[gr.Textbox(label="Enter a concept", lines=1)],
    outputs=[gr.Textbox(label="Explanation", lines=5)],
    flagging_mode="never",
    title="AI Concept Explainer",
    description="Get personalized explanations for any technical concept"
)

demo.launch()
