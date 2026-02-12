Student Performance Prediction System using Machine Learning

This project is an AI-based system that predicts student academic performance using machine learning techniques. The model analyzes various academic and behavioral factors such as study time, internal marks, health status, and attendance to estimate the final marks of a student. The trained model is deployed using a Streamlit web application for easy and interactive usage.

Problem Statement

Predicting student performance manually is challenging and often inaccurate. Educational institutions require an intelligent system that can analyze student data and predict academic outcomes in advance. This helps in identifying weak students early and taking necessary actions to improve their performance.

Proposed Solution

The proposed system uses a supervised machine learning algorithm (Linear Regression) to predict student final marks. The system is trained on a real-world dataset and deployed using a web interface. Users can enter student-related parameters and instantly get predicted results.

Technologies Used

Python  
Pandas  
NumPy  
Scikit-learn  
Streamlit  
Joblib  

Dataset

The dataset is taken from Kaggle (Student Performance Dataset) and contains student academic and personal attributes. Only numerical features are selected for training the model to ensure simplicity and efficiency.

Machine Learning Model

Algorithm Used: Linear Regression

Input Features:
Study Time  
Past Failures  
Family Relationship  
Free Time  
Going Out  
Workday Alcohol Consumption  
Weekend Alcohol Consumption  
Health  
Absences  
First Internal Marks (G1)  
Second Internal Marks (G2)  

Target Variable:
Final Marks (G3)

How to Run the Project

1. Download or clone the repository.
2. Install required libraries:
pip install pandas numpy scikit-learn streamlit joblib

3. Train the model:
python train_model.py

4. Run the Streamlit app:
streamlit run app.py

Output

The system provides predicted final marks based on user inputs through a simple and interactive web interface.

Future Scope

The system can be improved by using advanced algorithms like Random Forest and Neural Networks. More features such as attendance percentage, learning behavior, and psychological factors can be added. The system can also be deployed on cloud platforms like Microsoft Azure.

Author

Bharath Hegde  
BCA Student, Seshadripuram Degree College, Mysore
