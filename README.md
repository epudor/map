Rounded Map Generator

This script creates a map centered on a given location and highlights a circular area with a specified radius.

Requirements:

matplotlib
cartopy
numpy
How to Use:

Modify the script:

Update center_lat and center_lon with your desired center coordinates (latitude and longitude in degrees).
Change radius to set the radius of the highlighted area in meters.
Optionally, define a filename to save the plot as a specific image file (e.g., "my_map.png").
Run the script:

Bash

python rounded_map_generator.py
Output:

The script will generate a map centered on the specified coordinates with a blue circle highlighting the area within the provided radius. By default, the map is saved as "rounded_map.png" in the same directory as the script. If you specified a filename, the map will be saved under that name.

Additional Notes:

This script uses the PlateCarree projection, which is suitable for small areas. For larger regions, consider using a different projection that preserves distances more accurately.
