from rest_framework import serializers

from User.models import Myuser
from Event.models import Event
from Event.models import Registration
import base64
import re

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data + b'=' * (-len(data) % 4)) ###
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Myuser
        fields = ('id','firstName','lastName','email', 'username', 'password', 'role')

class EventSerializer(serializers.ModelSerializer):
	Event_image = Base64ImageField(
		max_length=None, use_url=True,
	)
	class Meta:
		model = Event
		fields = ('id','Event_id','Event_name','Event_description','Event_category','Event_start_date','Event_end_date',\
                  'Event_start_time','Event_end_time','Event_location','Allow_registration','Event_image','Adult_ticket_price',\
                  'Child_ticket_price')

class RegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registration
		fields = ('id','Event_name','First_name','Last_name','Email_id','Contact','Address','Total_adult_qty','Total_child_qty')

class EventSerializer2(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = ('id','Event_id','Event_name','Event_description','Event_category','Event_start_date','Event_end_date',\
                  'Event_start_time','Event_end_time','Event_location','Allow_registration','Adult_ticket_price',\
                  'Child_ticket_price')