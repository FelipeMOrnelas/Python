import json

d1 = {
    'Pessoa1': {
        'nome':'Felipe',
        'idade':20,
    },
    'Pessoa2': {
        'nome':'Rose',
        'idade':30,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
