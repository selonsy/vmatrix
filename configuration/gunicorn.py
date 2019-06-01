from gevent import monkey
monkey.patch_all()
import multiprocessing
debug = True
loglevel = 'debug'
bind = '172.18.216.226:8282'     # 绑定与Nginx通信的端口
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
workers = 2                 # multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'     # 默认为阻塞模式，最好选择gevent模式

# 运行方法：
# gunicorn -c gunicorn.py izone.wsgi:appliction

# gunicorn --bind unix:/home/selonsy/workspace/vmatrix/vmatrix.gunicorn.socket izone.wsgi:application

# workers是工作线程数，一般设置成：服务器CPU个数 + 1