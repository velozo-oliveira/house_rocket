# House Rocket
![alt text](https://github.com/velozo-oliveira/house_rocket/blob/main/real_estate.jpg)

## 1 - Description
**House Rocket** is a fictional company looking for investment opportunities in the real estate market.

The purpose of this project is to create insights through data analysis to help the decision-makers find the best business opportunities in the real estate market of King County. In other words, finding homes below market value in good locations and with good potential for future resale at a higher price.

## 2 - Business Problem
The House Rocket CEO set the following business problems:  
* What properties should we purchase and at what price?
* After the properties are in the company's possession, what is the best time to sell them and what would be the sale prices?

## 3 - Data Overview
The dataset used in this project represents properties sold from May 2014 through May 2015 in King County, WA - USA. 
The dataset is available on [Kaggle - House Sales in King County, USA.](https://www.kaggle.com/harlfoxem/housesalesprediction)

![alt text](https://camo.githubusercontent.com/0c912b9ede0dbd707a80ac066851e25060a7a992e2ac25ca42f20c3c3e67135f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4b6167676c652d3230424546463f7374796c653d666f722d7468652d6261646765266c6f676f3d4b6167676c65266c6f676f436f6c6f723d7768697465?raw=true)

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


## 4. Business Assumptions
The assumptions of the business problem in this project are as follow:

* All the properties are considered options to be purchased by House Rocket Company for the **price** listed in the dataset.
* The duplicate **ID** values were removed and only considered the most recent buy.
* Values of 0 in attribute **yr_renovated** are buildings that were not renovated.
* The **location** and **condition** of the property is key for the decision on whether to buy it or not.
* The **season** is the decisive variable for the selling of the properties.

## 5. Solution Strategy
<dd>
<strong>Step 1. Business Analysis and Data Collection</strong>
<ul>
  <li>Understand the business problem</li>
  <li>Collect Data from Kaggle</li>
</ul>
</dd>
<strong>Step 2. Data Transformation</strong>
<ul>
  <li>Variable transformation</li>
  <li>Data cleaning</li>
</ul>
</dd>
<dd>
<strong>Step 3. Exploratory Data Analysis</strong>
<ul>
  <li>Explore the data to find insights for the business team </li>
  <li>Build, deploy and run a cloud application where the House Rocket CEO can do the analyses by himself reviewing the company's portfolio </li>
</ul>
</dd>

The app presents descriptive tables, graphs and maps with an interactive user interface. With the available filters, the CEO can select the data to be shown in tables and graphs.  

Click here to launch the app: [House Rocket](https://analysis-dashboard-rocket.herokuapp.com/)  
![alt text](https://camo.githubusercontent.com/d18f98a93a8ca015503870e592f96dbdf86f41048e9de1fbbbd4b2dcc7c456b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6865726f6b752d2532333433303039382e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6865726f6b75266c6f676f436f6c6f723d7768697465)

<dd>
<strong>Step 4. Hypotheses Testing</strong>
<ul>
  <li>Discover insights and trends and communicate the findings to the business team</li>
</ul>
</dd>

<dd>
<strong>Step 5. Business Results</strong> 
<ul>
</dd>
  
* [Purchase Recommendation Report](https://github.com/velozo-oliveira/house_rocket/blob/main/reports/report_buy.csv)  
Group the properties by area (zip code). Calculate the median price within each area. Include in the report properties that are below the median price for each area and that are in good condition. 

* [Sales Price Report](https://github.com/velozo-oliveira/house_rocket/blob/main/reports/report_sale.csv)  
Group the properties by area (zip code) and by seasons (summer, winter, fall, spring). Calculate the median price within each area and season. Create a report listing all properties with a recommended sales price for each one. 
  
  
<dd>
<strong>Step 6. Conclusions</strong>
</dd>
The dashboard, along with reports will help the business team to close the best deals in the real estate market.
For more information please visit the [Project Notebook](https://github.com/velozo-oliveira/house_rocket/blob/main/House_Rocket_Notebook.ipynb).

![alt text](https://camo.githubusercontent.com/e922b45bfb79029cf4436e255b0d17b00b651e13b24f1751a9f87b14055fb4b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a7570797465722d2532334641304630302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6a757079746572266c6f676f436f6c6f723d7768697465)


## 6. Hypothesis Testing

**Hypothesis 01**: Properties that are waterfront are, in average, 30% more expensive.  
**False**: Waterfront houses are 213% more expensive, on average.

**Hypothesis 02**: Properties built before 1955 are, in average, 15% less expensive.  
**False**: Properties built before 1955 are 1.0 % cheaper than properties built after 1955. The year built does not influence the price of the property.

**Hypothesis 03**: Properties with basement have a living area 20% bigger than the ones without basement.  
**True**: Properties with basement are approximately 20% bigger in terms of living area, compared with properties without basement.

**Hypothesis 04**: Properties that were never renovated are, in average, 20% less expensive.  
**False**: Properties that were never renovated are, in average, 43 % less expensive

**Hypothesis 05**: Properties with higher number of bedrooms are, in average, 10% more expensive.  
**False**: Properties with 7 to 9 bedrooms are, in avarage, more expensive.

**Hypothesis 06**: The MoM (Month over Month) growth of the price of the properties with 3 bathrooms is 15%.  
**False**: The average price of the properties is higher between March and July.

## 7. Business Results
As per requested by the CEO of House Rocket, two reports were created to help the business team to make decisions. The Recommandation Report indicates which properties the company should invest on. The Sales Price Report suggests the best price to sell each property in the future considering the location and seasonality. 

A total of 3844 properties presented a buying price bellow the median of their zip code, and therefore were suggested as potential good buys.

The sale price was calculated for two situations:  
1 - If the purchase price is greater than the area median price plus the effect of the season, the sale price will be equal to the purchase price plus 5%.  
2 - If the purchase price is lower than the area median price plus the effect of the season, the sale price will be equal to the purchase price plus 10%.

The table below presents the estimated results for each situation:

|Sale Condition  |No of Properties| Total Cost (US$)| Sales Revenue (US$) | Profit (US$) |
| :-------------:|:---------------|:----------------|:--------------------|:-------------|
|1|1415|647,432,970|676,654,618.5|32,221,648.5|
|2|2429|873,329,930|960,662,923|87,332,993|
|**Total**|**3844**|**1,517,762,900**|**1,637,317,541.5**|**119,554,641.5**|

## 8. Conclusions
Overall, House Rocket was a great study project to practice the basics concepts of data analysis. Guided by my mentor Meigarom Lopes, I was able to explore and manipulate the data set using Python. The business problem was solved using a superficial approach, but enough to add value to the company. 

The next step would include more variables in the purchasing and selling analyis, such as number of badrooms, living area, and potentially adding features to ensure the property valuation would increase. 

