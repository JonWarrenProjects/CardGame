#!/bin/bash

source ../Server/venv/bin/activate
python -m grpc_tools.protoc -I . --python_out=../Server --grpc_python_out=../Server ./comms/GameState.proto
protoc -I . --csharp_out=../Client/ConsoleClient --grpc_out=../Client/ConsoleClient --plugin=protoc-gen-grpc=/home/jon/Projects/CardGame/Client/ConsoleClient/packages/Grpc.Tools.2.28.1/tools/linux_x86/grpc_csharp_plugin ./comms/GameState.proto