# syntax=docker/dockerfile:1

# select base image to use
FROM python:3.9.20

# create working directiory in the container
WORKDIR /web-app

# copy requirements.txt file to the new working directory
COPY requirements.txt /web-app/

# install all dependencies from the requirements.txt first
RUN pip3 install --no-cache-dir -r requirements.txt

# copy wab-app.py to the working directory
COPY web-app.py /web-app/

# set port on which Django server is to be exposed
EXPOSE 5000 

# run the web-application from the cli
CMD [ "python3", "web-app.py"]