from sklearn import datasets, model_selection, metrics
from sklearn.naive_bayes import GaussianNB

import fileReader
from hardCodedClassifier import HardCodedClassifier

iris = datasets.load_iris()

print(iris.data)

print(iris.target)

print(iris.target_names)

train_data_set, test_data_set, train_target_set, test_target_set = model_selection.train_test_split(iris.data,
                                                                                                    iris.target,
                                                                                                    shuffle=True,
                                                                                                    train_size=0.3)

classifier = GaussianNB()
classifier.fit(train_data_set, train_target_set)
prediction_result = classifier.predict(test_data_set)

print("Accuracy:", metrics.accuracy_score(test_target_set, prediction_result))

# Here starts the HardCoded Classifier

my_classifier = HardCodedClassifier()

my_classifier.fit(train_data_set, train_target_set)

my_result = my_classifier.predict(test_data_set)

print("Hard Coded Accuracy:", metrics.accuracy_score(test_target_set, my_result))

# Reading the Dataset from a csv

csv_dataset, csv_target = fileReader.read_data_set("iris_dataset.csv")

csv_train_data_set, csv_test_data_set, csv_train_target_set, csv_test_target_set = model_selection.train_test_split(
    csv_dataset,
    csv_target,
    shuffle=True,
    train_size=0.3)

classifier.fit(csv_train_data_set, csv_train_target_set)
csv_prediction_result = classifier.predict(csv_test_data_set)
print("CSV Accuracy:", metrics.accuracy_score(csv_test_target_set, csv_prediction_result))
