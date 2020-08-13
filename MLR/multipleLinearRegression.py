import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def read_csv_to_df():
    df = pd.read_csv('Clean_Data/df_data.csv').drop(['Unnamed: 0'], axis=1)
    return df


def do_some_regression():
    dataset = read_csv_to_df()

    #plt.figure(figsize=(15, 10))
    #plt.tight_layout()
    #seabornInstance.distplot(dataset['Cases'])
    #plt.show()
    print(dataset['Cases'])

    X = dataset[['Corona', 'Covid', 'Flu', 'Hand Sanitizer', 'Mask', 'Virus']]
    y = dataset['Cases']
    #Split data into 80% training 20% testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #check coefficients
    coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
    #print(coeff_df)

    #do predictions on test data
    y_pred = regressor.predict(X_test)

    #actual value vs predicted value
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)
    #print(df1)

    #Plot actual vs predicted
    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    #plt.show()

    #Check preformance of algorithm
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


if __name__ == '__main__':
    do_some_regression()
