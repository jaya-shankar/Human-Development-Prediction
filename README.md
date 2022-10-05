# Human Development Prediction
A ML model to find which factors influence the development of the country the most
# Report
 ### https://drive.google.com/file/d/1JXC0iJGKxBqqtUY2pk1-I26JTBTnNs8A/view?usp=sharing
# Goal
Our goal to find the most important indicator among the four indices which drives the development of a country and also how are these indicators are interrelated
## Approach
Initially we tried to predict country's development factors 40 years ahead, but due to data unavailability ,it's not feasible approach

We tried to find is there is any correaltion between different indicators using Random forest and Gradient Tree Algoritims

## Models Built
We built 2 x 5 different models each one for each Human Development Indices 
1) Life Expectancy
2) Total Fertility Rate
3) GDP per capita US inflation adjusted
4) Primary Education Completion rate ( 20 - 24 Age group )
5) Secondary Education Completion rate ( 20 - 24 Age group )
i ) Model built using all countries data
ii ) Model built using only developing/undeveloped* countries data

## Features
Features/Indicators used to train the model in predicting the state of the country
1) Life Expectancy
2) Infant Mortality Rate
3) Under 5 Mortality Rate
4) Total Fertility Rate
5) Primary Education Completion for age group 20-24\*
6) Lower Secondary Education Completion for age group 20-24
7) Higher Secondary Education Completion for age group 20-24
8) Female Primary Education Completion for age group 20-24
9) Female Lower Secondary Education Completion for age group 20-24
10) Female Higher Secondary Education Completion for age group 20-24
11) Population
12) GDP per Capita
13) Gini Index
14) CO2 emissions per capita

_Note_: Not all features are used in all the models we choose specific features each model based on some assumptions and data visualization which are mentioned in the report
/* -> The reason for using education levels of age group 20-24 is mentioned in the report

## Macro Level Diagram
![Macro Level Diagram](https://github.com/jaya-shankar/Human-Development-Prediction/blob/master/Macro%20level%20Diagram.png)

## Findings
The values in the cells are NRMSE scores of the best performing models for each predictor 

**Models considering all countries**
| Indicator Predicted      | Random Forest | Gradient Tree     |
| :---        |    :----:   |          ---: |
| Life Expectancy      | 0.03200       | 0.02672   |
| Total Fertility Rate   | 0.08868        | 0.10664     |
| GDP per capita     | 0.12329       | -  |
| Primary Education Comp.   | 0.04720        | 0.04191    |
| Lower Sec Education Comp.   | 0.05076        | 0.05758    |

**Models considering only Developing/Undeveloped countries**
| Indicator Predicted      | Random Forest | Gradient Tree     |
| :---        |    :----:   |          ---: |
| Life Expectancy      | 0.03431     | 0.02386   |
| Total Fertility Rate   | 0.05421        | 0.04755     |
| GDP per capita     | 0.18760       | -  |
| Primary Education Comp.   | 0.07726       | 0.06950    |
| Lower Sec Education Comp.   | 0.09420      | 0.07881    |

## Conclusions
Based on NRMSE scores we can rely on the Life Expectancy Model ( all / developing ) , TFR ( developing ), Primary & Lower Secondary Completion Rate ( all ) and Primary & Lower Secondary Completion Rate ( developing ) models to some extend

We can say Total Fertility Rate & Life Expectancy are highly interlinked i.e., both are interdependent based on models built using all countries data, and second important indicator to predict both of them is female higher secondary education completion rate followed by other female education completion rate in chronological order

To improve Life Expectancy & Total Fertility Rate of developing/undeveloped countries , the important indicator which needs to focused on is Female Education Levels.The better the female education the faster the improvement of the indicators

Also one of the interesting fact we found based on the models is GDP per capita & population did not show up as important indicator to predict Life Expectancy & Total Fertility Rate

We cannot rely on GDP per capita model results because of high NRMSE score even after including 20 yrs old GDP data the model built was not reliable so we conclude predication of GDP per capita using the given indicators and algorithms we used

Predication of Primary education is highly dependent on 20 yrs old Under 5 Child Mortality rate and in turn U5MR is dependent on Primary education completion rate for both all and developing countries dataset so we conclude that primary education completion rate is dependent on itself

Predication of Lower Secondary Education compeletion is highly dependent on 20 yrs old Primary Education Completion rate that is parent’s generation education and 10 yrs CO2 emission per capita which is proxy for economic state of the country so we conclude to improve lower secondary education level one must focus on improving the primary education levels

# Future Work
We are really interested to understand countries which have fast transition from undeveloped/developing to developed countries in all indicators
What we did was we found out all top performing countries in all the indicators in the following manner
- The country should be in bottom 50% countries in the year 1960 in all aspects
- The country should be in top 10% countries in the year 2015 in all aspects.By using the above constraints we got the following countries as top performing countries
   - China,
   - South Korea
   - Thailand
   - Singapore


We want to find out by improving which at the beginning helped the following to countries to have rapid growth , RNN is one of the algorithms that can be applied to analyse

We can improve model performance by adding more indicators and analyse them

We could not find proper predictions for GDP per capita, we believe there is more research and analysis needed to be done and try with more indicators

We tried regression using deep neural networks and the results are not presented in the paper as we couldn’t understand how to analyze the model that weight of each indicator but the code for training is available in the repository
Countries which are at war or political instabilty couldn't perform as expected by the HDI, Beacuse of the change in policies or consequences od the War, Which should be taken into account in Future work
