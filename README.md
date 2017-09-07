# Django-Elasticsearch-demo
You need install Elasticsearch 5

# Install
1) source .env/bin/activate
2) python manage.py migrate
3) python manage.py createsuperuser
4) python manage.py shell

python manage.py
bulk_indexing()

And them add data in database.
To find use params 'q'. Example:
http://127.0.0.1:8889/?q=text
