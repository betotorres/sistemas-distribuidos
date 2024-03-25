import requests

SERVIDOR_1 = 'http://localhost:5000/'


def efetua_deposito(cpf_origem, cpf_destino, valor_transferencia):
    resp = requests.get(f'{SERVIDOR_1}/conta/{cpf_origem}')

    saldo_origem = float(resp.text[2:-2])

    if saldo_origem >= valor_transferencia:
        resp2 = requests.get(f'{SERVIDOR_1}/debito/{cpf_origem}/{valor_transferencia}')

        if resp2.text == '1':
            resp3 = requests.get(f'{SERVIDOR_1}/credito/{cpf_destino}/{valor_transferencia}')
            if resp3.text == '1':
                return 'SUCESSO'
            else:
                resp4 = requests.get(f'{SERVIDOR_1}/conta/{cpf_origem}')
                if resp4.text != resp3.text:
                    resp3 = requests.get(f'{SERVIDOR_1}/credito/{cpf_origem}/{valor_transferencia}')

        
    


efetua_deposito(11111111111, 33333333333, 10)