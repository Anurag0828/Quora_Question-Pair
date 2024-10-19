# *Quora_Question-Pair Model*

This project implements a machine learning model to detect duplicate questions using natural language processing (NLP) techniques. The model is deployed using Streamlit and hosted on AWS EC2 for a live web application.

## *Table of Contents*
- [Introduction](#introduction)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Virtual Environment](#2-set-up-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Access the Application on AWS EC2](#4-access-the-application-on-aws-ec2)
- [Usage](#usage)
- [Model Information](#model-information)
- [Future Improvements](#future-improvements)
- [License](#license)

## *Introduction*
This project provides a web interface to detect whether two questions are duplicates using machine learning. It uses text-based features and natural language processing methods to analyze question pairs. The model is trained using a dataset from Quora and is deployed on AWS EC2 using Streamlit for real-time predictions.

## *Features*
- A Streamlit web app for predicting duplicate questions.
- Preprocessing of input text data using stopword removal and vectorization.
- Use of a pre-trained machine learning model to predict whether two input questions are duplicates.
- Live deployment on AWS EC2 for easy access.
## *Setup Instructions*

### *1. Clone the Repository*
Clone the GitHub repository to your local machine using the command:

```bash
git clone https://github.com/Anurag0828/Quora_Question-Pair.git
```
### *2. Set Up Virtual Environment*
Navigate to the project directory and create a virtual environment:
```bash
cd Quora_Question-Pair
python3 -m venv myenv
```
On macOS/Linux:
```
source myenv/bin/activate
```
On Windows:
```
myenv\Scripts\activate
```
*Step 3: Install Dependencies*: 
```
pip install -r requirements.txt
```
- *Step 4: Access the Application on AWS EC2*:
- The application  is deployed and hosted on aws EC2 instance. You can access the live application by visiting the following url
- ```
  http://51.20.249.29:8501/
  ```
Usage

1. Enter two questions in the input fields.


2. Click the "Predict" button.


3. The app will display whether the questions are duplicates or not.



The underlying machine learning model is trained on Quora question pairs, and it evaluates the similarity between the input questions using text processing techniques.

Model Information

The model is built using the following components:

Text Vectorization: The CountVectorizer (saved as cv.pkl) converts the input text data into numerical format.

Machine Learning Model: A classification model (saved as model.pkl) is trained to predict whether two questions are duplicates.


The model uses NLP techniques to preprocess the data, including stopword removal (using stopwords.pkl) and feature extraction.

Future Improvements

Implement more advanced NLP techniques, such as TF-IDF, word embeddings (Word2Vec, GloVe), and BERT.

Improve model accuracy by experimenting with different machine learning algorithms.

Add more robust error handling and user input validation to the app.

Explore additional deployment options like containerization with Docker.


License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code with appropriate attribution.

