import csv

import numpy as np

target_to_number = {
                    'setosa': 0,
                    'versicolor': 1,
                    'virginica': 2
}


def read_data_set(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data_set = []
        target = []
        count = 0
        for row in csv_reader:
            if count != 0:
                data_set.append(np.array(row[:-1]).astype(np.float))
                target.append(target_to_number[row[-1]])
            count += 1
        return data_set, target
