## Development
running app outside Docker container

### Setup locally
installs python depedencies, openalpr lib\
./setup_locally.sh

### Run locally
./run_locally.sh


## Deployment

### Build 
docker build -t michalcesek/spz-service:(tag e.g. '0.1') .\
docker push michalcesek/spz-service


### Run docker container
docker pull michalcesek/spz-service:0.1\
docker run -d -p 80:80 michalcesek/spz-service:0.1