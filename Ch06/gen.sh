#!/bin/bash

# Script to generate grpc server
# run from Ch06 folder with ./gen.sh

python3 -m grpc_tools.protoc \
    -I. \
    --python_out=. \
    --grpc_python_out=. \
    src/server/rides.proto
