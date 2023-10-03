#-------------------------------------------------------------------------
# AUTHOR: Jeremiah Garcia
# FILENAME: knn.py
# SPECIFICATION: Executes the KNN function.
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 Hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

false_pred = 0
#loop your data to allow each instance to be your test set
for i, point in enumerate(db):
    passed = False
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    # X =

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    # Y =


    X = []
    Y = []
    for j, p in enumerate(db):
        if j == i:
            passed = True
        else:
            X.append([])
            if passed:
                for k, val in enumerate(p):
                    if k != 2:
                        X[j-1].append(int(val))
                    else:
                        Y.append(val)
            else:
                for k, val in enumerate(p):
                    if k != 2:
                        X[j].append(int(val))
                    else:
                        Y.append(val)

    for j, clas in enumerate(Y):
        if clas == "+":
            Y[j] = 1
        elif clas == "-":
            Y[j] = 2
        else:
            Y[j] = 0

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =

    testSample = [int(point[0]), int(point[1])]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here

    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if point[2] == "+":
        trueLabel = 1
    else:
        trueLabel = 2

    if (class_predicted != trueLabel):
        false_pred = false_pred + 1

#print the error rate
#--> add your Python code here

print("Error Rate:", false_pred/len(db))




