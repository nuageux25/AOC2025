#!/bin/bash
docker build -t adventofcode -f ../docker/Dockerfile ..
docker run -it --rm --name adventofcode -e EXO=exo2.py adventofcode
