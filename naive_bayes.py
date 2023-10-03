#-------------------------------------------------------------------------
# AUTHOR: Jeremiah Garcia
# FILENAME: naive_bayes.py
# SPECIFICATION: Executes the Naive Bayes function
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here

dbTraining = []

with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTraining.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =

X = []
Y = []
for i, day in enumerate(dbTraining):
    X.append([])
    for j, val in enumerate(day):
        if j != 0 and j != 5:
            if val == "Sunny":
                X[i].append(1)
            elif val == "Overcast":
                X[i].append(2)
            elif val == "Rain":
                X[i].append(3)
            elif val == "Hot":
                X[i].append(1)
            elif val == "Mild":
                X[i].append(2)
            elif val == "Cool":
                X[i].append(3)
            elif val == "High":
                X[i].append(1)
            elif val == "Normal":
                X[i].append(2)
            elif val == "Weak":
                X[i].append(1)
            elif val == "Strong":
                X[i].append(2)
        elif j == 5:
            if val == "Yes":
                Y.append(1)
            elif val == "No":
                Y.append(2)


#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here

#printing the header os the solution
#--> add your Python code here

dbTest = []

with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)
        else:
            print(f"{row[0]} {row[1]:8} {row[2]:11} {row[3]:8} {row[4]:6} {row[5]:10} Confidence")

XTest = []
for i, day in enumerate(dbTest):
    XTest.append([])
    for j, val in enumerate(day):
        if j != 0 and j != 5:
            if val == "Sunny":
                XTest[i].append(1)
            elif val == "Overcast":
                XTest[i].append(2)
            elif val == "Rain":
                XTest[i].append(3)
            elif val == "Hot":
                XTest[i].append(1)
            elif val == "Mild":
                XTest[i].append(2)
            elif val == "Cool":
                XTest[i].append(3)
            elif val == "High":
                XTest[i].append(1)
            elif val == "Normal":
                XTest[i].append(2)
            elif val == "Weak":
                XTest[i].append(1)
            elif val == "Strong":
                XTest[i].append(2)
        elif j == 5:
            if val == "Yes":
                Y.append(1)
            elif val == "No":
                Y.append(2)

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here

for i, test in enumerate(XTest):
    class_predicted = clf.predict_proba([test])[0]
    if class_predicted[0] >= 0.75:
        print(f"{dbTest[i][0]} {dbTest[i][1]:8} {dbTest[i][2]:11} {dbTest[i][3]:8} {dbTest[i][4]:6} {'Yes':10} {class_predicted[0]:.2}")
    elif class_predicted[1] >= 0.75:
        print(f"{dbTest[i][0]} {dbTest[i][1]:8} {dbTest[i][2]:11} {dbTest[i][3]:8} {dbTest[i][4]:4} {'No':10} {class_predicted[1]:.2}")