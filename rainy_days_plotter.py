import matplotlib.pyplot as plt

def plot_rainy_days(precipitation_data, threshold=3, average_threshold=9.4):
    """
    Plot the number of rainy days comparison for each year with a specified threshold and average threshold.

    Parameters:
        precipitation_data (dict): A dictionary where keys are years and values are DataFrames containing the precipitation data for each year.
        threshold (float): The threshold value for considering a day as rainy (default is 3 mm).
        average_threshold (float): The threshold value for the average number of rainy days (default is 9.4).
    """
    # Count the number of rainy days for each year based on the threshold
    rainy_days = {int(year): (df["prec"] > threshold).sum() for year, df in precipitation_data.items()}

    # Create the figure object
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the number of rainy days comparison
    ax.bar(rainy_days.keys(), rainy_days.values(), color='lightgreen')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Rainy Days (> {} mm)'.format(threshold))
    ax.set_title('Number of Rainy Days (> {} mm) Comparison by Year'.format(threshold))  # Include threshold in title
    ax.set_xticks(list(rainy_days.keys()))
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Add horizontal line for average rainy days if threshold is 1
    if threshold == 1:
        ax.axhline(y=average_threshold, color='red', linestyle='-', linewidth=2, label=f'Average Rainy Days ({average_threshold:.2f})')
        ax.legend()  # Show legend

    plt.tight_layout()

    return fig
