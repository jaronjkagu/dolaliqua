import pandas as pd

# Create a DataFrame
data = {'Team': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Score': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)

# Group the data by the 'Team' column
grouped = df.groupby('Team')

# Apply a function to each group, such as calculating the mean
mean_scores = grouped.mean()
