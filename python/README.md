# gRPC Python Playgorund

Prerequisite:
- pipenv

How-to:
- Install all dependencies using `pipenv install`
- Activate virtual env using `pipenv shell`
- Generate pb2 file after updating proto file using `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. echo.proto`
- Run server `python server.py`
- Run client `python client.py`