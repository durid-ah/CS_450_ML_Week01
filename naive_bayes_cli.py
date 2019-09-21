from sklearn import model_selection, metrics
from sklearn.naive_bayes import GaussianNB

import fileReader

# This a command line app that pulls in the iris data set from a csv file and runs it through the naive bayes classifier
# After which it tests it and shows the accuracy, then the user can put it in his/her own values and predict what type
# of flower it is.

# Translate the target from numeric value to name
number_to_target = {
                    0: 'setosa',
                    1: 'versicolor',
                    2: 'virginica'
}

print("Reading File...")
csv_dataset, csv_target = fileReader.read_data_set("iris_dataset.csv")

classifier = GaussianNB()

csv_train_data_set, csv_test_data_set, csv_train_target_set, csv_test_target_set = model_selection.train_test_split(
    csv_dataset,
    csv_target,
    shuffle=True,
    train_size=0.3)

print("Training...")
classifier.fit(csv_train_data_set, csv_train_target_set)
csv_prediction_result = classifier.predict(csv_test_data_set)
accuracy = metrics.accuracy_score(csv_test_target_set, csv_prediction_result) * 100
print("Accuracy:", "%.2f" % accuracy, "%")

input_terms = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

while True:
    input_array = []
    for i in input_terms:
        value = input(f'Put in {i}:')
        input_array.append(float(value))

    test_array = [input_array]
    prediction = classifier.predict(test_array)
    print(number_to_target[prediction[0]])
    continue_loop = input("Would you like to input another flower? (y/n)")
    if continue_loop == "n":
        break
