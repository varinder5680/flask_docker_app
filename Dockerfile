FROM python:3.11-slim
# from capital and first install an image here i install python:3image which is in dockerhub

WORKDIR /app
#set working directory inside the container

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5000

CMD ["python", "app.py"]
