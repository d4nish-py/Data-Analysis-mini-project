import pandas as pd 
import matplotlib.pyplot as mp

# using custom dataset forked from https://ourworldindata.org/covid-deaths
# the dataset can be found in the same folder
df = pd.read_csv(r"covid-deaths.csv")

print(df.head())

# selecting useful and common columns
data = df[["country","date", "total_cases", "new_cases", "total_deaths", "new_deaths"]]

# this filters it for one country // eg. using Algeria for example due to limited data in csv
country_data = data[data["country"] == "Algeria"]

#converts 'date' column to datetimes
country_data["date"] = pd.to_datetime(country_data["date"])

# Rolling average for smoother visualization
country_data["new_deaths_7d_avg"] = country_data["new_deaths"].rolling(7).mean()

# Visualization
fig = mp.figure(figsize=(10,6))
fig.canvas.manager.set_window_title("Covid 19 Analyzer")
mp.plot(country_data["date"], country_data["new_deaths_7d_avg"], label="new_deaths", linewidth=2)
mp.xlabel("Date")
mp.ylabel("New Deaths")
mp.title("New COVID-19 Deaths in Algeria (7-day average)")
mp.legend()
mp.grid(True)
mp.tight_layout()

fig.text(0.5, 0.5, "made by d4nish", fontsize=30, color="gray",
         ha="center", va="center", alpha=0.2, rotation=30)
mp.show()