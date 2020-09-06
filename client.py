import random

import grpc
import msg_pb2
import msg_pb2_grpc


class Client:
    def __init__(self, address='localhost:5051'):
        self.address = address

    def open(self):
        self.channel = grpc.insecure_channel(self.address)
        self.stub = msg_pb2_grpc.StorageServiceStub(self.channel)

    def __enter__(self):
        self.open()
        return self

    def close(self):
        self.channel.close()

    def __exit__(self, exc_tpe, exc_value, traceback):
        self.close()

    def __getitem__(self, key: str) -> str:
        return self.stub.Load(msg_pb2.Req(key=key)).value

    def __setitem__(self, key: str, value: str) -> str:
        return self.stub.Save(msg_pb2.Data(key=key, value=value))

    def __delitem__(self, key: str) -> None:
        self.stub.Remove(msg_pb2.Req(key=key))


if __name__ == '__main__':
    with Client('localhost:5051') as db:
        for i in range(10):
            key = str(random.randint(0, 5))

            print(f'before {key} => {db[key]}')
            val = '{:04d}'.format(random.randint(0, 9999))
            db[key] = val
            print(f'set    {key} => {val}')
            print(f'after  {key} => {db[key]}')
            print()
            assert db[key] == val

            del db[key]
            assert db[key] == ''
