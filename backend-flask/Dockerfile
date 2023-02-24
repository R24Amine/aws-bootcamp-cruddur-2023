FROM python:3.10-slim-buster

#make a new folder inside the container
WORKDIR /backend-flask
#this contains the libraries we want to install to run the app
COPY requirements.txt requirements.txt

#install python libaries used for the app
RUN pip3 install -r requirements.txt
#. copy everything in the current directory
#. everything in backend-flask (outside the container)
#. everything in backend-flask (inside the container)
COPY . .
#set environment variables inside the container and remain set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}
#Command
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
