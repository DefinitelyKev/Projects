import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


# Feature Scaling
sc_X = StandardScaler()
sc_y = StandardScaler()

X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Training the SVR model on the whole dataset
regressor = SVR(kernel="rbf")
regressor.fit(X, y)

# Predicting a new result
predict_x = regressor.predict(X)
predict_y = sc_y.inverse_transform(predict_x.reshape(-1, 1))

# Visualising the SVR results
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color="red")
plt.plot(sc_X.inverse_transform(X), predict_y, color="blue")
plt.title("SVR regrssion")
plt.xlabel("Postion Level")
plt.ylabel("Salary")
