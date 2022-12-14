gunicorn --bind 0.0.0.0:5000 wsgi_memcache:webapp &
gunicorn --bind 0.0.0.0:5001 wsgi_backend:webapp &

echo "Memcache and backend have been started successfully"