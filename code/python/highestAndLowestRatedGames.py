import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
file_path = '/content/drive/MyDrive/Big Data Technologies/CSV/positive_to_negative_csv.txt'

# Read language counts from the file
all_reviews = {}
game_data = {}
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split("|")
        if len(parts) == 2:
            game_name, num_of_reviews = parts
            all_reviews[game_name] = int(num_of_reviews)

for game in all_reviews:
  if game.endswith("not"):
    continue
  sum_of_reviews = all_reviews[game] + all_reviews[game+"not"]
  if sum_of_reviews < 20000:
    continue
  game_data[game] = all_reviews[game] / (sum_of_reviews)

# Sort the games based on review percentages
sorted_games = sorted(game_data.items(), key=lambda x: x[1], reverse=True)

# Extract the top and bottom 15 games
top_15_games = sorted_games[:15]
bottom_15_games = sorted_games[-15:]

# Plotting the bar chart for the top 15 games
top_games, top_percentages = zip(*top_15_games)
plt.barh(top_games, top_percentages, color='green')
plt.xlabel('Positive Review Percentage')
plt.ylabel('Games')
plt.title('Top 15 Games with Highest Positive Review Percentages')
plt.xlim(0, 1)  # Set x-axis limit to represent percentages (0 to 100%)
plt.show()

# Plotting the bar chart for the bottom 15 games
bottom_games, bottom_percentages = zip(*bottom_15_games)
plt.barh(bottom_games, bottom_percentages, color='red')
plt.xlabel('Positive Review Percentage')
plt.ylabel('Games')
plt.title('Bottom 15 Games with Lowest Positive Review Percentages')
plt.xlim(0, 1)  # Set x-axis limit to represent percentages (0 to 100%)
plt.show()
