#!/bin/bash
docker build -t adventofcode -f ../docker/Dockerfile ..
docker run -it --rm --name adventofcode -e EXO=exo4.py adventofcode
