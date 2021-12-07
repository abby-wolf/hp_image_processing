# Food-Based Image Processing
## Overview
This project provides an image classification system which can identify the follow food items:
  1. Chicken Nuggets
  2. Chicken Patties
  3. Hash Browns
  4. Shoestring Fries

The model works through the use of transfer learning on the MobileNet image classification system.

## Project Contents
The project includes working classification model, but also includes everything you would need to create a new one, including the training algorithm and a basic food dataset. The trained model can be found in the saved_model directory, the training algorithm can be found in the system_training directory, and the dataset can be found in the dataset directory. Of note, the training algorithm code is optimized to work using Google Colab and TensorFlow v1. Attempting to run the code in any other environment (or on any other version of tensorflow) may result in errors. While the code should be functional in TensorFlow v2, it has not beem tested in that environment. If the code cannot be run on Google Colab, it is important to ensure that h5py v2.10.0 is used. Else, the save and load functions for the system may fail. Use ```pip install 'h5py == 2.10.0' --force-reinstall``` in the command line to ensure the proper version of h5py is installed. 

## Nvidia Jetson Nano Functionality
The project also includes directories which allow the trained system to function on the Nvidia Jetson Nano development board. These files can be found in the jetson_compatibility directory. In order to run this code on the Jetson Nano, you must use a CSI camera. The code is not optimized for USB cameras. Some edits to the ```PATH``` variables may be needed in order to run this code. Be sure the paths in the code match to the paths you are using in the Nano's Linux file system.

## Collaborators
* @IndiansFan25

## Helpful Links
* [Jetson Nano Bringup](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit) -- note: the link to the 2GB Nano Flash image is incorrect, you can find the correct image [here](https://developer.nvidia.com/embedded/downloads#?search=sd)
* [Jetson Nano CSI Camera Interfacing](https://developer.nvidia.com/embedded/learn/tutorials/first-picture-csi-usb-camera)
* [MobileNet](https://medium.com/@godeep48/an-overview-on-mobilenet-an-efficient-mobile-vision-cnn-f301141db94d)
