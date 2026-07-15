from sklearn.datasets import load_iris
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, classification_report

iris = load_iris()

X = iris.data
y = iris.target

print("Total Samples:", len(X))
print("Number of Dimensions:", X.shape[1])
print("Class Names:", iris.target_names)

X, y = shuffle(X, y, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,shuffle=False,random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)


predictions = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, predictions))

print("\nPrecision:")
print(precision_score(y_test, predictions, average="weighted"))

print("\nF1 Score:")
print(f1_score(y_test, predictions, average="weighted"))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))