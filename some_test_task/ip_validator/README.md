IP Validator

built: docker build . -t test-ip_validator
run: docker run -d --name test-ip_validator test-ip_validator

all: docker build . -t test-ip_validator | docker run -d --name test-ip_validator test-ip_validator