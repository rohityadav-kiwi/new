from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pynamodb.connection import Connection

from .models import UserModel


def create_user():
    """function to create user in database"""
    user = UserModel('test@example.com', first_name='sun', last_name='rise')
    user.save()


# create_user()


def create_table(model_name):
    """function to create table"""
    model_name.create_table(read_capacity_units=10, write_capacity_units=10)


# create_table()

def get_user_object():
    user = UserModel.get('test@example.com')
    print(user)
    context = {
        'user': user
    }
    return JsonResponse(context, safe=False)


# get_user_object()

def update_user():
    user = UserModel.get('test@example.com')
    user.update(
        actions=[
            UserModel.first_name.set('rahul')
        ])


# update_user()

def search():
    for user in UserModel.query('r', UserModel.first_name.startswith('r')):
        print(user.first_name)
#
