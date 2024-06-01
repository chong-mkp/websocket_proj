import graphene
from graphene_django.types import DjangoObjectType
from websocket_app.models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        post.save()
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
