from concurrent import futures
import logging
import time

import msg_pb2
import grpc
import msg_pb2_grpc
import msgpack


def make_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s:%(name)s:%(levelname)s: %(message)s',
    )
    logger = logging.getLogger('PyIMDB')

    return logger


logger = make_logger()


class StorageService(msg_pb2_grpc.StorageServiceServicer):
    def __init__(self):
        self.storage = dict()
        self.need_dump = False

    def Save(self, request, context):
        logger.debug(f'save: {request.key} => {request.value}')

        self.storage[request.key] = request.value
        self.need_dump = True

        return msg_pb2.Req(key=request.key)

    def Load(self, request, context):
        value = self.storage.get(request.key, '')
        logger.debug(f'load: {request.key} => {value}')

        return msg_pb2.Data(key=request.key, value=value)

    def Remove(self, request, context):
        logger.debug(f'remove: {request.key}')

        del self.storage[request.key]

        return msg_pb2.Req(key=request.key)

    def dump(self, path: str):
        if not self.need_dump:
            logger.debug('dump: skip')
        else:
            with open(path, 'wb') as f:
                msgpack.pack(self.storage, f)
            self.need_dump = False

    def load_dump(self, path: str):
        try:
            with open(path, 'rb') as f:
                self.storage = msgpack.load(f)
        except:
            logger.info(f'load dump: skip')
            self.storage = dict()
        else:
            logger.info(f'load dump: {len(self.storage)} items')
        self.need_dump = False


class Server:
    def __init__(self, address='localhost:5051', n_workers=10):
        self.service = StorageService()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=n_workers))

        self.address = address
        self.n_workers = n_workers

        msg_pb2_grpc.add_StorageServiceServicer_to_server(
            self.service,
            self.server,
        )

        self.server.add_insecure_port(address)

    def serve_forever(self):
        self.server.start()

        logger.info(
            f'start server on {self.address} with {self.n_workers} workers'
        )

        while True:
            try:
                interval = float(self.service.storage['__config/dump/interval'])
            except:
                interval = 10.0

            time.sleep(interval)

            path = self.service.storage.get('__config/dump/path', './pyimdb.db')

            logger.debug(f'dump: {path} (every {interval}s)')
            self.service.dump(path)

    def stop(self):
        self.server.stop(0)

        logger.info('stop server')


if __name__ == '__main__':
    server = Server()
    server.service.load_dump('./pyimdb.db')

    try:
        server.serve_forever()
    except Exception as e:
        server.stop()
        logger.exception(e)
