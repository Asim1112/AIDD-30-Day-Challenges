Role: Senior Python AI Engineer

Objective:
Build a "PDF Study Notes Summarizer & Quiz Generator Agent" using Streamlit and the openai-agents SDK, powered by Gemini CLI + Context7 MCP.

This prompt will instruct the Gemini CLI to generate the full project.

------------------------------------------------------------
1. Project Overview
------------------------------------------------------------

Agent must:

1. Extract text from PDFs
2. Generate clean, structured summaries
3. Generate quizzes from PDF content
4. Allow user to select answers in Streamlit UI
5. Evaluate user's answers and return score + correctness report

Quiz format (MANDATORY):
- Each MCQ contains:
    - question
    - four options: A, B, C, D
    - correct_answer: "A" | "B" | "C" | "D"

The agent MUST return quiz questions in a JSON-safe schema.

UI Framework:
- Streamlit

Tools:
- PyPDF
- openai-agents
- Context7 MCP
- dotenv for keys

------------------------------------------------------------
2. Critical Technical Constraints
------------------------------------------------------------

1. Zero-Bloat Protocol:
- Only functions described
- Only SDK-documented patterns
- No extra helpers
- No hallucinated features

2. API Requirements:
- Library: openai-agents
- Base URL:
  https://generativelanguage.googleapis.com/v1beta/openai/
- Use GEMINI_API_KEY from .env
- Model: OpenaiChatCompletionModel with Gemini model

3. SDK Rules:
- Correct tool registration
- Correct agent initialization
- Correct sync/async style
- Tool schemas exactly follow docs

4. Error Protocol:
On SyntaxError / AttributeError / ImportError:
- STOP immediately
- Re-run get-library-docs
- Fix only after doc verification

------------------------------------------------------------
3. Architecture & File Structure
------------------------------------------------------------

.
├── .env
├── extract.py
├── agent.py
├── app.py
└── pyproject.toml

------------------------------------------------------------
4. Implementation Steps
------------------------------------------------------------

Step 1 — SDK Documentation Verification
- Run: get-library-docs for openai-agents
- Study:
    • tool decorator format
    • agent creation
    • model usage
    • tool invocation schema
    • correct function signatures

Step 2 — extract.py
Create EXACTLY TWO functions:

1. extract_text_from_pdf(file_path: str)
   - Use PyPDF
   - Return raw extracted text

2. clean_text(text: str)
   - Remove newlines and extra spaces
   - No advanced NLP

Register both as tools using correct SDK decorator or FunctionTool (as per docs).

Step 3 — agent.py
- Load API key using dotenv
- Initialize OpenaiChatCompletionModel with base_url
- Import and register tools
- System Prompt:

"Summarize uploaded PDFs and generate quizzes strictly from extracted text. MCQs must contain a question, four options (A–D), and correct_answer. Do not invent content. Follow JSON-safe structured output."

Step 4 — app.py (Streamlit UI)

A) PDF Upload Section
- User uploads PDF
- Call extract_text_from_pdf → get text
- Clean the text
- Send to agent → get summary
- Display summary in styled Streamlit container

B) Quiz Generation Section
- Button: “Generate Quiz”
- Send original text to agent
- Receive MCQ list:
    [
        {
            "question": "...",
            "options": { "A": "...", "B": "...", "C": "...", "D": "..." },
            "correct_answer": "B"
        },
        ...
    ]
- Display each question using:
    st.radio("Select your answer", list_of_options)

C) NEW FEATURE: Answer Checking & Results
- After user selects all answers:
    - Button: “Check Answers”
    - Compare selected answers with correct_answer
    - Display:
        - Correct/Incorrect for each question
        - Final Score: X / total
    - Results should be rendered clearly inside Streamlit

No multipage app.  
No streaming.  
No unnecessary state logic.

------------------------------------------------------------
5. Testing Scenarios
------------------------------------------------------------

1. Summary Test  
2. MCQ Generation Test  
3. Answer Checking Test  
4. Incorrect Answer Behavior  
5. Tool Invocation Check:
   Must show:
   [tool call: extract_text_from_pdf]

------------------------------------------------------------
6. CLI Requirement
------------------------------------------------------------

You MUST generate and include a screenshot showing the exact Gemini CLI prompt used:
Save it as:
prompt_screenshot.png
in the project root folder.

------------------------------------------------------------

FINAL INSTRUCTION:
Generate the entire project exactly as described,
following SDK documentation strictly,
with no deviations or extra features.
