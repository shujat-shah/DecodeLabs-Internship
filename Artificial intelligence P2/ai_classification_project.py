import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target


print("\n========= DATASET INFORMATION =========")
print(X.head())

print("\n========= TARGET LABELS =========")
print(iris.target_names)

print("\n========= DATASET SHAPE =========")
print(X.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))


model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")


predictions = model.predict(X_test)

print("\n========= PREDICTIONS =========")
print(predictions)


accuracy = accuracy_score(y_test, predictions)

print("\n========= MODEL ACCURACY =========")
print(f"Accuracy: {accuracy * 100:.2f}%")


print("\n========= CLASSIFICATION REPORT =========")
print(classification_report(y_test, predictions))


cm = confusion_matrix(y_test, predictions)

print("\n========= CONFUSION MATRIX =========")
print(cm)

plt.figure(figsize=(8, 5))

plt.scatter(
    X['sepal length (cm)'],
    X['petal length (cm)'],
    c=y,
)

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Iris Dataset Visualization')

plt.show()


sample_data = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample_data)

print("\n========= CUSTOM PREDICTION =========")
print("Predicted Flower:", iris.target_names[prediction][0])

