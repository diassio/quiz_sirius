import json
import streamlit as st
from loguru import logger

# Load the JSON data
with open('/Users/dias/Documents/Cerebra/quiz/test.json') as f:
    quiz_data = json.load(f)

# Define a function to display the quiz question and options
def display_question(score, current_question):
    # Get the current question data
    question_data = quiz_data['mcq'][current_question]
    logger.info(question_data)
    # Display the question text
    question = question_data["question"]
    answers = question_data["answers"]
    selected = st.radio(label = question, options = [option["option"] for option in answers])
    for answer in answers:
        option_text = answer["option"]
        is_correct = answer["is_correct"]
        if selected == option_text and is_correct:
            st.write("✅ You are correct!")
            score += 1
        elif selected == option_text and not is_correct:
            st.write("❌ Sorry, that is incorrect.")
        # st.write(f"The correct answer is: {option_text}" if is_correct else "")

    return score

# Define the main function to run the quiz
def run_quiz():
    # Initialize variables to store user's score and current question number
    score = 0
    current_question = 0
    
    # Loop through the questions until the user has answered all of them
    while current_question < len(quiz_data['mcq']):
        st.write(f"Question {current_question + 1}")
        score = display_question(score, current_question)
        current_question += 1

    # Display the user's final score
    st.write(f"Your final score is {score} out of {len(quiz_data['mcq'])}!")

# Run the quiz
run_quiz()