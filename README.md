# *Duplicate Question Pair Detection Model*

This project implements a machine learning model to detect duplicate questions using natural language processing (NLP) techniques. The model is deployed using Streamlit and hosted on AWS EC2 for a live web application.

## *Table of Contents*
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
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

## *Project Structure*
