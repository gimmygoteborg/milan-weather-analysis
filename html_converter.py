import matplotlib.pyplot as plt

def html_converter(fig_total_precipitation, fig_daily_max_precipitation, figures):
    """
    Convert the provided figures to HTML and save them to a file, then open the HTML file in the default web browser.

    Parameters:
        fig_total_precipitation: The total precipitation comparison figure.
        figures: A list of tuples containing the other figures and their titles.
    """
    # Save the total precipitation figure as an image
    fig_total_precipitation.savefig('total_precipitation.png')
    fig_daily_max_precipitation.savefig("daily_max_precipitation.png")

    # Write HTML content to a file
    with open('index.html', 'w') as file:
        file.write('<!DOCTYPE html>\n')
        file.write('<title>Milan Linate Airport Historical Rainfall</title>\n')
        file.write('</head>\n<body>\n')
        file.write('<h1>Milan Linate Airport Rainfall Collection Historical Data</h1>\n')

        file.write('<h2>Month of May: Total Precipitation Comparison</h2>\n')
        file.write('<img src="total_precipitation.png" alt="Total Precipitation">\n')

        file.write('<h2>Month of May: Max daily rainfall Comparison</h2>\n')
        file.write('<img src="daily_max_precipitation.png" alt="Heaviest rainfall on a calendar day">\n')

        file.write('<h2>Month of May: Number of Rainy Days Comparison</h2>\n')
        # Iterate over the other figures
        for fig, title in figures:
            # Save each figure as an image
            fig.savefig(f'{title}.png')
            # Write HTML content for each figure
            file.write(f'<h3>{title}</h3>\n')
            file.write(f'<img src="{title}.png" alt="{title}">\n')
        file.write('</body>\n</html>\n')
