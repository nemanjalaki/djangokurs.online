# Start your image with a node base image
FROM python:3.11-slim

# The /app directory should act as the main application directory
WORKDIR /usr/src/djangokurs.online

# Prevents Python from buffering stdout and stderr
ENV PYTHONBUFFERD 1

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat-traditional

# pip install
RUN pip install --upgrade pip

# Copy the app package and package-lock.json file
COPY requirements.txt requirements.txt

# Install requirements.txt file
RUN pip3 install -r requirements.txt

# copy entrypoint.sh
COPY entrypoint.sh entrypoint.sh
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

# Copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["bash", "entrypoint.sh"]

# Install gunicorn, used to serve app
#CMD gunicorn blog.wsgi:application --bind 0.0.0.0:8001

# informs Docker that the container listens on the specified network ports at runtime
# EXPOSE 8000




# Install node packages, install serve, build the app, and remove dependencies at the end
# RUN pip install -r django/requirements.txt
# RUN pip install uwsgi

# EXPOSE 8089
# Start the app using serve command
# CMD [ "serve", "-s", "build" ]