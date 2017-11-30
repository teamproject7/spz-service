# Use an official Python runtime as a parent image
FROM ubuntu:xenial

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y git python3-pip python3-dev openalpr openalpr-daemon openalpr-utils libopenalpr-dev postgresql postgresql-contrib

WORKDIR /opt

RUN git clone https://github.com/openalpr/openalpr.git && cd openalpr/src/bindings/python && python3 setup.py install

WORKDIR /app
# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# postgresql
#TODO
#RUN service postgresql start && su - postgres -c "createdb test; psql -s test" && createdb test && psql -s test <<FOO create user test password 'test'; GRANT ALL PRIVILEGES ON DATABASE test TO test; FOO


#TODO gunicorn file upload limit, log files etc.
#web: gunicorn app:app --log-file=-
#CMD ["python3", "run.py"]
#RUN chmod 755 /app/run.sh
RUN chmod +x /app/run.sh
ENTRYPOINT /app/run.sh