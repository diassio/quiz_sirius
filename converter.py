import json
import re

def run_converter(path_to_content: str):
    with open(path_to_content, 'r') as file:
        doc = file.read()
    doc = re.sub('\n+', '\n', doc)
    doc = '\n'.join([' '.join(line.split()) for line in doc.split('\n')])
    # Split the document into sections
    sections = doc.split('#')

    # Remove empty sections
    sections = list(set(filter(lambda x: x.strip() != '', sections)))

    # Create a list to hold the MCQ questions and answers
    mcq = []

    # Process each section
    for section in sections:
        # Split the section into lines
        lines = section.strip().split('*')
        # print(lines)

        # Extract the question
        question = lines[0]+" "+lines[1]
        lines.pop(1)

        # Extract the answers
        answers = [{'option': "", 'is_correct': False}]
        for line in lines[1:]:
            is_correct = False
            if "+" in line:
                is_correct = True
                line = line[1:]
                option = line.strip()
            else:
                line = line
                option = line.strip()
            answers.append({'option': option, 'is_correct': is_correct})

        # Append the question and answers to the MCQ list
        mcq.append({'question': question, 'answers': answers})

    # Create a dictionary to hold the final data
    data = {'title': 'test', 'mcq': mcq}

    # Convert the dictionary to JSON
    json_data = json.dumps(data, indent=4)

    # Write the JSON data to a file
    with open('test.json', 'w') as f:
        f.write(json_data)

if __name__ == "__main__":
    run_converter("/Users/dias/Documents/Cerebra/quiz/content.txt")
