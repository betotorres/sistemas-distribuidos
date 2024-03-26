import requests

BB = 'http://localhost:8001/'
CAIXA = 'http://localhost:8002/'


def efetua_deposito(srv_banco_origem, cpf_origem, srv_banco_destino, cpf_destino, valor_transferencia):
    resp = requests.get(f'{srv_banco_origem}/conta/{cpf_origem}')

    saldo_origem = float(resp.text[2:-2])

    if saldo_origem >= valor_transferencia:
        resp2 = requests.get(f'{srv_banco_origem}/debito/{cpf_origem}/{valor_transferencia}')

        if resp2.text == '1':
            resp3 = requests.get(f'{srv_banco_destino}/credito/{cpf_destino}/{valor_transferencia}')
            if resp3.text == '1':
                return 'SUCESSO'
            else:
                resp4 = requests.get(f'{srv_banco_origem}/conta/{cpf_origem}')
                if resp4.text != resp3.text:
                    resp3 = requests.get(f'{srv_banco_origem}/credito/{cpf_origem}/{valor_transferencia}')

        
    


efetua_deposito(BB, 33333333333, CAIXA, 44444444444, 50)