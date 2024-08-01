# Highlight to Quiz

**Highlight to Quiz** is a Streamlit-based web application that transforms highlighted text from PDF documents into interactive multiple-choice quiz questions. This tool is particularly useful for educators, students, and anyone interested in testing their knowledge on specific topics highlighted in documents.

## Features

- **PDF Upload**: Upload a PDF file to extract highlighted text.
- **Automated Quiz Generation**: The app uses Natural Language Processing (NLP) techniques to analyze the highlighted text and generate quiz questions, complete with multiple-choice options.
- **Interactive Quiz**: Users can participate in the quiz directly within the app, with instant feedback on their answers.
- **Focus on Computer Science**: The quiz questions are specifically geared towards computer science topics, making it ideal for students and professionals in this field.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for building interactive web applications.
- **PyMuPDF (fitz)**: Library for extracting highlighted text from PDF files.
- **NLTK**: Natural Language Toolkit for processing and analyzing text.
- **Pandas**: Data manipulation and analysis.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/highlight-to-quiz.git
2. **Install the requirement**:
   pip install -r requirements.txt

3. **Run the application**:
   streamlit run app.py
