import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
<<<<<<< HEAD
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Importing the dataset
dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter="\t", quoting=3)

# Cleaning the texts
nltk.download("stopwords")
ps = PorterStemmer()
all_stopwords = stopwords.words("english")
all_stopwords.remove("not")
corpus = []

for i in range(0, 1000):
    review = re.sub("[^a-zA-Z]", " ", dataset["Review"][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = " ".join(review)
    corpus.append(review)

# Creating the Bag of Words model
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the Naive Bayes model on the Training set
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred_cols = y_pred[:, np.newaxis]
y_test_cols = y_test[:, np.newaxis]

print(np.concatenate((y_pred_cols, y_test_cols), axis=1))

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))
=======
>>>>>>> b84e731a0d5e6d583032982a1250ec9f678a449b
