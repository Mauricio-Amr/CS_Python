import json

d1 = {'Pessoa1':{
    'nome' : 'luiz',
    'idade' : 25,
    },
    'Pessoa2':{
     'nome':'Rose',
        'idade' : 30,
    },
      }

d1_jason = json.dumps(d1,indent=True)

with open('abc.json','w+') as file:
    file.write(d1_jason)

print(d1_jason)
