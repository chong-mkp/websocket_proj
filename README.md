# About
Server side event example on Django and Graphql


# To install
* Use cors headers to support connected from other apps such as ReactJS
```
pip3 install django channels daphne django-cors-headers graphql-core graphene-django
```

# To install websocat for testing websocket
```
cargo install websocat
```


# To migrate
```
python3 manage.py makemigrations websocket_app
python3 manage.py migrate
```

# To run servers
* They should use different ports
* They should all be running. 
* Daphne serves websocket requests while Django server serves all the other requests. If you only want to test websocket, please feel free to only run daphne server.
```
daphne -p 8001 websocket_proj.asgi:application
python3 manage.py runserver
```

# Connect to WebSocket server
Open a new terminal and run this
```
websocat ws://127.0.0.1:8001/ws/test/
```


# To add example modal
```
mutation {
  createMyModel(amount: 123) {
    payment {
      id
      amount
    }
  }
}
```


# To query all modal
```
query MyQuery {
  payments {
    id
    amount
  }
}
```
