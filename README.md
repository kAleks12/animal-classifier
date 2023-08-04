### Table of contents
- [General info](#general-info)
  * [Description](#description)
  * [Screenshots](#screenshots)
- [Installation](#installation)
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
4. Install all required packages by running this cli command in project directory:
```
pip install -r requirements.txt
```
5. Launch the API by running this cli command in the same directory as before:
```
python3 main.py config.ini logger_config.ini
```


# Disclaimer
This software does nothing with uploaded data by itself. However, wath out for the fact that ultralytics may use your images for analytics and marketing purposes since their provided package makes post requests to google servers after each model run. 

