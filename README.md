## Development
running app outside Docker container

### Setup locally
installs python depedencies, openalpr lib\
./setup_locally.sh

### Run locally
./run_locally.sh


## Deployment

### Build 
docker build -t michalcesek/spz-service:(tag) .\
docker push michalcesek/spz-service


### Run docker container
docker pull michalcesek/spz-service:(tag)\
docker run -d -p 80:80 michalcesek/spz-service:(tag)