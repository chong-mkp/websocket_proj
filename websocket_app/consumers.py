import json
from channels.generic.websocket import AsyncWebsocketConsumer
from graphene_django.settings import graphene_settings
from graphql import graphql_sync


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            # Attempt to load the input as JSON
            data = json.loads(text_data)
            query = data.get('query')
            if not query:
                raise ValueError("No query found in the JSON data.")
        except Exception:
            # If JSON loading fails, treat input as a raw GraphQL query string
            query = text_data

        try:
            # schema = graphene_settings.SCHEMA
            # result = graphql_sync(schema, query)
            # content = {
            #     'data': result.data,
            #     'errors': [error for error in result.errors] if result.errors else [],
            # }
            content = {
                'data': query,
                'errors': None,
            }
        except Exception as e:
            content = {'error': str(e)}

        await self.send(text_data=json.dumps(content))
