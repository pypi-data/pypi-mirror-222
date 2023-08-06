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
                  

            print("Removendo combinações...")   
            for x in id_list:
              
                body = {
                          "id":"e9df4092-54c5-4631-b367-be1f99f76d65",
                          "to":"postmaster@ai.msging.net",
                          "method":"delete",
                          "uri":f"/content/{x}"
                        }
                r = requests.post(self.url, json=body,headers=self.headers)
                response = r.json()
            print("Combinações excluídas com sucesso!")

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


class manager:

  def __init__(self, contract_id, key, combinations):
    self.authorization = key
    self.contract_id = contract_id
    self.combinations = combinations
    self.url = f'https://{self.contract_id}.http.msging.net/commands'

    self.headers = {
            'content-type': 'application/json',
            'Authorization': self.authorization
          }

 
  def prepare_combinations(self):
  
    entity_columns = []
    for c in self.combinations.columns:
      if 'entity' in c:
        entity_columns.append(c)

    def create_list(row):
        return [item for item in row if item != 0]

    self.combinations['ENTIDADE'] = self.combinations[entity_columns].apply(create_list, axis=1)
      
    df = self.combinations[['name','intent','ENTIDADE','answer']]
    return(df)

  def make_body(self):

      df = self.prepare_combinations()
      
      combs = []
      for resp in df.answer.unique():
        question_combs = df[df.answer == resp][['intent','ENTIDADE']]
        combinations = [{"intent": question_combs.intent.tolist()[qc],"entities":question_combs.ENTIDADE.tolist()[qc],"minEntityMatch": len(question_combs.ENTIDADE.tolist()[qc])} for qc in range(len(question_combs))]
        content =  {
                      "id": str(uuid.uuid4()),
                      "to": "postmaster@ai.msging.net",
                      "method": "set",
                      "uri": f"/content/{str(uuid.uuid4())}",
                      "type": "application/vnd.iris.ai.content-result+json",
                      "resource": {
                      "id": str(uuid.uuid4()),
                      "name": df[df.answer == resp].name.iloc[0],
                      "result": {"type": "text/plain", "content": resp},
                      "combinations": combinations
                    }
                }

        combs.append(json.dumps(content))
      return(combs)
      
  def remove_all(self):
    rmv = remove(contract_id=self.contract_id,key=self.authorization)
    rmv.run('delete')
  

  def import_combinations(self, overwrite='n'):


    if overwrite == 'y':
      rmv = remove(contract_id=self.contract_id,key=self.authorization)
      rmv.run('delete')
    else:
      pass

    mylist = self.make_body()
    for item in mylist:
        myrequest = requests.post(self.url, data=item ,headers=self.headers)
        name = json.loads(item)['resource']['name']
        print(f'Importando... {name}')
    print("Importação concluída com sucesso!")
        
 
 