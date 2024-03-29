import grpc
from concurrent import futures
import time

# import the generated classes
import echo_pb2
import echo_pb2_grpc

import echo


# create a class to define the server functions, derived from
class EchoServicer(echo_pb2_grpc.EchoServicer):

    # the request and response are of the data type
    # echo_pb2.Number
    def Response(self, request, context):
        response = echo_pb2.Set()
        response.value = echo.echo(request.value)
        response.number = echo.echo(request.number)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# to add the defined class to the server
echo_pb2_grpc.add_EchoServicer_to_server(
        EchoServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
