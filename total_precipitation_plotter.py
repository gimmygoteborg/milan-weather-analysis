import matplotlib.pyplot as plt

def plot_total_precipitation(precipitation_data, historical_avg_rainfall=70):
    """
    Plot the total precipitation comparison for each year.

    Parameters:
        precipitation_data (dict): A dictionary where keys are years and values are DataFrames containing the precipitation data for each year.
        historical_avg_rainfall (float): The historical average rainfall threshold.

    Returns:
        matplotlib.figure.Figure: The matplotlib figure object.
    """
    # Calculate total precipitation for each year
    total_precipitation = {int(year): df["prec"].sum() for year, df in precipitation_data.items()}

    # Create the figure object
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the total precipitation comparison
    ax.bar(total_precipitation.keys(), total_precipitation.values(), color='skyblue')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Precipitation (mm)')
    ax.set_title('Total Precipitation Comparison by Year')
    ax.set_xticks(list(total_precipitation.keys()))
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Add horizontal line for historical average rainfall
    ax.axhline(y=historical_avg_rainfall, color='red', linestyle='-', linewidth=2, label=f'Historical Avg Rainfall ({historical_avg_rainfall} mm)')
    ax.legend()  # Show legend

    plt.tight_layout()

    return fig
