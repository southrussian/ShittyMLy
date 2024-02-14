# support vector machine

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

data = load_breast_cancer()

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

clf_svc = SVC(kernel='linear', C=3)
clf_svc.fit(x_train, y_train)

clf_knn = KNeighborsClassifier(n_neighbors=3)
clf_knn.fit(x_train, y_train)

print(clf_svc.score(x_test, y_test))
print(clf_knn.score(x_test, y_test))

