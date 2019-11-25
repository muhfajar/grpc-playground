import grpc

# import the generated classes
import echo_pb2
import echo_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = echo_pb2_grpc.EchoStub(channel)

# create a valid request message
text = echo_pb2.Set(value='Hello, world!')

# make the call
response = stub.Response(text)

print(response.value)
