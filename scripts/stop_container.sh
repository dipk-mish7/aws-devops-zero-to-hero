#!/bin/bash
set -e

# Stop the running container (if any)
container_id=`docker ps | awk '{{ $print $1 }}'`
docker rm -rf $container_id