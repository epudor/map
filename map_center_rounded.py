import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

def create_rounded_map(center_lat, center_lon, radius, filename):
    # Create a figure and axis
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Set the extent of the map based on the center and radius
    ax.set_extent([center_lon - np.degrees(radius/111000), center_lon + np.degrees(radius/111000), 
                   center_lat - np.degrees(radius/111000), center_lat + np.degrees(radius/111000)])

    # Draw coastline and borders
    ax.coastlines(resolution='10m', color='black', linewidth=1)
    ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)

    # Draw a circle to represent the radius
    circle = plt.Circle((center_lon, center_lat), radius/1000, color='blue', alpha=0.3, transform=ccrs.PlateCarree())
    ax.add_patch(circle)

    # Plot the center
    ax.plot(center_lon, center_lat, marker='o', color='red', markersize=5, transform=ccrs.PlateCarree())

    # Add gridlines
    ax.gridlines(draw_labels=True)

    # Set title
    ax.set_title('Map with Rounded Borders')

    # Save the plot to a file
    plt.savefig(filename)

    # Close the plot
    plt.close()

# Center coordinates and radius in meters
center_lat = 40.512175
center_lon = -3.673938
radius = 2000

# File name to save the plot
filename = 'C:\\Users\\z\\Desktop\\Real Estate\\Promora\\Datos\\csv\\rounded_map.png'

# Create the map and save it
create_rounded_map(center_lat, center_lon, radius, filename)
