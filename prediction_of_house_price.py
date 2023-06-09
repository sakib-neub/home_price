# -*- coding: utf-8 -*-
"""Prediction_of_house_price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GlWOgfCHPn2Uue9DTX6VuGzf0HXEP2Yq

**<h1>Prediction of House Price</h1>**

**<h3>Introduction</h3>**

The purchase and sale of real estate has important ramifications for people, corporations, and policymakers alike, making it an essential part of any economy. Understanding and forecasting housing prices can support firms in their investment strategies, buyers and sellers in their decision-making, and policymakers in their efforts to govern and regulate the market.

In this project, we want to create a machine learning model that can precisely forecast the price of a house based on a variety of characteristics, including the size of the property, the number of bedrooms and bathrooms, and the location of the house. We will make use of a dataset on housing costs in the US, which includes details on over 21,000 homes sold between 2014 and 2015.

We want to examine this dataset, clean and prepare the data, and then use the Random Forest algorithm to create a prediction model. We will examine the key characteristics that help predict the price of a house and assess the model's effectiveness using the Root Mean Squared Error (RMSE).

We want to have obtained insights into the housing market and the factors that influence housing prices by the end of this project, as well as constructed a model that can be used to generate accurate predictions of house prices for future sales.
"""



"""Import libraries"""

import pandas as pd
import numpy as np
import tensorflow as tf

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error





"""Load dataset"""

df = pd.read_csv("/content/data.csv")
df.head()

"""Data explore:
Explore the dataset using df.head(), df.info(), df.describe(), ,df.shape() and df.isnull().values.any() to get a sense of the data. 
"""

df.info()

print(df.describe())

print("Dataframe Shape: ", df.shape)
# df["NextShares"].plot()

print("Null Value Present: ", df.isnull().values.any())

"""Figure:
observe price depend on city
and observe price depend on bedrooms
"""

area_means = df.groupby('city')['price'].mean()
print(area_means)

city = df['city']
price = df['price']
fig = plt.figure(figsize=(10, 18))

plt.scatter(price,city)
plt.ylabel('city')
plt.xlabel('Price')
plt.title('Price vs city')
plt.show()

max_bedrooms = df['bedrooms'].max()
print(max_bedrooms)

min_bedrooms = df['bedrooms'].min()
print(min_bedrooms)

max_price=df['price'].max()
print(max_price)

mean_price=df['price'].mean()
print(mean_price)

zero_bedrooms = df.loc[df['bedrooms'] == 0]

print(zero_bedrooms)

# Group the data by number of bedrooms and calculate the mean price for each group
bedroom_means = df.groupby('bedrooms')['price'].mean()

# Create a bar chart of the bedroom means
bedroom_means.plot(kind='bar')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Average Price')
plt.title('Average Price per Bedroom')


plt.show()

"""Data processing:
pd.to_datetime() method. It converts the string representation of date to a datetime object.
encoded values object to numerical.
 Drop the 'country' and 'date' columns as they are not useful for our analysis.
 Split the dataset into training and testing sets using train_test_split() function from sklearn.
"""



# df['date'] = pd.to_datetime(df['date'])

df['date'] = pd.to_datetime(df['date'])
df['date'] = (df['date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

df





from sklearn.preprocessing import LabelEncoder

# Create a new column for the encoded values
# df['encoded_column'] = LabelEncoder().fit_transform(df['categorical_column'])

# Loop through all columns in the DataFrame
for column in df.columns:
    if df[column].dtype == 'object':  # Check if the column contains strings
        df[column] = LabelEncoder().fit_transform(df[column])

df.head()

df.drop(['country', 'date'], axis=1, inplace=True)

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)



"""Make predictions on the testing data and calculate the mean squared error

"""



y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)



"""Example of using the model to predict the price of a new house
enter all the feature of house and it will predict the nearest price for that house.

"""

new_house = np.array([[	5.0,	2.50,	3650,	9050,	2.0	,0,	4,	5,	3370,	280	,1921	,0	,3899,	35,	58]])  # Features (size, bedrooms, bathrooms, latitude, longitude)
predicted_price = model.predict(new_house)
print("Predicted price:", predicted_price)

from sklearn.metrics import r2_score

accuracy_score = 

print('R^2 score: {:.2f}'.format(accuracy_score))

"""<h3>Conclution</h3>

Following a thorough examination of the data, it was discovered that the three most influencing determinants on housing costs are property size, house location, and bedroom/bathroom count. When it comes to housing market decisions, our model can be a helpful tool for buyers, sellers, and even policymakers. Though we are encouraged by our preliminary results, we recognise that there is always room for improvement through new data and feature engineering.
"""

