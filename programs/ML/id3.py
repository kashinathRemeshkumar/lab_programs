import pandas as pd
from sklearn import datasets 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load the Iris dataset
#iris = pd.read_csv("iris.csv")
#X = iris.drop("species", axis=1)  # Features
#y = iris["species"]  # Target labels

#load dataset from sklearn
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=['target'])


# Split the dataset into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Decision Tree Classifier with the 'entropy' criterion
clf = DecisionTreeClassifier(criterion='entropy') 

# Train the classifier
clf.fit(X_train, y_train)

# Predict on the test data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Classification report
print(classification_report(y_test, y_pred))

# Confusion matrix
print(confusion_matrix(y_test, y_pred))

# Plot the decision tree
plt.figure(figsize=(12, 8))

#plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True) #import csv
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)  #dataset from sklearn

plt.title("Decision Tree Visualization")
plt.show()
