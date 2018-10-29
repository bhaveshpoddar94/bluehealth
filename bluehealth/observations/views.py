from rest_framework import generics, mixins
from permissions import IsOwnerOrReadOnly
from models import Attribute as Observation
from serializers import ObservationSerializer


class ObservationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    # queryset = Device.objects.all()
    serializer_class = ObservationSerializer
    lookup_field = 'pk'
    permissions = [IsOwnerOrReadOnly]

    def get_queryset(self):
        qs = Observation.objects.all()
        type = self.request.query_params.get('type', None)
        return qs.filter(type=type) if type else qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ObservationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Device.objects.all()
    serializer_class = ObservationSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        qs = Observation.objects.all()
        return qs
        


class Mailer:
    """
    Send email messages helper class
    """

    def __init__(self, from_email=None):
        self.connection = mail.get_connection()
        self.from_email = from_email

    def send_messages(self, subject, template, context, to_emails):
        messages = self.__generate_messages(
            subject, template, context, to_emails)
        self.__send_mail(messages)

    def __send_mail(self, mail_messages):
        self.connection.open()
        self.connection.send_messages(mail_messages)
        self.connection.close()

    def __generate_messages(self, subject, template, context, to_emails):
        messages = []
        message_template = get_template(template)
        for recipient in to_emails:
            message_content = message_template.render(context)
            message = EmailMessage(subject, message_content, to=[
                                   recipient], from_email=self.from_email)
            message.content_subtype = 'html'
            messages.append(message)

        return messages
