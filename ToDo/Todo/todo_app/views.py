from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
import os

user_api = os.getenv('docker_user')
pass_api = os.getenv('docker_pass')
class index(generics.ListAPIView):
    try:
        response = requests.get("http://userservice-container:5000/users/",auth = (user_api, pass_api)).json()    
    except requests.exceptions.RequestException as e:
        response = 'No reponse'

     
    def get(self, request, *args, **kwargs):
        response = {'Success': self.response}
        return Response(response)

class Project(generics.ListAPIView):
    try:
        response = requests.get('http://userservice-container:5000/project/',auth = (user_api, pass_api)).json()    
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the pong service.')
        response = 'No reponse'
    
    def get(self,request, *args, **kwargs):
        response = {'Success': self.response}
        return Response(response)

class Project_by_user(generics.ListAPIView):
    try:    
        user_data = requests.get('http://userservice-container:5000/users/',auth = HTTPBasicAuth(user_api, pass_api)).json()    
    except requests.exceptions.RequestException as e:
        response = 'No reponse'
    try:
        project_data = requests.get('http://userservice-container:5000/project/',auth = HTTPBasicAuth(user_api, pass_api)).json()    
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the pong service.')
        response = 'No reponse'
    def get(self,request,user, *args, **kwargs):
        for i in self.user_data:
            if i['username'] == user:
                uid = i['id']
                break
        
        d = []
        for j in self.project_data:
            if j['user'] == uid:
                d.append(j)

        response = {'Success': d}
        return Response(response)

