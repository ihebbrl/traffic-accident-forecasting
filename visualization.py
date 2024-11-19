import matplotlib.pyplot as plt

def plot_category_accidents(category_accidents, save_path='images/category_accidents.png'):
    plt.figure(figsize=(10, 6))
    category_accidents.plot(kind='bar')
    plt.title("Total Number of Accidents per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Accidents")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_alkohol_accidents(alkohol_dt, january_points, save_path='images/alkohol_accidents.png'):
    plt.figure(figsize=(12, 6))

    # Plot the alcohol-related accidents as a line plot
    alkohol_dt['Value'].plot(kind='line', title='Number of Alcohol-Related Accidents Over Time', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Number of Accidents')

    # Plot the January points as a scatter plot
    plt.scatter(january_points.index, january_points['Value'], color='red', label='January Points')

    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()