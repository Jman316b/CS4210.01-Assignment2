#-------------------------------------------------------------------------
# AUTHOR: Jeremiah Garcia
# FILENAME: decision_tree_2.py
# SPECIFICATION: Creates a decision tree
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    accuracies = []
    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =

    for i, row in enumerate(dbTraining):
        X.append([])
        for j, column in enumerate(row):
            if j == 4:
                continue

            if column == "Young":
                X[i].append(1)
            elif column == "Prepresbyopic":
                X[i].append(2)
            elif column == "Presbyopic":
                X[i].append(3)
            elif column == "Myope":
                X[i].append(1)
            elif column == "Hypermetrope":
                X[i].append(2)
            elif column == "Yes":
                X[i].append(1)
            elif column == "No":
                X[i].append(2)
            elif column == "Reduced":
                X[i].append(1)
            elif column == "Normal":
                X[i].append(2)
            else:
                X[i].append(0)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    for i, row in enumerate(dbTraining):
        for j, column in enumerate(row):
            if j != 4:
                continue

            if column == "Yes":
                Y.append(1)
            elif column == "No":
                Y.append(2)
            else:
                Y.append(0)

    #loop your training and test tasks 10 times here
    for i in range (10):
        true_pred = 0

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        # dbTest =

        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)


        for index, data in enumerate(dbTest):
            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            XTest = []
            YTest = -1

            for i, column in enumerate(data):
                if i != 4:
                    if column == "Young":
                        XTest.append(1)
                    elif column == "Prepresbyopic":
                        XTest.append(2)
                    elif column == "Presbyopic":
                        XTest.append(3)
                    elif column == "Myope":
                        XTest.append(1)
                    elif column == "Hypermetrope":
                        XTest.append(2)
                    elif column == "Yes":
                        XTest.append(1)
                    elif column == "No":
                        XTest.append(2)
                    elif column == "Reduced":
                        XTest.append(1)
                    elif column == "Normal":
                        XTest.append(2)
                    else:
                        XTest.append(0)
                else:
                    if column == "Yes":
                        YTest = 1
                    elif column == "No":
                        YTest = 2
                    else:
                        YTest = 0

            class_predicted = clf.predict([XTest])[0]

            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if (class_predicted == YTest):
                true_pred = true_pred + 1

        accuracies.append(true_pred / len(X))
    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    accuracy = sum(accuracies)/10

    print('final accuracy when training on ',ds,': ',accuracy, sep="")