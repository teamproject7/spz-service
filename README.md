## Development
running app outside Docker container

### Setup locally
installs python depedencies, openalpr lib\
./setup_locally.sh

### Run locally
./run_locally.sh


## Deployment

### Build 
docker build -t spz-service .

### Run docker container
docker run --env-file .env -p 4000:80 spz-service:latest