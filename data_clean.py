# import pandas as pd
import pandas as pd

root = "" 
datasets_path = {
                    "infant_mortality"              :  root+ "datasets/Infant_Mortality_Rate.csv",
                    "child_mortality"               :  root+ "datasets/child_mortality_0_5_year_olds_dying_per_1000_born.csv",
                    "children_per_woman"            :  root+ "datasets/children_per_woman_total_fertility.csv",
                    "co2_emissions"                 :  root+"datasets/co2_emissions_tonnes_per_person.csv",
                    "population"                    :  root+ "datasets/converted_pop.csv",
                    "food_supply"                   :  root+ "datasets/food_supply_kilocalories_per_person_and_day.csv",
                    "gdp_per_captia"                :  root+ "datasets/gdp_per_capita_yearly_growth.csv",
                    "Avg_daily_income_ppp"          :  root+ "datasets/mincpcap_cppp.csv",
                    "gini_index"                    :  root+ "datasets/gini.csv",
                    "life_expectancy"               :  root+ "datasets/life_expectancy_years.csv",
                    "malnutrition"                  :  root+ "datasets/malnutrition_weight_for_age_percent_of_children_under_5.csv",
                    "poverty_index"                 :  root+ "datasets/mincpcap_cppp.csv",
                    "maternal_mortality"            :  root+ "datasets/mmr_who.csv",
                    "people_in_poverty"             :  root+ "datasets/number_of_people_in_poverty.csv",
                    "primary_completion"            :  root+ "datasets/primary_school_completion_percent_of_girls.csv",
                    "ratio_b_and_g_in_primary"          :  root+ "datasets/ratio_of_girls_to_boys_in_primary_and_secondary_education_perc.csv",
                    "wcde-25--34"                   :  root+ "datasets/wcde-25--34.csv",
                    "wcde-Incomplete_Primary"       :  root+ "datasets/wcde-Incomplete Primary.csv",
                    "wcde-Lower_Secondary"          :  root+ "datasets/wcde-Lower Secondary.csv",
                    "wcde-Post_Secondary"           :  root+ "datasets/wcde-Post Secondary.csv",
                    "wcde_female-Incomplete_Primary":  root+ "datasets/wcde_female-Incomplete Primary.csv",
                    "wcde_female-Lower_Secondary"   :  root+ "datasets/wcde_female-Lower Secondary.csv",
                    "wcde_female-Post_Secondary"    :  root+ "datasets/wcde_female-Post Secondary.csv",
                }


for dataset in datasets_path:
    df = pd.read_csv(datasets_path[dataset])
    df["Country"] = df["Country"].str.lower()
    df.to_csv(root+"datasets_clean/clean_"+dataset+".csv", index=False)
