from flask import Flask
import threading
webapp = Flask(__name__)

from backend_app import main
from AWS_Log_operator import thread_stats

th = threading.Thread(target=thread_stats)
th.start()