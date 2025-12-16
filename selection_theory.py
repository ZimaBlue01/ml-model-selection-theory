🧠 Machine Learning Model Selection – Theory & Reasoning

This repository focuses on machine learning fundamentals, specifically model selection, loss functions, and algorithm suitability.

The goal is to demonstrate conceptual understanding of machine learning models — not just implementation.

❓ Why Linear Regression Is Not Suitable for Loan Approval

Linear Regression works by learning a linear relationship between input features and a continuous numeric output.
It predicts values on an unbounded scale (−∞ to +∞).

Why this is a problem for loan approval

Loan approval is a classification problem:

Outcome is Yes / No

We need probabilities or class labels, not continuous values

Using Linear Regression for this task can result in:

Predictions outside the valid range (e.g. −0.4 or 1.3)

Poor interpretability for decision-making

No direct probabilistic meaning

✅ More appropriate algorithm

Logistic Regression is better suited because:

It outputs probabilities between 0 and 1

It is designed for binary classification

It is widely used in credit scoring and risk modeling

📊 Parametric vs Non-Parametric Algorithms
Parametric Algorithms

Assume a fixed functional form

Learn a limited number of parameters

Faster and easier to interpret

Example:

Linear Regression

Logistic Regression

Non-Parametric Algorithms

Do not assume a specific data distribution

Model complexity grows with data

More flexible but harder to interpret

Example:

Decision Trees

k-Nearest Neighbors (k-NN)

📐 Mean Squared Error (MSE) Calculation

Given:

X = [40, 65, 90, 150]
Y_actual = [100, 95, 130, 160]


Predicted values:

Y_predicted = [100, 95, 130, 160]


Python Calculation
import numpy as np

y_true = np.array([100, 95, 130, 160])
y_pred = np.array([100, 95, 130, 160])

mse = np.mean((y_true - y_pred) ** 2)
print(mse)

Result
MSE = 1550.0


MSE quantifies how far predictions deviate from actual values, making it a standard evaluation metric for regression models.

🎯 Key Takeaways

Model choice must match the problem type

Regression ≠ Classification

Understanding why an algorithm works is as important as knowing how to implement it

Clear reasoning leads to better, safer ML systems

👤 Author

Muhammed Uwais Adam
Machine Learning Fundamentals | Model Selection | ML Theory
