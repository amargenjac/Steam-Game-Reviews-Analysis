import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from google.colab import drive
drive.mount('/content/drive')

# Received for free positive percentage
file_path = '/content/drive/MyDrive/Big Data Technologies/CSV/recieved_game_for_free_csv.txt'

# Read language counts from the file
all_reviews = {}
received_for_free_reviews_percentages = {}
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split("|")
        if len(parts) == 2:
            game_name, num_of_reviews = parts
            all_reviews[game_name] = int(num_of_reviews)

for game in all_reviews:
  if game.endswith("notrecommendedandfree"):
    continue
  try:
    sum_of_reviews = all_reviews[game] + all_reviews[game+"notrecommendedandfree"]
  except:
    sum_of_reviews = all_reviews[game]
  received_for_free_reviews_percentages[game] = all_reviews[game] / (sum_of_reviews)

# Paid for game positive percentage
file_path = '/content/drive/MyDrive/Big Data Technologies/CSV/paid_for_game_csv.txt'

# Read language counts from the file
all_reviews = {}
paid_for_game_reviews_percentages = {}
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split("|")
        if len(parts) == 2:
            game_name, num_of_reviews = parts
            all_reviews[game_name] = int(num_of_reviews)

for game in all_reviews:
  if game.endswith("notrecommendedandpaid"):
    continue
  try:
    sum_of_reviews = all_reviews[game] + all_reviews[game+"notrecommendedandpaid"]
  except:
    sum_of_reviews = all_reviews[game]
  paid_for_game_reviews_percentages[game] = all_reviews[game] / (sum_of_reviews)

# Extract the common games
common_games = set(paid_for_game_reviews_percentages.keys()) & set(received_for_free_reviews_percentages.keys())

# Create lists of ratings for common games
purchased_ratings = [paid_for_game_reviews_percentages[game] for game in common_games]
free_ratings = [received_for_free_reviews_percentages[game] for game in common_games]

# Calculate the Pearson correlation coefficient
correlation_coefficient, _ = pearsonr(free_ratings, purchased_ratings)

# Plotting the scatter plot
plt.scatter(purchased_ratings, free_ratings, color='blue')
plt.xlabel('Percentage of Positive Ratings for Purchased Games')
plt.ylabel('Percentage of Positive Ratings for Free Games')
plt.title('Correlation Between Purchased and Free Game Ratings')
plt.grid(True)

# Show the plot
plt.show()

print(f"Pearson Correlation Coefficient: {correlation_coefficient:.2f}")