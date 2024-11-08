import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,accuracy_score
import seaborn as sb
import matplotlib.pyplot as plt

'''dataset=load_iris()
x=dataset.data
y=dataset.target'''

data=pd.read_csv("iris.csv")
x=data.drop('species',axis=1)
y=data['species']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=4)

Classifier=SVC(kernel="linear")
Classifier.fit(x_train,y_train)
y_pred=Classifier.predict(x_test)

accuracy=accuracy_score(y_test,y_pred)*100
confusion_mat=confusion_matrix(y_test,y_pred)

print("accuracy for SVM is ",accuracy)
print("confusion matrix")
print(confusion_mat)
sb.heatmap(confusion_mat,annot=True,fmt="d",cmap="Reds",xticklabels=np.unique(y_test),yticklabels=np.unique(y_test))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
