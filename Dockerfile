FROM python:3.13.1

WORKDIR /app

COPY . .

RUN docker stop my_container

RUN docker rm my_container

RUN docker build -t my_image .

RUN docker run -d --name=my_container -p 80:8000 my_image:latest

RUN pip install -r requirements.txt

CMD ["python", "main.py"]