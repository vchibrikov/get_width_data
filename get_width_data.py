#import packages
import numpy as np
import os
import cv2
import pandas as pd
import math

# Create an empty DataFrame to store the results
df = pd.DataFrame(columns=['file_name', 'point_1', 'point_2', 'pixel_width', 'width_metric_units'])
output_filename = 'test_data.csv'

# Define the function to handle mouse events
def mouse_callback(event, x, y, flags, params):

    # If left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN and len(params['points']) < 30: # define max of 30 clicks
        
        # Add the point to the list
        params['points'].append((x, y))

        # Track clicks
        print('Filename: ', filename ,' | Click number: ', len(params['points']))

        # Draw a circle at the point
        cv2.circle(params['image'], (x, y), 3, (0, 0, 255), -1)

        # Update the display
        cv2.imshow('image', params['image'])

        # print(params['points'])

        # If the list of points contains a multiple of 2 points, draw a line between them and calculate the mean point
        if len(params['points']) in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]:

            # Define the points
            point1 = params['points'][-2]
            point2 = params['points'][-1]

            # Calculate the mean point
            mean_point = ((point1[0] + point2[0]) // 2, (point1[1] + point2[1]) // 2)

            # Draw a line between the points
            cv2.line(params['image'], point1, point2, (0, 0, 255), 1)

            # Draw a circle at the mean point
            # cv2.circle(params['image'], mean_point, 1, (0, 255, 0), -1)

            # Draw perpendicular
            # Calculate the slope of the line formed by the two points
            slope = ((point1[1] - point2[1]))/((point1[0] - point2[0]))

            # Calculate the negative reciprocal of the slope to get the slope of the perpendicular line
            perpendicular_slope = -1 / slope

            # Definition of the length of the perpendicular line (in pixels)
            perpendicular_length = 150

            # Calculate the coordinates of the two endpoints of the perpendicular line
            x_left = mean_point[0] - (perpendicular_length / 2) * math.cos(math.atan(perpendicular_slope))
            y_left = mean_point[1] - (perpendicular_length / 2) * math.sin(math.atan(perpendicular_slope))
            x_right = mean_point[0] + (perpendicular_length / 2) * math.cos(math.atan(perpendicular_slope))
            y_right = mean_point[1] + (perpendicular_length / 2) * math.sin(math.atan(perpendicular_slope))

            # Draw the perpendicular line
            cv2.line(params['image'], (int(x_left), int(y_left)), (int(x_right), int(y_right)), (0, 255, 0), 1)
            # cv2.line(params['image'], ((x_left), (y_left)), ((x_right), (y_right)), (0, 255, 0), 1)

            # Update the display
            cv2.imshow('image', params['image'])

        if len(params['points']) % 3 == 0:

            # Define the points
            point1 = params['points'][-3]
            point2 = params['points'][-2]  
            point3 = params['points'][-1]

            # Calculate the mean point
            mean_point = ((point1[0] + point2[0]) // 2, (point1[1] + point2[1]) // 2)

            # Draw a line between the points
            cv2.line(params['image'], point3, mean_point, (0, 255, 0), 1)

            # Update the display
            cv2.imshow('image', params['image'])

            # Calculate width in pixels
            pixel_width = round(math.sqrt((point3[0] - mean_point[0])**2 + (point3[1] - mean_point[1])**2),2)
            print('Width in pixels: ', pixel_width)

            # Calculate width in nm
            width_metric_units = round(pixel_width * (---/---),2) # instead of (---/---), insert your parameters of scale in metric units per pixel

            df.loc[len(df)] = [filename_short, mean_point, point3 ,pixel_width, width_metric_units]

            df.to_csv(path + output_filename, index = False)

        ################################################################################################################
        ################ CALCULATING SCALE LENGTH (OPTIONALLY) #########################################################

	# Current code is optional when the scale is known. In case if not, it allows to define scale is there is one on source image
        # # If two points have been selected, calculate the distance
        # if len(params['points']) == 2:

        #     # Define the points
        #     point1 = params['points'][0]
        #     point2 = params['points'][1]

        #     # Calculate the distance
        #     distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

        #     # Draw a line between the points
        #     cv2.line(params['image'], point1, point2, (0, 0, 255), 1)

        #     # Update the display
        #     cv2.imshow("image", params['image'])

        #     df.loc[len(df)] = [filename_short, 'scale' ,distance]

        #     df.to_csv(path + 'scale_values.csv', index = False)

        ################################################################################################################
        ################################################################################################################

# Define the folder containing the images
folder = '/Users/---/Desktop/---/---/---/' 
path = '/Users/---/Desktop/---/---/---/'

# Define the extensions of the image files
extensions = ('.jpeg','.tiff', '.jpg', '.tif')

# Iterate over the images in the folder
for filename in os.listdir(folder):
    if filename.lower().endswith(extensions):

        # filename_short = filename.replace('.jpg', '')
        # filename_short = filename.replace('.tif', '')
        # filename_short = filename.replace('.jpeg', '')
        filename_short = filename.replace('.tiff', '')

        # Load the image
        image = cv2.imread(os.path.join(folder, filename))

        # Create a copy of the image for display purposes
        display_image = image.copy()
        
        # Define the dictionary of parameters to be passed to the mouse callback function
        params = {'image': display_image, 'filename': filename, 'points': []}
        
        # Create a window to display the image
        cv2.namedWindow("image", cv2.WINDOW_FULLSCREEN)

        # Set the mouse callback function
        cv2.setMouseCallback("image", mouse_callback, params)

        # Show the image and wait for user to select points
        cv2.imshow("image", image)
        cv2.setMouseCallback("image", mouse_callback, params)
        cv2.waitKey(0)



