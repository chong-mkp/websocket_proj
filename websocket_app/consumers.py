import json
from channels.generic.websocket import WebsocketConsumer

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
