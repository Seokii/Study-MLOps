import argparse
import os

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

def train():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', default='/mnt/pv/models/sklearn/iris', type=str)
    args = parser.parse_args()erve-models-pvc

    if not (os.path.isdir(args.model_path)):
        os.makedirs(args.model_path)

    model_file = os.path.join(args.model_path, 'model.joblib')

    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    rf_clf = RandomForestClassifier()
    rf_clf.fit(X, y)
    dump(rf_clf, model_file)

if __name__ == '__main__':
    train()