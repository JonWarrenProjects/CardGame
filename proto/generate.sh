#!/bin/bash

source ../Server/venv/bin/activate
python -m grpc_tools.protoc -I . --python_out=../Server --grpc_python_out=../Server ./src/GameState.proto