#Quiz Generator from Doc Files
This project aims to create a quiz application using Streamlit, which parses doc files and generates multiple-choice questions for users to answer. The questions are displayed one by one, and the user's score is calculated based on their responses.

##Project Structure
The project consists of the following files:

1. app.py: The main script that runs the quiz application.
2. content.txt: Copy paste content from docx test
3. converter.py: Script that converts content.txt to test.json
4. test.json: A JSON file containing the quiz questions and answers.
5. req.txt: Required libraries for the project
5. Readme.md: The project documentation (you're currently reading it).

##Dependencies

The project relies on the following dependencies:
1. Python 3.8
2. Streamlit: A Python library for building interactive web applications.
3. loguru: A logging library for Python.
4. json: A Python library for working with JSON data.
5. regex: A Python library for text parsing
##Setup and Execution
To run the quiz application, follow these steps:

1. Clone the project repository to your local machine.
`git clone https://github.com/diassio/quiz_sirius.git`
2. Ensure that Python 3.8 is installed on your system.
3. Install the required dependencies by running the following command in your terminal:
'pip install -r req.txt'
4. Modify the file path in the app.py script to point to your desired doc file containing the quiz questions.
5. Open a terminal or command prompt and navigate to the project directory.
6. Run the quiz application by executing the following command:
'python -m streamlit run app.py'
7. The application will start, and you can access it in your web browser at http://localhost:8501.

##Usage

Upon running the application, you will see the first question displayed.
Read the question and choose one of the provided options.
After selecting an option, the application will provide feedback on whether your answer is correct or incorrect.
Proceed to the next question by clicking the "Next" button.
Repeat the process until you have answered all the questions.
Once you have completed the quiz, the application will display your final score.
Customization
To customize the quiz, you can modify the following components:

Quiz Questions: Create or edit a doc file containing the quiz questions and answers. The file should follow a specific format for parsing.
Styling: Adjust the appearance of the quiz application by modifying the Streamlit elements and CSS styles in the main.py script.
Logging: Modify the loguru logger configuration in the app.py script to control the logging behavior according to your needs.
Conclusion
The Quiz Generator from Doc Files project provides a simple way to create interactive quizzes using Streamlit. By parsing doc files, the application generates multiple-choice questions and allows users to test their knowledge. This project can be customized and extended to support various quiz formats and additional features as per specific requirements.