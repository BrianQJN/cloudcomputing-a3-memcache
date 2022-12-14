sudo kill -9 `sudo lsof -t -i:5000` 2> /dev/null

echo "Memcache has been stopped successfully"