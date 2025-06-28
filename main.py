import pandas as pd
from scipy import stats

#correlation
#H0 There is no correlation betweeen average temperature and CO2 emssisions
#H1 Therer is a correlation between temperature and C02 emissions

df = pd.read_csv("climate_change_dataset.csv")

temperature_col = df["Avg Temperature (°C)"]
co2_col = df['CO2 Emissions (Tons/Capita)']


#using scipy to use built in pearson correlation

correlation_result = stats.pearsonr(temperature_col,co2_col)

print(correlation_result[0], correlation_result[1])

#T test
#H0 There isn't a differencce between the sea level rise before and after 2010
#H1 There is a difference between the sea level before/after 2010

# If p<0.5 we reject H0 if p>0.5 we fail to reject h0

sea_level_before = df[df["Year"] <= 2010]["Sea Level Rise (mm)"]
sea_level_after = df[df["Year"] > 2010]["Sea Level Rise (mm)"]

t_result = stats.ttest_ind(sea_level_before,sea_level_after)

print(t_result[0], t_result[1])

#Anova

data_by_country = []

for country in df["Country"].unique():
    group = df[df["Country"] == country]["CO2 Emissions (Tons/Capita)"]
    data_by_country.append(group)


anova_results = stats.f_oneway(*data_by_country)

print(anova_results[0], anova_results[1])
