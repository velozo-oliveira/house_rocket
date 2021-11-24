# House Rocket
![alt text](https://github.com/velozo-oliveira/house_rocket/blob/main/real_estate1.jpg?raw=true)

## 1 - Description
**House Rocket** is a fictional company looking for investment opportunities in the real estate market.

The purpose of this project is to create insights through data analysis to help the decision-makers find the best business opportunities in the real estate market of King County. In other words, finding homes below market value in good locations and with good potential for future resale at a higher price.

## 2 - Business Problem
The House Rocket CEO set the following business problems:

* What properties should we purchase and at what price?
* After the properties are in the company's possession, what is the best time to sell them and what would the sale prices be?
* Should House Rocket do a renovation to raise the sale price? What would be the suggestions for changes? What is the price increase given for each refurbishment option?

## 3 - Data Overview
The dataset used in this project represents 21613 properties sold from May 2014 through May 2015 in King County, WA - USA. 
The dataset is available on [Kaggle - House Sales in King County, USA.](https://www.kaggle.com/harlfoxem/housesalesprediction)

Below is a breakdown of the attributes:

|Attribute  |Description|
| :--------- |:-----------|
|id	|Unique ID for each property |
|date|	Date of the property |
|price|	Price of each property |
|bedrooms	|Number of bedrooms|
|bathrooms|	Number of bathrooms, where .5 accounts for a room with a toilet but no shower|
|sqft_living|	Square footage of the property interior living space|
|sqft_lot	|Square footage of the land space|
|floors|	Number of floors|
|waterfront|	A dummy variable for whether the home was overlooking the waterfront or not|
|view	|An index from 0 to 4 of how good the view of the property was|
|condition	|An index from 1 to 5 on the condition of the property|
|grade	|An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design|
|sqft_above	|The square footage of the interior housing space that is above ground level|
|sqft_basement|	The square footage of the interior housing space that is below ground level|
|yr_built	|The year the property was initially built|
|yr_renovated	|The year of the property’s last renovation|
|zipcode|	What zip code area the property is located|
|lat	|Latitude|
|long	|Longitude|
|sqft_living15|	The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15	|The square footage of the land lots of the nearest 15 neighbors|

![alt text](https://camo.githubusercontent.com/0c912b9ede0dbd707a80ac066851e25060a7a992e2ac25ca42f20c3c3e67135f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4b6167676c652d3230424546463f7374796c653d666f722d7468652d6261646765266c6f676f3d4b6167676c65266c6f676f436f6c6f723d7768697465?raw=true)

## 4. Business Assumptions
The assumptions about the business problem accepted in this project are as follow:

Values of 0 in attribute **yr_renovated** are buildings that were not renovated.
**Recent renovations** were considered to be the ones made after, and including, year 2000.
The attribute **price** represents the price that can potentially be bought by the House Rocket company.
The **location** and **condition** of the property is key for the decision on wether to buy it or not.
The **season** is the decisive variable for the selling of the properties.

## 5. Solution Strategy

### Step 1. Business Analysis and Data Collection
* Understand the business problem
* Collect Data from Kaggle

### Step 2. Data Transformation:
* Variable transformation
* Data cleaning

### Step 3. Exploratory data analysis
* Explore the data to find insights for the business team
* Build, deploy and run an app where the House Rocket CEO can do the analyses by himself reviewing the company's portfolio. 

The app presents descriptive tables, graphs and maps with an interactive user interface. With the available filters, the CEO can select the data to be shown in tables and graphs.

Click here to launch the app: [House Rocket](https://analysis-dashboard-rocket.herokuapp.com/)

![alt text](https://camo.githubusercontent.com/d18f98a93a8ca015503870e592f96dbdf86f41048e9de1fbbbd4b2dcc7c456b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6865726f6b752d2532333433303039382e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6865726f6b75266c6f676f436f6c6f723d7768697465)

### Step 4. Hypotheses Testing
* Discover insights and trends and communicate the findings to the business team.

### Step 5. Business solutions
* Purchase Recommendation Report 

Group the homes by area (zip code). Calculate the median price within each area. Include in the report homes that are below the median price for each area and that are in good condition. The report can be found here: [Link]

* Sales Price Report

Create a report listing all properties with a recommended sales price for each one. Group the homes by area (zip code) and by seasons (summer, winter, and so on). Calculate the median price within each area and season. The report can be found here: [Link]

### Step 6. Conclusions
