# get_width_data

get_width_data.py is a Python script that extracts the width data of a given image file and saves it to a CSV file. This script is designed to work with a variety of image file formats such as JPEG, PNG, and BMP.

# System requirements

- Python 3.5 or higher
- Pillow library (pip install Pillow)

# Usage

Open the terminal and navigate to the directory where get_width_data.py is located.
Run the script using the command python get_width_data.py 
Modify the following lines of the script to specify the folder containing your images (folder) and the folder where your output file will be stored (path):

folder = '/Users/---/Desktop/---/---' 

path = '/Users/---/Desktop/---/---/'

Modify the following line of the script to specify the file extensions of your image files:

extensions = ('.jpeg','.tiff', '.jpg', '.tif')

The script will generate a test_data.csv file, which will contain the following columns: 'file_name', 'point_1', 'point_2', 'pixel_width', 'width_metric_units'.
The 'file_name' column contains the name of the image file, 'point_1' and 'point_2' columns contain start and end points of width calculation, 'pixel_width' column contains the width data in pixels, and the 'width_metric_units' column specifies width in defined metric units.

# License

This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgments

The Pillow library for its image processing capabilities.
