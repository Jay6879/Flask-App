from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = Flask(__name__)

import os
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = "Phanidhar Sai Sravan Chandana, a Master of Science in Computer Science candidate at San Jose State University (expected Dec 2024, GPA 4.00/4.00), has developed a deep expertise in Databases, Distributed Systems, Web Development, Machine Learning, and Parallel Programming. He holds a Bachelor of Technology in Computer Science from Amrita Vishwa Vidyapeetham (GPA 3.50/4.00) and has hands-on experience in multiple programming languages including Java, JavaScript, Python, C, C++, Typescript, SQL, and R, with proficiency in web development frameworks like ExpressJS, React, REST APIs, Spring Boot, and NodeJS. Phanidhar has worked extensively with databases and cloud technologies such as MongoDB, MySQL, Docker, and AWS. During his Software Development Engineer Internship at Informatica, he contributed to a conversation session management service using Java, Spring Boot, MongoDB, WebSockets, Redis, and Kafka, handling over 100,000 sessions daily, optimizing API efficiency with GraphQL and caching mechanisms, and achieving a 50% reduction in latency. As a Software Engineer at Informatica, he developed scalable applications using Java, Spring Boot, and MySQL, improving data migration efficiency by 70%, and refactored codebases to improve performance by 50%, while also engineering CI/CD pipelines using Jenkins. His academic projects include an NLP-based user authentication system with 91% accuracy utilizing BERT and RNN models, and a movie booking web application built using NodeJS, React, MongoDB, and Redis. He has been recognized with the Think Customer First INFA Star Award, published a paper on detecting malicious URLs in Twitter (IEEE, ICSES 2021), and earned a CodeChef DSA certification."
    user_message = user_message +" Now, answer the below question based on the details provided"
    question = request.json['message']
    user_message = user_message + " " + question

    try:
        # Call OpenAI's ChatCompletion endpoint for GPT-3.5/4
        response = openai.chat.completions.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if you're using GPT-3.5
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150
        )

        bot_message = response.choices[0].message.content
        # print(response.choices[0].message.content)

        return jsonify({'message': bot_message})

    except Exception as e:
        return jsonify({'message': 'Error: ' + str(e)})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']

#     try:
#         # Call OpenAI's ChatCompletion endpoint for GPT-3.5/4
#         response = openai.completions.create(
#             model="gpt-4",  # Replace with your model ID, like 'gpt-4' or 'gpt-3.5-turbo'
#             prompt=user_message,
#             max_tokens=150,
#             n=1,
#             stop=None,
#             temperature=0.7
#         )

#         # The correct way to access the response message
#         bot_message = response.choices[0].message['content']

#         return jsonify({'message': bot_message})

#     except Exception as e:
#         return jsonify({'message': 'Error: ' + str(e)})


if __name__ == '__main__':
    app.run(debug=True)
