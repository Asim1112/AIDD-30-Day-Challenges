import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, Agent, AsyncOpenAI
from extract import extract_text_from_pdf, clean_text

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")


external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" 
)


llm_model= OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client = external_client
)

# Define the tools
tool_extract_text_from_pdf = extract_text_from_pdf
tool_clean_text = clean_text

# System Prompt
SYSTEM_PROMPT = (
    "Summarize uploaded PDFs and generate quizzes strictly from extracted text. "
    "MCQs must contain a question, four options (A-D), and correct_answer. "
    "Do not invent content. Follow JSON-safe structured output."
)

# Initialize the Agent
pdf_agent = Agent(
    name = "PDF_Summarizer_and_Quiz_Generator",
    instructions=SYSTEM_PROMPT,
    model=llm_model,
    tools=[tool_extract_text_from_pdf, tool_clean_text],
)

if __name__ == '__main__':
    # This block is for testing the agent setup, not for direct execution
    print("Agent initialized successfully.")
    print(f"Agent system prompt: {pdf_agent.instructions}")
    print(f"Agent tools: {[tool.__name__ for tool in pdf_agent.tools]}")