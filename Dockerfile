FROM python:3
#FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# ADD requirements.txt /
# RUN pip3 install -r requirements.txt

RUN pip install Flask gunicorn requests

# ADD solar.py /
# CMD [ "python", "./solar.py" ]

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 solar:app
