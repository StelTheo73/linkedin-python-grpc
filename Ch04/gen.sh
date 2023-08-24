#!/bin/bash

# Script to generate grpc server
# run from Ch04 folder with ./gen.sh

python3 -m grpc_tools.protoc \
    -I. \
    --python_out=. \
    --grpc_python_out=. \
    server/rides.proto
