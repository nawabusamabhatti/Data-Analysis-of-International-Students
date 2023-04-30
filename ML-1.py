import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load the given data
data = {'Sex': ['Female', 'Female', 'Female', 'Male', 'Male', 'Male', 'Other', 'Other', 'Other'],
        'Age': [20, 21, 25, 20, 24, 29, 20, 24, 29],
        'Disability': ['Known disability', 'Known disability', 'Known disability', 'No known disability', 'No known disability', 'No known disability', 'Other', 'Other', 'Other'],
        'First class honours': [66270, 43685, 300, 2665, 84250, 9385, 13950, 0, 0],
        'Upper second class honours': [92405, 63875, 355, 4605, 123130, 11300, 17600, 0, 0],
        'Lower second class honours': [30940, 24880, 125, 1405, 39235, 5740, 9570, 0, 0],
        'Third class honours/Pass': [7220, 6130, 25, 205, 7825, 2100, 3245, 0, 0],
        'Unclassified': [11335, 7345, 40, 250, 10565, 4305, 3605, 0, 0],
        'Other': [5, 5, 0, 0, 10, 0, 0, 0, 0],
        'Classification': ['First', 'Second', 'Pass', 'First', 'Second', 'Pass', 'Second', 'Pass', 'Pass']}
df = pd.DataFrame(data)

# Convert categorical variables to numerical values using LabelEncoder
le_sex = LabelEncoder()
le_disability = LabelEncoder()
le_classification = LabelEncoder()
df['sex_encoded'] = le_sex.fit_transform(df['Sex'])
df['disability_encoded'] = le_disability.fit_transform(df['Disability'])
df['classification_encoded'] = le_classification.fit_transform(df['Classification'])

# Prepare the independent variables (features) and dependent variable (target)
# Prepare the independent variables (features) and dependent variable (target)
X = df[['sex_encoded', 'Age', 'disability_encoded', 'First class honours', 'Upper second class honours', 'Lower second class honours', 'Third class honours/Pass', 'Unclassified', 'Other']]
y = df['classification_encoded']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Create and train the multinomial logistic regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the model's performance metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=le_classification.classes_))





# The output shows that the precision, recall, and F1-score for some classes are 0.0, and it also shows 
# some UndefinedMetricWarnings. These warnings occur when there are no predicted samples or no true 
# samples for some classes. This can happen when the data is imbalanced, and some classes have very few samples.


# The code performs the following tasks:
# 1.	Defines a dictionary 'data' with the data to be used for analysis.
# 2.	Imports the required libraries: pandas, LabelEncoder, train_test_split, LogisticRegression, classification_report, and accuracy_score.
# 3.	Converts categorical variables to numerical values using LabelEncoder and adds them as new columns to the pandas DataFrame 'df'.
# 4.	Prepares the independent variables (features) and dependent variable (target) and assigns them to the variables X and y, respectively.
# 5.	Splits the data into training and testing sets using the train_test_split function.
# 6.	Creates a multinomial logistic regression model using LogisticRegression with multi_class='multinomial', solver='lbfgs', and max_iter=1000.
# 7.	Fits the model to the training data using the fit function.
# 8.	Makes predictions on the test set using the predict function.
# 9.	Calculates the model's performance metrics by printing the accuracy and classification report using the accuracy_score and classification_report functions.
# Overall, the code uses a logistic regression model to predict the classification of students based on their gender, age, disability, and grades. It encodes categorical variables and prepares the data for analysis, then trains the model and evaluates its performance using accuracy and other classification metrics. The output shows the model's accuracy and precision, recall, and F1-score for each class in the test set

