import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def main():
    df = pd.read_csv('training.csv', delimiter=';')
    df = df[['text', 'country_code']]

    text = df['text'].tolist()
    extractor = TfidfVectorizer(input='content', stop_words='english')
    feats = extractor.fit_transform(text).toarray()

    labels = (df['country_code'] == 'US').astype(int).tolist()

    X_train, X_test, y_train, y_test = train_test_split(feats, labels, test_size=0.3, random_state=42)

    model = GaussianNB()
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(acc)


if __name__ == '__main__':
    main()
