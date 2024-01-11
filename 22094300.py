#Github link
#https://github.com/azmatmanzoor/Project-DHV


#Plot1


import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
import seaborn as sns


# Convert the string data to a DataFrame
df = pd.read_csv(StringIO('Data1.csv'), sep='\t')

# Count the occurrences of each vaccine
vaccine_counts = df['VACCINE_NAME'].value_counts()

# Use Seaborn for a more stylish plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

# Bar plot with Seaborn
sns.barplot(x=vaccine_counts.index, y=vaccine_counts.values, palette="viridis")

# Adding data labels
for i, count in enumerate(vaccine_counts.values):
    plt.text(i, count + 0.1, f'{count}', ha='center', va='bottom', fontsize=10, color='black')

# Adding labels and title
plt.title('Vaccine Distribution by Product Name', fontsize=16)
plt.xlabel('Vaccine Name', fontsize=14)
plt.ylabel('Number of Occurrences', fontsize=14)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=12)

# Adding horizontal grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()
plt.savefig('22094300.png', bbox_inches='tight')



#Plot2




# Convert the string data to a DataFrame
df = pd.read_csv(StringIO('Data2.csv'), parse_dates=["Date_reported"])

# Sorting the data by the "New_cases" column for better visualization
df_sorted = df.sort_values(by="New_cases", ascending=False)

# Plotting the bar plot with additional features
plt.figure(figsize=(12, 8))

# Bar for new cases
plt.bar(df_sorted["Country"], df_sorted["New_cases"], color='skyblue', label='New Cases', alpha=0.7)

# Bar for cumulative cases (using a different color)
plt.bar(df_sorted["Country"], df_sorted["Cumulative_cases"], color='lightcoral', label='Cumulative Cases', alpha=0.7)

# Adding data labels
for i, (new_cases, cumulative_cases) in enumerate(zip(df_sorted["New_cases"], df_sorted["Cumulative_cases"])):
    plt.text(i, new_cases + 100, f'{new_cases}', ha='center', va='bottom', color='blue', fontsize=8)
    plt.text(i, cumulative_cases + 100, f'{cumulative_cases}', ha='center', va='bottom', color='red', fontsize=8)

# Adding labels and title
plt.title('New and Cumulative Cases by Country', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Cases', fontsize=14)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)

# Adding a legend
plt.legend()

# Adding horizontal grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()
plt.savefig('22094300.png', bbox_inches='tight')



#Plot3




# Data Location
df = pd.read_csv('Data3.csv')
                 
                 
# Extracting the "TOTAL_VACCINATIONS_PER100" column
vaccinations_per100 = [row[7] for row in df if row[7] is not None]

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(vaccinations_per100, labels=[row[0] for row in df if row[7] is not None], autopct='%1.1f%%', startangle=140)

# Adding a title
plt.title('Percentage of Total Vaccinations Per 100 People by Country')

# Show plot
plt.savefig('22094300.png', bbox_inches='tight')



#Plot4




# Data Location
df = pd.read_csv('Data4.csv')

# Extracting country names and total number of cases
countries = [row[0] for row in df]
total_cases = [row[2] for row in df]

# Set a seaborn style
sns.set(style="whitegrid")

# Plotting the line chart
plt.figure(figsize=(12, 8))
sns.lineplot(x=countries, y=total_cases, marker='o', linestyle='-', color='b', markersize=8)

# Adding labels and title
plt.title('Total Number of Cases by Country', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Total Cases (in millions)', fontsize=14)

# Adding annotations for specific points (e.g., maximum value)
max_value = max(total_cases)
max_index = total_cases.index(max_value)
plt.annotate(f'Max: {max_value:,}', xy=(max_index, max_value), xytext=(max_index, max_value + 1000000),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12, color='red')

# Formatting y-axis ticks with commas
plt.ticklabel_format(axis='y', style='plain', useOffset=False)
plt.yticks(plt.yticks()[0], [f'{int(x):,}' for x in plt.yticks()[0]])

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=12)

# Show plot
plt.tight_layout()

plt.savefig('22094300.png', bbox_inches='tight')

