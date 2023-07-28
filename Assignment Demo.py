# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define the path to your CSV file
file_path = 'Groceries_dataset.csv'

# Load the data
data = pd.read_csv(file_path)

# Calculate the frequency of each item
item_counts = data['itemDescription'].value_counts().head(10)

# Create a bar plot for the 10 most frequently purchased items
plt.figure(figsize=(10,6))
plt.barh(item_counts.index, item_counts.values, color='steelblue')
plt.xlabel('Count')
plt.ylabel('Item')
plt.title('10 Most Frequently Purchased Items')
plt.gca().invert_yaxis()

# Save the figure as a PNG file
plt.savefig('most_purchased_items.png')

# Display the plot
plt.show()