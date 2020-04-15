from threading import Thread

from django.db import models

# Create your models here.
from pynamodb.attributes import ListAttribute, MapAttribute, NumberAttribute, UnicodeAttribute
from pynamodb.models import Model


#
# class Office(Model):
#     class Meta:
#         table_name = 'OfficeModel'
#         region = 'us-east-2'
#         host = "http://localhost:8000"
#
#     office_id = NumberAttribute(hash_key=True)
#     address = UnicodeAttribute()
#     employee = UnicodeAttribute()
#
#
# if not Office.exists():
#     Office.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
class UserModel(Model):
    """
    A DynamoDB User
    """

    class Meta:
        table_name = 'dynamodb-user_3'
        region = 'us-east-2'

    email = UnicodeAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()


# UserModel.create_table(read_capacity_units=10, write_capacity_units=10)




