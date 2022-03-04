
from re import I


values_str = """0  20-24-female_Higher_Secondary_fin                 656286.0307628437
1  children_per_woman                                382974.4950600916
2  co2_emissions_percapita                           116278.14568862511
3  gini_index                                        101323.6553943645
4  population                                        93404.65103581121
5  20-24-Higher_Secondary_fin                        84465.34317598981
6  gdppercapita_us_infla_adjust                      67241.82479145261
7  20-24-female_Primary_fin                          40223.05811154557
8  20_yrs_old_gdppercapita_us_infla_adjust           30175.495728068083
9  20-24-female_Lower_Secondary_fin                  25357.14809456613
10  20-24-Primary_fin                                 16089.832982359978
11  20-24-Lower_Secondary_fin                         15757.07766815045"""

indicators_str = values_str.split('\n')

indicator_dic = {}
total_sum_score = 0
for indicator_str in indicators_str:
    indicator_list = indicator_str.split()
    indicator_dic[indicator_list[1]] = indicator_list[2]
    total_sum_score += float(indicator_list[2])
    
indicator_dic_per = {}

for indicator in indicator_dic:
    indicator_dic_per[indicator] = round((float(indicator_dic[indicator])/total_sum_score) * 100, 2)
    

for indicator in indicator_dic_per:
    print(f"{ indicator}, {indicator_dic_per[indicator]}")