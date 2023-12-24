import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/Big Data Technologies/CSV/recieved_game_for_free_csv.txt'

# Received for free positive percentage
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

file_path = '/content/drive/MyDrive/Big Data Technologies/CSV/paid_for_game_csv.txt'

# Paid for game positive percentage
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

# Sort the games based on review percentages
top_paid_games = sorted(paid_for_game_reviews_percentages.items(), key=lambda x: x[1], reverse=True)[:15]

# Extract game names and percentages for top paid games
paid_game_names, paid_percentages = zip(*top_paid_games)

# Get the free equivalents for the top paid games
free_equivalents = {game: received_for_free_reviews_percentages.get(game, 0) for game in paid_game_names}

# Plotting the stem plot for top paid and free equivalent games on the same graph
plt.figure(figsize=(12, 8))  # Adjust the figure size
plt.stem(paid_game_names, paid_percentages, basefmt="k-", linefmt="b-", markerfmt="bo", label='Top Paid Games')
plt.stem(paid_game_names, free_equivalents.values(), basefmt="k-", linefmt="g-", markerfmt="go", label='Free Equivalents')

plt.title('Top 15 Paid Games Reviews and Their Free Equivalents')
plt.xlabel('Games')
plt.ylabel('Positive Review Percentage')

# Rotate x-axis labels for better readability
plt.xticks(rotation='vertical')

plt.legend(loc='center right')

# Show the plot
plt.show()

# Sort the games based on review percentages
top_received_for_free_games = sorted(received_for_free_reviews_percentages.items(), key=lambda x: x[1], reverse=True)[:15]

# Extract game names and percentages for top paid games
received_for_free_game_names, received_for_free_games_percentages = zip(*top_received_for_free_games)

# Get the free equivalents for the top paid games
paid_equivalents = {game: paid_for_game_reviews_percentages.get(game, 0) for game in received_for_free_game_names}

# Plotting the stem plot for top paid and free equivalent games on the same graph
plt.figure(figsize=(12, 8))  # Adjust the figure size
plt.stem(received_for_free_game_names, received_for_free_games_percentages, basefmt="k-", linefmt="b-", markerfmt="go", label='Top Received for Free Games')
plt.stem(received_for_free_game_names, paid_equivalents.values(), basefmt="k-", linefmt="g-", markerfmt="bo", label='Paid Equivalents')

plt.title('Top 15 Received for Free Games Reviews and Their Paid Equivalents')
plt.xlabel('Games')
plt.ylabel('Positive Review Percentage')

# Rotate x-axis labels for better readability
plt.xticks(rotation='vertical')

plt.legend(loc='center right')

# Show the plot
plt.show()
