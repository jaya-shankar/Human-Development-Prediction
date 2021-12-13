## Done:-
- Converted population dataset values from string to numbers using python script
- extracted WCDE data and added in datasets
## To Do:-

- Find the common countries from the datasets.
  - a) Either add the missing countries to the datasets.
  - b) Remove the missing countries from the remaining datasets.

- Build a 3D Numpy array containing countries, years and development factors as axis.

- Create new Numpy arrays containg outputs(From year 2000) : Life Expectancy, GDP, Education(Level of education for ages below 40years).

- Build a Decision Tree and Random Forest for the given inputs and outputs.

- Measure the accuracy.

- Explore different possible algorithms and measure the accuracy.


## To Try:
- First build model using decision trees & random forests and then on top of it use XGBoost algorithm.




## Assumptions about how to use data
1 - gdp         - 20 yrs old
2 - gdp today   - current
3 - edu level   - current
4 - life exp    - current
5 - tfr         - current

to predict gdp use 1,3,4,5

to predict life exp use 

to predict edu level use 1,2,4,5




## conclusions

### for life exp :

Input Features (10):
	20-24-In_Primary_OL
	20-24-Primary_OL
	20-24_female-In_Primary_OL
	20-24_female-Primary_OL
	children_per_woman
	co2_emissions_percapita
	gdppercapita_us_infla_adjust
	gdppercapita_us_infla_adjust_20years_before
	gini_index
	population

No weights

Variable Importance: MEAN_MIN_DEPTH:
    1.                                     "__LABEL" 11.748073 ################
    2.                         "20-24-In_Primary_OL"  8.435553 ##########
    3. "gdppercapita_us_infla_adjust_20years_before"  8.204703 ##########
    4.                            "20-24-Primary_OL"  8.201590 ##########
    5.                                  "population"  7.950396 #########
    6.                  "20-24_female-In_Primary_OL"  7.526676 #########
    7.                                  "gini_index"  6.886902 ########
    8.                     "co2_emissions_percapita"  6.415726 #######
    9.                     "20-24_female-Primary_OL"  4.550530 ####
   10.                "gdppercapita_us_infla_adjust"  4.374326 ####
   11.                          "children_per_woman"  1.636202 

Variable Importance: NUM_AS_ROOT:
    1.         "children_per_woman" 162.000000 ################
    2.    "20-24_female-Primary_OL" 80.000000 #######
    3. "20-24_female-In_Primary_OL" 33.000000 ###
    4.           "20-24-Primary_OL" 19.000000 #
    5.        "20-24-In_Primary_OL"  4.000000 
    6.    "co2_emissions_percapita"  2.000000 

Variable Importance: NUM_NODES:
    1.                                  "population" 36720.000000 ################
    2.                          "children_per_woman" 30047.000000 ###########
    3.                                  "gini_index" 29553.000000 ##########
    4.                     "co2_emissions_percapita" 29364.000000 ##########
    5.                "gdppercapita_us_infla_adjust" 26217.000000 ########
    6.                     "20-24_female-Primary_OL" 22638.000000 #####
    7.                            "20-24-Primary_OL" 22571.000000 #####
    8.                         "20-24-In_Primary_OL" 21055.000000 ####
    9.                  "20-24_female-In_Primary_OL" 20982.000000 ####
   10. "gdppercapita_us_infla_adjust_20years_before" 15031.000000 

Variable Importance: SUM_SCORE:
    1.                          "children_per_woman" 75641785.408594 ################
    2.                     "20-24_female-Primary_OL" 40126555.632186 ########
    3.                  "20-24_female-In_Primary_OL" 17116219.578391 ##
    4.                "gdppercapita_us_infla_adjust" 13846413.411122 ##
    5.                            "20-24-Primary_OL" 11449256.273094 #
    6.                     "co2_emissions_percapita" 7882773.026798 
    7.                                  "gini_index" 6738826.165506 
    8.                         "20-24-In_Primary_OL" 5908146.456876 
    9.                                  "population" 5634153.466150 
   10. "gdppercapita_us_infla_adjust_20years_before" 4008216.953797 


### for gdp

Input Features (10):
	20-24-In_Primary_OL
	20-24-Lower_Secondary_OL
	20-24-Primary_OL
	20-24_female-In_Primary_OL
	20-24_female-Lower_Secondary_OL
	20-24_female-Primary_OL
	child_mortality
	children_per_woman
	infant_mortality
	life_expectancy

No weights

Variable Importance: MEAN_MIN_DEPTH:
    1.                         "__LABEL" 11.751111 ################
    2. "20-24_female-Lower_Secondary_OL"  9.493809 ###########
    3.         "20-24_female-Primary_OL"  8.810090 ##########
    4.        "20-24-Lower_Secondary_OL"  8.391004 #########
    5.                "20-24-Primary_OL"  7.763451 ########
    6.      "20-24_female-In_Primary_OL"  7.448441 ########
    7.              "children_per_woman"  6.126549 #####
    8.             "20-24-In_Primary_OL"  5.785711 #####
    9.                 "life_expectancy"  3.621421 #
   10.                 "child_mortality"  3.167948 
   11.                "infant_mortality"  2.808860 

