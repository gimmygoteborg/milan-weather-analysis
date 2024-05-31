# gliu 20240531
# Questions:
# 1. total rainfall year over year
# 2. total number of rainy days yoy
# 3. max daily rainfall yoy

# Source:
# https://www.3bmeteo.com/meteo/milano+linate/storico/201905

import os
import pandas as pd
import mpld3

from superseded.read_csv_files_from_folder import *
from data_reader import read_precipitation_data
from total_precipitation_plotter import plot_total_precipitation
from rainy_days_plotter import plot_rainy_days
from heaviest_rainfall_plotter import plot_heaviest_rainfall  # Import the function

from html_converter import html_converter

# Specify the path to the folder containing the CSV files
# Get the current directory
current_directory = os.path.dirname(__file__)
subfolder_name = "Raw data from 3bmeteo"
folder_path = os.path.join(current_directory, subfolder_name)

# Call the function to read and print the CSV files
read_csv_files_from_folder(folder_path)

# Read precipitation data
precipitation_data = read_precipitation_data(folder_path)

# Plot the heaviest rainfall vs each year
fig_daily_max_precipitation = plot_heaviest_rainfall(precipitation_data)
fig_daily_max_precipitation.savefig("daily_max_precipitation.png")

# Plot total precipitation comparison and save the figure
fig_total_precipitation = plot_total_precipitation(precipitation_data, 70.4)
# historical avg source: https://en.wikipedia.org/wiki/Template:Milan_weatherbox
# fig_total_precipitation.savefig("total_precipitation.png")

# Generate figures for different daily rain thresholds
figures = []
for threshold in [1, 10]:
    fig_rainy_days = plot_rainy_days(precipitation_data, threshold, 9.4)
    # historical avg source: https://en.wikipedia.org/wiki/Template:Milan_weatherbox
    title = f'Rainy Days Comparison (Threshold: {threshold} mm)'
    figures.append((fig_rainy_days, title))
    # Save the figure as a PNG file with the threshold in the filename
    # fig_rainy_days.savefig(f'rainy_days_threshold_{threshold}.png')

# Convert figures to HTML and open in the default web browser
html_converter(fig_total_precipitation, fig_daily_max_precipitation, figures)