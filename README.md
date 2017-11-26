### Build 
docker build -t spz-service .

### Run docker container
docker run --env-file .env -p 4000:80 test-spz:latest

### Run locally
./run_locally.sh
