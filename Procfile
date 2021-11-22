web: trap '' SIGTERM; gunicorn --pythonpath app/ app:app & bash test.sh & wait -n; kill -SIGTERM -$$; wait
