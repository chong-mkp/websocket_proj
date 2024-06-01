# In myproject/consumers.py

from channels.generic.websocket import WebsocketConsumer
import json
import requests

class PostConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']

        if message_type == 'query_posts':
            self.query_posts()

    def query_posts(self):
        # Define your GraphQL query
        query = '''
            query {
            allPosts {
                id
                title
                content
                createdAt
            }
            }
        '''

        # Make a POST request to the GraphQL endpoint
        graphql_endpoint = 'http://127.0.0.1:8000/graphql/'
        response = requests.post(graphql_endpoint, json={'query': query})

        if response.status_code == 200:
            # If the request is successful, send the query result back to the WebSocket client
            self.send(text_data=json.dumps({
                'type': 'query_result',
                'data': response.json()['data'],
            }))
        else:
            # If the request fails, send an error message back to the WebSocket client
            self.send(text_data=json.dumps({
                'type': 'query_error',
                'message': 'Failed to execute GraphQL query',
            }))
