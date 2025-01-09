import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def get_training_data(filename):
    dataframe=pd.read_csv(filename)
    print(dataframe)
    x_parameters=[]
    y_parameters=[]


    for single_sqare_feet, single_price in zip(dataframe['square_feet'],dataframe['price']):
        x_parameters.append([single_sqare_feet])
        y_parameters.append(     single_price      )
    #Once we got the data , return it to main program
    return x_parameters, y_parameters

def train_linear_model(x_parameters,y_parameters,quest_value):
    #Create Linear Regression Object
    regr = LinearRegression()
    regr.fit(x_parameters,y_parameters)
    predicted_ans = regr.predict([[quest_value]])       #quest_value=700
    print("Output from machine = ",predicted_ans)

    print("After Training via sklearn: Model Parameter")
    print("m = ",regr.coef_)    #m
    print("c = ",regr.intercept_)   #c
    print("Sklearn generated Model: y =",regr.coef_,"* x +",regr.intercept_)
    plt.scatter(x_parameters,y_parameters,color="m",marker="o")
    all_predicted_y=regr.predict(x_parameters)
    plt.scatter(x_parameters,all_predicted_y,color="b",marker="o")
    plt.plot(x_parameters,all_predicted_y,color="g")
    plt.scatter(quest_value,predicted_ans,color="r")
    plt.show()

def startAIAlogrithm():
    #Collect the training data from external csv data file.
    x,y = get_training_data('LR_House_price.csv')
    print("Formatted Training Data : ")
    print("x = ",x)
    print("y = ",y)
    question_value = 700    #This is the question
    train_linear_model(x,y,question_value)

if __name__ == "__main__":
    startAIAlogrithm()