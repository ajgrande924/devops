#!/bin/bash

# DEBUG COMMAND
# curl --insecure --silent https://hub.docker.com/v2/repositories/ajgrande924/node-libc6-compat-pm2/tags/ | jq '.results[].name'

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
NAME=$(jq '.name' ${SOURCE_DIR}/package.json | sed 's/"//g')
VERSION=$(jq '.version' ${SOURCE_DIR}/package.json | sed 's/"//g')
TAG=$(curl --insecure --silent https://hub.docker.com/v2/repositories/${NAME}/tags/ | jq ".results[].name | select(. == \"${VERSION}\")" | sed 's/"//g')

echo "SOURCE_DIR: ${SOURCE_DIR}"
echo "NAME: ${NAME}"
echo "VERSION: ${VERSION}"
echo "TAG: ${TAG}"

if [ "$VERSION" == "$TAG" ]; then
  echo "Docker tag does exists, do not build / push ..."
else
  echo "Docker tag does not exist, create new build / push ..."
fi
