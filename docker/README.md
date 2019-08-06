# docker
> docker configuration files

### notes

  - Jenkins is an open source automation tool written in java.
  - CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development.

### usage

```sh
# generate certs
./scripts/gen_certs.sh

# start jenkins @https://localhost
cd jenkins
docker-compose up -d

# start jenkins_blue_ocean @ https://localhost
cd jenkins_blue_ocean
docker-compose up -d

# remove certs
rm -rf nginx/certs
```