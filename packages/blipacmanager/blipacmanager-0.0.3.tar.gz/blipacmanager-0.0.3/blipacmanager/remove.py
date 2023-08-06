from unidecode import unidecode
import numpy as np
import pandas as pd
import requests
import json
import uuid
import ast
import csv

class remove:
 def __init__(self, contract_id, key):
  self.contract_id = contract_id 
  self.authorization = key 
  self.url = f'https://{self.contract_id}.http.msging.net/commands'
  self.headers = {
            'content-type': 'application/json',
            'Authorization': self.authorization
          }


 def run(self, action):

    if action == 'delete':

        response = self.run(action='get')
        id_list = []
        name_list = []

        try:
            content_size = response['resource']['total']
        except KeyError:
            print('Não existe conteúdo nessa base')

        else:
            for i in range(content_size):
                  id_list.append(response['resource']['items'][i]['id'])
                  name_list.append(response['resource']['items'][i]['name'])


            for x in id_list:
              
                body = {
                          "id":"e9df4092-54c5-4631-b367-be1f99f76d65",
                          "to":"postmaster@ai.msging.net",
                          "method":"delete",
                          "uri":f"/content/{x}"
                        }
                r = requests.post(self.url, json=body,headers=self.headers)
                response = r.json()
 

    elif action == 'get':
            body = {
                          "id": 'aa89s7da-b4as85da8as87',
                          "to": 'postmaster@ai.msging.net',
                          "method": fr'{action}',
                          "uri": f'/content'
                        }


            z = requests.post(self.url, json=body,headers=self.headers)
            response = z.json()


    return(response)