Variable Importance: NUM_AS_ROOT:
    1.         "infant_mortality" 132.000000 ################
    2.          "child_mortality" 95.000000 ###########
    3.          "life_expectancy" 49.000000 #####
    4.       "children_per_woman" 20.000000 ##
    5. "20-24-Lower_Secondary_OL"  3.000000 
    6.      "20-24-In_Primary_OL"  1.000000 

Variable Importance: NUM_NODES:
    1.              "children_per_woman" 24506.000000 ################
    2.                 "life_expectancy" 22347.000000 ###########
    3.        "20-24-Lower_Secondary_OL" 18848.000000 ####
    4.                "infant_mortality" 18306.000000 ##
    5.             "20-24-In_Primary_OL" 17999.000000 ##
    6.         "20-24_female-Primary_OL" 17742.000000 #
    7.                "20-24-Primary_OL" 17716.000000 #
    8.      "20-24_female-In_Primary_OL" 17521.000000 #
    9.                 "child_mortality" 17518.000000 #
   10. "20-24_female-Lower_Secondary_OL" 16923.000000 

Variable Importance: SUM_SCORE:
    1.                "infant_mortality" 74093519586886.921875 ################
    2.                 "child_mortality" 60043676559816.781250 ############
    3.                 "life_expectancy" 42885140679562.875000 ########
    4.              "children_per_woman" 23165564427439.730469 ###
    5.             "20-24-In_Primary_OL" 20282913399155.054688 ##
    6.      "20-24_female-In_Primary_OL" 11864886581614.328125 
    7.                "20-24-Primary_OL" 11770260186435.292969 
    8.        "20-24-Lower_Secondary_OL" 11642564224051.107422 
    9.         "20-24_female-Primary_OL" 11333289924165.910156 
   10. "20-24_female-Lower_Secondary_OL" 8461745170503.916992 



### for TFR

Input Features (11):
	20-24-In_Primary_OL
	20-24-Lower_Secondary_OL
	20-24-Primary_OL
	20-24_female-In_Primary_OL
	20-24_female-Lower_Secondary_OL
	20-24_female-Primary_OL
	child_mortality
	co2_emissions_percapita
	gdppercapita_us_infla_adjust
	infant_mortality
	life_expectancy

No weights

Variable Importance: MEAN_MIN_DEPTH:
    1.                         "__LABEL" 11.546172 ################
    2.        "20-24-Lower_Secondary_OL"  8.386103 ##########
    3.    "gdppercapita_us_infla_adjust"  7.900018 #########
    4.             "20-24-In_Primary_OL"  7.662158 #########
    5.         "co2_emissions_percapita"  7.205872 ########
    6.                "infant_mortality"  6.946104 ########
    7.         "20-24_female-Primary_OL"  6.699026 #######
    8.                "20-24-Primary_OL"  6.621430 #######
    9.      "20-24_female-In_Primary_OL"  6.236713 #######
   10. "20-24_female-Lower_Secondary_OL"  5.893409 ######
   11.                 "life_expectancy"  5.699302 ######
   12.                 "child_mortality"  2.104864 

Variable Importance: NUM_AS_ROOT:
    1.                 "child_mortality" 132.000000 ################
    2.                 "life_expectancy" 75.000000 ########
    3. "20-24_female-Lower_Secondary_OL" 46.000000 #####
    4.                "infant_mortality" 21.000000 ##
    5.         "20-24_female-Primary_OL" 13.000000 #
    6.      "20-24_female-In_Primary_OL" 11.000000 #
    7.        "20-24-Lower_Secondary_OL"  2.000000 

Variable Importance: NUM_NODES:
    1.         "co2_emissions_percapita" 28772.000000 ################
    2.    "gdppercapita_us_infla_adjust" 24929.000000 #########
    3.                 "child_mortality" 24906.000000 #########
    4.                 "life_expectancy" 24641.000000 #########
    5.                "infant_mortality" 21105.000000 ###
    6.                "20-24-Primary_OL" 21091.000000 ##
    7.      "20-24_female-In_Primary_OL" 20797.000000 ##
    8.        "20-24-Lower_Secondary_OL" 20535.000000 ##
    9.             "20-24-In_Primary_OL" 20270.000000 #
   10. "20-24_female-Lower_Secondary_OL" 19691.000000 
   11.         "20-24_female-Primary_OL" 19327.000000 

Variable Importance: SUM_SCORE:
    1.                 "child_mortality" 2838314.599651 ################
    2.                 "life_expectancy" 1369686.701397 #######
    3. "20-24_female-Lower_Secondary_OL" 971060.329765 ####
    4.                "infant_mortality" 456502.873180 #
    5.         "20-24_female-Primary_OL" 445062.047823 #
    6.      "20-24_female-In_Primary_OL" 412629.566524 #
    7.                "20-24-Primary_OL" 239204.569304 
    8.         "co2_emissions_percapita" 210337.541091 
    9.        "20-24-Lower_Secondary_OL" 170576.178026 
   10.             "20-24-In_Primary_OL" 148695.687245 
   11.    "gdppercapita_us_infla_adjust" 135042.309842 
