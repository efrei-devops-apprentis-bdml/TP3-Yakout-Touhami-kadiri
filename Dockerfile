FROM python:3.8 
RUN apt update 
RUN apt install python3   

WORKDIR /Users/yaksouTk/Desktop/DockerFiles/Dockerfile  
COPY tp_devops.py ./ 
COPY requirements.txt . 
RUN pip install -r requirements.txt  

CMD [ "python3", "./tp_devops.py" ]
