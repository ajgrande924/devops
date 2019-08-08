# docker
> docker configuration files

### notes

  - Jenkins is an open source automation tool written in java.
  - CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development.

### usage

```sh
# jenkins

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

```sh
# registry

# generate certs
./scripts/gen_certs.sh

cd registry

# check catalog
curl --insecure https://localhost/v2/_catalog
curl --cacert ../nginx/certs/ca.crt  https://localhost/v2/_catalog

# garbage collect
docker exec registry bin/registry garbage-collect --dry-run /etc/docker/registry/config.yml
```

```sh
# x509: certificate signed by unknown authority

# https://docs.docker.com/engine/security/certificates/
# https://docs.docker.com/registry/recipes/nginx/

sudo mkdir -p /etc/docker/certs.d/<private_registry_url>

# copy certificates
sudo ln -s <path_to_cert> /etc/docker/certs.d/<private_registry_url>/ca.crt
sudo ln -s <path_to_cert> /etc/docker/certs.d/<private_registry_url>/client.cert
sudo ln -s <path_to_key> /etc/docker/certs.d/<private_registry_url>/client.key

# restart docker
sudo systemctl restart docker
```