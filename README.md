# PyIMDB: Python In-Memory DataBase

In-memory database for python like a Redis(?).
It's my learning sandbox of grpc.


## Usage
### Setup

``` shell
$ git clone https://github.com/macrat/pyimdb.git
$ cd pyimdb
$ pipenv install
```

### Server

``` shell
$ pipenv run server
```

### Client

Use client,

``` shell
$ pipenv run client
```

Or use as library,

``` python
import pyimdb.client


with pyimdb.client.Client() as db:
    db['hello'] = 'world'
    assert db['hello'] == 'world'

    del db['hello']
    assert db['hello'] == ''
```
