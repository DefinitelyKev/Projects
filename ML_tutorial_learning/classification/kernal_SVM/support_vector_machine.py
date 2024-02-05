import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score

dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the SVM model on the Training set
classifier = SVC(kernel="rbf", random_state=0)
classifier.fit(X_train, y_train)

# Predicting a new result
print(classifier.predict(sc.transform([[30, 87000]])))

y_pred = classifier.predict(X_test)

y_pred_cols = y_pred[:, np.newaxis]
y_test_cols = y_test[:, np.newaxis]

print(np.concatenate((y_pred_cols, y_test_cols), axis=1))

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

# Visualising the Training set results
# X_set, y_set = sc.inverse_transform(X_train), y_train
# X1, X2 = np.meshgrid(
#     np.arange(start=X_set[:, 0].min() - 10, stop=X_set[:, 0].max() + 10, step=0.25),
#     np.arange(start=X_set[:, 1].min() - 1000, stop=X_set[:, 1].max() + 1000, step=0.25),
# )
# plt.contourf(
#     X1,
#     X2,
#     classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(
#         X1.shape
#     ),
#     alpha=0.75,
#     cmap=ListedColormap(("salmon", "dodgerblue")),
# )
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(
#         X_set[y_set == j, 0],
#         X_set[y_set == j, 1],
#         c=ListedColormap(("salmon", "dodgerblue"))(i),
#         label=j,
#     )
# plt.title("SVM (Training set)")
# plt.xlabel("Age")
# plt.ylabel("Estimated Salary")
# plt.legend()
# plt.show()

# # Visualising the Test set results
# X_set, y_set = sc.inverse_transform(X_test), y_test
# X1, X2 = np.meshgrid(
#     np.arange(start=X_set[:, 0].min() - 10, stop=X_set[:, 0].max() + 10, step=0.25),
#     np.arange(start=X_set[:, 1].min() - 1000, stop=X_set[:, 1].max() + 1000, step=0.25),
# )
# plt.contourf(
#     X1,
#     X2,
#     classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(
#         X1.shape
#     ),
#     alpha=0.75,
#     cmap=ListedColormap(("salmon", "dodgerblue")),
# )
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(
#         X_set[y_set == j, 0],
#         X_set[y_set == j, 1],
#         c=ListedColormap(("salmon", "dodgerblue"))(i),
#         label=j,
#     )
# plt.title("SVM (Test set)")
# plt.xlabel("Age")
# plt.ylabel("Estimated Salary")
# plt.legend()
# plt.show()
