import json
from channels.generic.websocket import WebsocketConsumer
from graphql import graphql
from graphene import Schema
from websocket_app.schema import Query  


class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
        This method is called when a message is received from the WebSocket.
        It will echo back the message with "123" appended to it and send it back to the client.
        Note: Assuming incoming text_data is a string. If it's a JSON string, we can parse it by json.loads(text_data)
        """
        modified_data = text_data.strip() + "123"

        self.send(text_data=json.dumps(modified_data))

    # def receive(self, text_data):
    #     # Deserialize the received JSON string into a Python dictionary
    #     received_data = json.loads(text_data)

    #     # Extract the GraphQL query from the received data
    #     graphql_query = received_data.get('query')

    #     # Execute the GraphQL query
    #     result = graphql(Schema(query=Query), graphql_query)

    #     # Serialize the result of the query into a JSON-compatible Python object
    #     result_data = {'data': result.data, 'errors': result.errors}

    #     # Convert the serialized data into JSON string
    #     json_data = json.dumps(result_data)

    #     # Send the JSON data as a WebSocket message
    #     self.send(text_data=json_data)
