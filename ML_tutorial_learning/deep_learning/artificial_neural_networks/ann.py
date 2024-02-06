import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

import tensorflow.python as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

### Part 1 - Data Preprocessing ###

# Importing the dataset
dataset = pd.read_csv("Churn_Modelling.csv")
X = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

# Label Encoding the "Gender" column
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])

# One Hot Encoding the "Geography" column
transformers = [("encoder", OneHotEncoder(), [1])]
ct = ColumnTransformer(transformers=transformers, remainder="passthrough")
X = np.array(ct.fit_transform(X))


# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### Part 2 - Building the ANN ###

# Initializing the ANN
ann = Sequential()

# Adding the input layer and the first hidden layer
ann.add(Dense(units=6, activation="relu"))

# Adding the second hidden layer
ann.add(Dense(units=6, activation="relu"))

# Adding the output layer
ann.add(Dense(units=1, activation="sigmoid"))

### Part 3 - Training the ANN ###

# Compiling the ANN
ann.compile(optimzer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Training the ANN on the Training set
ann.fit(X_train, y_train)
