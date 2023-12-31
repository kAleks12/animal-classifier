### Table of contents
- [General info](#general-info)
  * [Description](#description)
  * [Screenshots](#screenshots)
- [Installation](#installation)
- [Configuration](#configuration)
- [Disclaimer](#disclaimer)


# General info

## Description

animal-classifier is a REST API that generates list of text tags based on image of animals using FAST API and YoloV8 from ultralytics!

## Screenshots

-  API has a single endpoint that accepts a file

   
![image](https://github.com/kAleks12/animal-classifier/assets/79469983/fd1144b3-ac5a-49cd-847f-546ba7ca098b)


-  Response schema is simply a list of animal tags found in the uploaded image
  
![image](https://github.com/kAleks12/animal-classifier/assets/79469983/8fe44bf8-8b74-44b9-a81c-ec4a0e93f9af)


-  Now you can compare the tags with the uploaded image ;)

  
![image](https://github.com/kAleks12/animal-classifier/assets/79469983/062dc53e-d957-47cd-9727-4b872e44c830)


# Installation
1. Clone this repo
2. Install python 3.11 or newer
3. Create python venv by running this cli command in project directory:
```
python3 -m venv
```
4. Activate venv by running this cli command in the same directory:
```
venv\Scripts\activate
```
5. Install all required packages by running this cli command inside venv:
```
pip install -r requirements.txt
```
6. Launch the API by running this cli command inside venv:
```
python main.py config.ini logger_config.ini
```

# Configuration
Config file is named `config.ini` and it contains all the changeable settings for the API. Defined parameters are:
* **server** section
  - **host** - host address of the API, default is 127.0.0.1
  - **port** - port of the API, default is 8081
  - **prefix** - prefix of the API, default is "/api/v1"
  - **allow_origins** - list of allowed origins, default is * (all)
  - **allow_methods** - list of allowed origins, default is * (all)
  - **allow_headers** - list of allowed origins, default is * (all)
  - **docs** - enable/disable swagger docs available under `host\port\docs`, default is 1 (on)
  - **redoc** - enable/disable redoc docs available `host\port\redoc`, default is 1 (on)
* **yolo** section
  - **model_weights** - name of the yolov8 to be used, default is yolov8x-cls.pt, make sure to use classifier model (ends with -cls)
  - **img_data_path** - path to the folder with images to be classified, default is ./img_data/
  - **image_threshold** - defines the number of images allowed to exist simultaneously in the yolo predict folder, default is 1000

# Disclaimer
This software does nothing with uploaded data by itself. However, watch out for the fact that ultralytics may use your images for analytics and marketing purposes since their provided package makes post requests to google servers after each model run. 

