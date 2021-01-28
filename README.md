# flask-socketio


### Flask_socketio 测试 Demo


Flask-SocketIO使Flask应用程序可以访问客户端和服务器之间的低延迟双向通信。客户端应用程序可以使用 Javascript，C ++，Java和Swift中的任何SocketIO官方客户端库，或任何兼容的客户端来建立与服务器的永久连接。

#### 项目依赖：

```
bidict==0.21.2
certifi==2020.12.5
click==7.1.2
dnspython==1.16.0
eventlet==0.30.0
Flask==1.1.2
Flask-gzip==0.2
Flask-SocketIO==4.3.2
greenlet==1.0.0
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
python-engineio==3.14.2
python-socketio==4.6.1
six==1.15.0
Werkzeug==1.0.1
```


> `Flask-SocketIO==4.3.2` 一定是这个版本，如果版本太高，项目有可能执行不成功。以上的项目依赖亲测是可以使用的。

#### 要求：

Flask-SocketIO与Python 3.6+兼容。可以从以下三个选项中选择此程序包所依赖的异步服务：

- [eventlet](http://eventlet.net/)是性能最好的选项，并支持长轮询和WebSocket传输。
- 许多不同的配置都支持[gevent](http://www.gevent.org/)。gevent软件包完全支持长轮询传输，但是与eventlet不同，gevent不具有本机WebSocket支持。要增加对WebSocket的支持，目前有两个选择。安装[gevent-websocket](https://pypi.python.org/pypi/gevent-websocket/) 软件包可以为gevent添加WebSocket支持，或者可以使用带有WebSocket功能的[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) Web服务器。gevent的使用也是一种性能选择，但比eventlet略低。
- 也可以使用基于Werkzeug的Flask开发服务器，但要注意的是，它缺乏其他两个选项的性能，因此只能用于简化开发工作流程。此选项仅支持长轮询传输。

该扩展会根据安装的内容自动检测要使用的异步框架。优先选择eventlet，后跟gevent。对于gevent中的WebSocket支持，首选uWSGI，其次是gevent-websocket。如果既未安装eventlet也未安装gevent，则使用Flask开发服务器。

如果使用多个进程，则进程将使用消息队列服务来协调诸如广播之类的操作。支持的队列是 [Redis](http://redis.io/)，[RabbitMQ](https://www.rabbitmq.com/)， [Kafka](http://kafka/apache.org/)以及[Kombu](http://kombu.readthedocs.org/en/latest/)软件包支持的任何其他消息队列 。

在客户端，可以使用官方的Socket.IO Javascript客户端库建立与服务器的连接。也有使用Swift，Java和C ++编写的官方客户端。只要非正式客户端实现[Socket.IO协议](https://github.com/socketio/socket.io-protocol)，它们也可能起作用 。的[python-socketio](https://github.com/miguelgrinberg/python-socketio) 封装包括Python客户端。



**[[Flask_socketio官方文档地址](https://flask-socketio.readthedocs.io/en/latest/)]**



本Demo是经过我测试，能够正常使用，具体安装步骤如下：

```
1、执行 pip install -r requirements.txt
2、执行 python application.py
3、访问地址 http://127.0.0.1:8888或者http://localhost:8888/
```

