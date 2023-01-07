# Setting up Backend

### Install Depedencies


* Redis
* PostgreSQL
* Python 3.10.x


### Installing psycopg2
```
LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib
```

### Development

#### Client

```
yarn dev --hostname 0.0.0.0
```


#### Server
```
PSQL_URL='postgresql://jbcurtin:password@localhost:5432/sustainability-page' ./manage.py runserver
```

#### Running Tests


```
cd sustainability_tests/
pytest test_webservice.py
```


#### Product Outline

When something is updated, find viewed shops simular by user and push a shop to the user
If a user is an a given area and we know know that a product maybe interesting to them, having a push notification
to with those details.
