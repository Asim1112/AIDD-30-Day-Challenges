import streamlit as st
import json
import os
import re
import asyncio # <--- New import for running async client
from extract import extract_text_from_pdf, clean_text
from agent import pdf_agent, SYSTEM_PROMPT, external_client

st.set_page_config(page_title="PDF Study Notes Summarizer & Quiz Generator", layout="centered")
st.title("PDF Study Notes Summarizer & Quiz Generator")

# Session State
if "summary" not in st.session_state:
    st.session_state.summary = None
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "quiz_checked" not in st.session_state:
    st.session_state.quiz_checked = False
if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None
if "cleaned_text_for_quiz" not in st.session_state:
    st.session_state.cleaned_text_for_quiz = None

# Safe JSON Extractor
def _extract_json_from_text(text: str):
    text = text.strip()
    try:
        return json.loads(text)
    except:
        match = re.search(r"(\[.*\]|\{.*\})", text, re.DOTALL)
        if not match:
            raise ValueError("No valid JSON detected.")
        return json.loads(match.group(1))

# Upload PDF
st.header("1. Upload PDF")
uploaded_file = st.file_uploader("Choose PDF", type="pdf")

if uploaded_file and st.session_state.uploaded_file_name != uploaded_file.name:
    st.session_state.uploaded_file_name = uploaded_file.name
    st.session_state.summary = None
    st.session_state.quiz_data = None
    st.session_state.user_answers = {}
    st.session_state.quiz_checked = False
    st.session_state.cleaned_text_for_quiz = None

    temp_pdf = "temp.pdf"
    with open(temp_pdf, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing PDF..."):
        try:
            raw = extract_text_from_pdf(temp_pdf)
            st.write("**[tool call: extract_text_from_pdf]**")  # marker for your tests
            cleaned = clean_text(raw)
            st.session_state.cleaned_text_for_quiz = cleaned

            # Call LLM for summary - FIXED: Using asyncio.run()
            summary_res = asyncio.run(
                external_client.chat.completions.create(
                    model="gemini-2.5-flash",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": f"Summarize the following text into clean study notes:\n\n{cleaned}"}
                    ]
                )
            )
            st.session_state.summary = summary_res.choices[0].message.content
            st.success("Summary Ready!")
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            if os.path.exists(temp_pdf):
                os.remove(temp_pdf)

# Show Summary
if st.session_state.summary:
    st.subheader("Summary")
    st.info(st.session_state.summary)

# Generate Quiz
st.header("2. Generate Quiz")
if st.session_state.cleaned_text_for_quiz:
    if st.button("Generate Quiz"):
        with st.spinner("Generating Quiz..."):
            try:
                # Call LLM for quiz - FIXED: Using asyncio.run()
                quiz_res = asyncio.run(
                    external_client.chat.completions.create(
                        model="gemini-2.5-flash",
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": f"Generate 5 MCQs in STRICT JSON array from this text:\n\n{st.session_state.cleaned_text_for_quiz}"}
                        ]
                    )
                )
                quiz_text = quiz_res.choices[0].message.content
                quiz = _extract_json_from_text(quiz_text)

                if not isinstance(quiz, list):
                    raise ValueError("Quiz must be a JSON list.")

                # Validate MCQ schema
                for i, q in enumerate(quiz):
                    if not q.get("question") or not isinstance(q.get("options"), dict) or q.get("correct_answer") not in ["A","B","C","D"]:
                        raise ValueError(f"Invalid MCQ format at index {i}")
                
                st.session_state.quiz_data = quiz
                st.success("Quiz Ready!")
            except Exception as e:
                st.error(f"Quiz Error: {e}")

# Render Quiz + Answer Checking
if st.session_state.quiz_data:
    quiz = st.session_state.quiz_data
    st.subheader("Quiz Questions")

    for i, q in enumerate(quiz):
        st.markdown(f"**Q{i+1}. {q['question']}**")
        labels = [f"A. {q['options']['A']}", f"B. {q['options']['B']}", f"C. {q['options']['C']}", f"D. {q['options']['D']}"]
        ans = st.radio("Your Answer:", labels, key=f"mcq_{i}")
        st.session_state.user_answers[str(i)] = ans.split(".")[0]

    st.markdown("---")
    if st.button("Check Answers"):
        score = 0
        report = []

        for i, q in enumerate(quiz):
            correct = q["correct_answer"]
            user = st.session_state.user_answers.get(str(i))
            is_ok = user == correct
            if is_ok:
                score += 1
            report.append({"q": q["question"], "your": user, "correct": correct, "status": "✅" if is_ok else "❌"})

        st.session_state.quiz_checked = True

        st.subheader("Report")
        for r in report:
            st.write(f"{r['status']} {r['q']}")
            st.write(f"- You: {r['your']} | Correct: {r['correct']}")
            st.write("---")

        st.success(f"Final Score: {score} / {len(quiz)}")