FROM ubuntu:xenial

WORKDIR /app
COPY . /app
RUN mkdir data

RUN apt-get update && apt-get upgrade -y && apt-get install -y git python3-pip python3-dev
# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip==9.0.3 && pip3 install --upgrade setuptools && pip3 install --trusted-host pypi.python.org -r requirements.txt

# -------------- BUILD & INSTALL OPENALPR --------------
# Install prerequisites
RUN apt-get install -y libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev liblog4cplus-dev libcurl3-dev
# If using the daemon, install beanstalkd
RUN apt-get install -y beanstalkd
# Clone the latest code from GitHub
RUN git clone https://github.com/openalpr/openalpr.git

# Setup the build directory
WORKDIR /app/openalpr/src
RUN mkdir build
WORKDIR /app/openalpr/src/build

# setup the compile environment
RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..
# compile the library
RUN make
# Install the binaries/libraries to your local system (prefix is /usr)
RUN make install


WORKDIR /app
RUN cd openalpr/src/bindings/python && python3 setup.py install


# Make port 80 available to the world outside this container
EXPOSE 80


#TODO gunicorn file upload limit, log files etc.
#web: gunicorn app:app --log-file=-
RUN chmod +x /app/run.sh
ENTRYPOINT /app/run.sh