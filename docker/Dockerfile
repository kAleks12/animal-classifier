FROM python:3.11-bullseye
WORKDIR /animal-classifier
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY  main.py docker/config/config.ini logger_config.ini ./
COPY ../src src
EXPOSE 8081
CMD ["python3", "main.py", "config.ini", "logger_config.ini"]