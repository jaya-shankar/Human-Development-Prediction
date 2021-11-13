# education-impact
A ML model to find which factors influence the development of the country the most

## Random Forest
### First Attempt
We trained a TensorFlow RandomForest without any data interpolation

train : test = 70 : 30

total data points : 2834

#### model performance:

"malnutrition","maternal_mortality","people_in_poverty"  were not used by the model.

**MSE** : 5.545248985290527

**RMSE**: 2.354835235274546
 ![First Attempt Decision Tree](images/firstAttempt.png)

 ### Second Attempt
We trained a TensorFlow RandomForest with WCDE datasets, data interpolation

train : test = 70 : 30

total data points : 2834

#### model performance:

"malnutrition","maternal_mortality","people_in_poverty"  were not used by the model.

**MSE** : 3.8452484607696533

**RMSE**: 1.9609305089088835
 ![First Attempt Decision Tree](images/secondAttempt.png)