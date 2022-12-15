from flask import Flask
from memcache_app import memcache
from memcache_app import config
from memcache_app import memcache_routes
webapp = Flask(__name__)

''' Default Type is LRU and default size is 10 MB'''
config.emcache_obj = memcache.LRUMemCache(10)
memcache_routes.startup_app()
