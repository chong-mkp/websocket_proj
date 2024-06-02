import graphene
from graphene_django.types import DjangoObjectType
from websocket_app.models import Payment


class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment


class Query(graphene.ObjectType):
    payments = graphene.List(PaymentType)

    def resolve_payments(self, info):
        return Payment.objects.all()


class CreatePayment(graphene.Mutation):
    class Arguments:
        amount = graphene.Float(required=True)

    payment = graphene.Field(PaymentType)

    def mutate(self, info, amount):
        payment = Payment.objects.create(amount=amount)
        return CreatePayment(payment=payment)


schema = graphene.Schema(query=Query, mutation=graphene.ObjectType('Mutation', create_payment=CreatePayment))
