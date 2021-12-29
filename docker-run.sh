#!/bin/bash
docker run \
    --rm \
    -it \
    -p 8000:8000 \
    --volume $(pwd):/site \
    --volume $(pwd)/content:/input \
    --volume $(pwd)/output:/output \
    --volume $(pwd)/themes/pelican-elegant-custom:/theme \
    pelican_local:v1.0.1 pelican /input -o /output -t /theme -s /site/pelicanconf_2.py

docker run \
    --rm \
    -it \
    -p 8000:8000 \
    --volume $(pwd):/site \
    --volume $(pwd)/content:/input \
    --volume $(pwd)/output:/output \
    --volume $(pwd)/themes/pelican-elegant-custom:/theme \
    pelican_local:v1.0.1 pelican /input -o /output -t /theme -s /site/pelicanconf_2.py -b 0.0.0.0 --listen