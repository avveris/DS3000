# Import necessary libraries
from pytrends.request import TrendReq
import pandas as pd

# Initialize Google Trends API client
pytrends = TrendReq(hl='en-US', tz=360)

# Define expanded health-related search terms to analyze
health_terms = [
    "intermittent fasting", "home workouts", "mental health", "healthy eating", "meditation",
    "anxiety relief", "yoga benefits", "keto diet", "low carb diets", "meal prep ideas",
    "stress management", "sleep quality"
]

# Setting up the empty dictionary for Trend Data
trends_dict = {'search_term': list(),
               'date': list(),
               'interest_score': list(),
               'year': list(),
               'month': list()}

# Loop through the search terms and retrieve trend data
for term in health_terms:
    # Get interest over time data for each search term
    pytrends.build_payload([term], timeframe='all')
    trends_data = pytrends.interest_over_time()

    # If trends_data is empty, skip to the next term
    if trends_data.empty:
        continue

    # Extract relevant trend data
    for index, row in trends_data.iterrows():
        trends_dict['search_term'].append(term)
        trends_dict['date'].append(row.name)
        trends_dict['interest_score'].append(row[term])
        trends_dict['year'].append(row.name.year)
        trends_dict['month'].append(row.name.month)

# Convert dictionary to DataFrame
trends_df = pd.DataFrame(trends_dict)

# Save the DataFrame to a CSV file
trends_df.to_csv('health_trends_data.csv', index=False)

print("Data has been saved to 'health_trends_data.csv'")
