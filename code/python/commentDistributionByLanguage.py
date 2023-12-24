import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/Big Data Technologies/CSV/languages_csv.txt'

# Read language counts from the file
language_counts = {}
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            language, count = parts
            language_counts[language.lower()] = int(count)
        else:
            language, count = parts[0] + " " +  parts[1], parts[2]
            language_counts[language.lower()] = int(count)

# Calculate the total count
total_count = sum(language_counts.values())

# Identify languages with less than 3% and group them into 'Other'
threshold_percentage = 3
other_count = 0
languages_to_remove = []
for language, count in language_counts.items():
    percentage = (count / total_count) * 100
    if percentage < threshold_percentage:
        other_count += count
        languages_to_remove.append(language)

# Remove languages below the threshold from the original dictionary
for language in languages_to_remove:
    del language_counts[language]

# Add 'Other' category to the dictionary
language_counts['Other'] = other_count

# Capitalize language names
languages = [lang.capitalize() for lang in language_counts.keys()]

# Extracting data for plotting
counts = list(language_counts.values())

# Creating a pie chart
plt.figure(figsize=(10, 6))
plt.pie(counts, labels=languages, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Comment Distribution by Language')

# Display the pie chart
plt.show()