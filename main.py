import pandas as pd
from scipy import stats

# T-Test 
#Do countries with higher renewable energy have lower CO2 emissions

df = pd.read_csv("climate_change_dataset.csv")

#Renewable energy median (rem)
rem = df['Renewable Energy (%)'].median()

countries_high_renewable = df[df["Renewable Energy (%)"] > rem]['CO2 Emissions (Tons/Capita)']

countries_low_renewable = df[df["Renewable Energy (%)"] <= rem]['CO2 Emissions (Tons/Capita)']

t_stat, p_value = stats.ttest_ind(countries_high_renewable,countries_low_renewable)


if (p_value < 0.05): # type: ignore
    print(f"T-val: {t_stat}, P-val: {p_value}\nIn this case we reject the null hypothesist")
else:
    print(f"T-val: {t_stat}, P-val: {p_value}\nIn this case we fail to reject the null hypothesist")
