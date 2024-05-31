import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_heaviest_rainfall(precipitation_data):
    # Extract the maximum precipitation value for each year
    max_precipitation_per_year = {int(year): df["prec"].max() for year, df in precipitation_data.items()}
    
    # Convert years to integers
    years = list(map(int, max_precipitation_per_year.keys()))

    # Create the figure object
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the heaviest rainfall vs each year as a bar chart
    ax.bar(years, max_precipitation_per_year.values(), color='m')
    ax.set_xlabel('Year')
    ax.set_ylabel('Heaviest One Day Rainfall (mm)')
    ax.set_title('Heaviest Rainfall in May vs Year')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Set x-axis intervals to 1 year
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    plt.tight_layout()
    
    return fig
