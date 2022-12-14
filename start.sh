gunicorn --bind 0.0.0.0:5000 wsgi_memcache:webapp &

echo "Memcache has been started successfully"