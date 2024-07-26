import os
import streamlit as st
import fitz  # PyMuPDF
import pandas as pd
from groq import Groq
import time  # for sleep functionality

def extract_highlighted_text_from_pdf(file):
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    highlighted_texts = []

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        for annot in page.annots():
            if annot.type[0] == 8:  # Highlight annotation
                text = page.get_text("text", clip=annot.rect)
                highlighted_texts.append(text.strip())

    return highlighted_texts

def generate_quiz(highlighted_texts):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    quiz_questions = []
    for text in highlighted_texts:
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": f"Create a quiz question with multiple choices from this text: {text}"}],
                max_tokens=150
            )
            quiz_question = response.choices[0].message.content
            quiz_questions.append(quiz_question)
        except groq.RateLimitError as err:
            # Handle rate limit error
            st.error(f"API rate limit reached. Retrying in {err.wait_time:.2f} seconds...")
            time.sleep(err.wait_time)  # Wait for the specified time before retrying

    return quiz_questions

def main():
    st.set_page_config(page_title="H2Q - Highlighted PDF Quiz", layout="wide")

    st.title("H2Q - Highlighted PDF Quiz")
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file is not None:
        st.success("PDF file uploaded successfully!")
        highlighted_texts = extract_highlighted_text_from_pdf(uploaded_file)
        if highlighted_texts:
            st.header("Highlighted Text")
            for text in highlighted_texts:
                st.write(text)
            st.write("=" * 40)

            st.success("Highlighted text extracted.")
            st.write("Generating MCQ questions...")

            quiz_questions = generate_quiz(highlighted_texts)
            correct_answers = []  # Store correct answers for comparison

            st.header("Generated MCQ Quiz")
            for i, question in enumerate(quiz_questions):
                st.write(f"Q{i+1}: {question}")

                # Generate multiple choice options
                options = ["Option A", "Option B", "Option C", "Option D"]
                choices = st.radio(f"Select your answer for Q{i+1}", options)

                # Store user-selected answer
                user_answer = choices

                # Add logic to determine correct answer from Groq response (if possible)
                # You'll need to understand the Groq response structure for this
                # Placeholder for now - replace with your logic
                correct_answer = "Option B"  # Replace with actual logic
                correct_answers.append(correct_answer)

                if st.button(f"Submit Answer (Q{i+1})", key=f"submit_{i}"):
                    if user_answer == correct_answer:
                        st.success("Correct!")
                    else:
                        st.error(f"Incorrect. The correct answer is: {correct_answer}")

        else:
            st.write("No highlighted text found in the uploaded PDF.")

if __name__ == "__main__":
    main()

