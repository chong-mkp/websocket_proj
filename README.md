# About
Server side event example on Django and Graphql


# To install
```
pip3 install django graphene-django channels asgiref websockets graphql-ws
```

# To install websocat for testing websocket
```
cargo install websocat
```

# To run server
```
python3 manage.py makemigrations websocket_app
python3 manage.py migrate
daphne websocket_proj.asgi:application
```

# Connect to WebSocket server
Open a new terminal and run this
```
websocat ws://127.0.0.1:8000/ws/posts/
```

# To access GraphQL Playground
```
http://127.0.0.1:8000/graphql/
```

# To add example modal
```
mutation {
  createPost(title: "New Post Title", content: "Lorem ipsum dolor sit amet") {
    post {
      id
      title
      content
    }
  }
}
```


# To query all modal
```
query MyQuery {
  allPosts {
    content
    createdAt
    id
    title
  }
}
```
