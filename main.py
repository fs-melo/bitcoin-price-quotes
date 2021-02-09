'''
Get Bitcoin Value
http://api.coindesk.com/v1/bpi/currentprice.json
'''

import urllib.request, json, time

def obter_valor():
	try:
		url = "http://api.coindesk.com/v1/bpi/currentprice.json"
		with urllib.request.urlopen(url) as url:
			response = url.read()
			data = json.loads(response.decode('utf-8'))
			valor = float(data['bpi']['USD']['rate'].replace(",", ""))
			t = data['time']['updateduk']
			print(t)
			return valor
	except urllib.error.HTTPError:
		print('URL inexistente!')

def exibir_valores(tempo=1):
	valor = obter_valor()
	nova_cotacao = True
	print('1 Bitcoin vale %f dólares!' % valor)
	while True:

		valor_atual = obter_valor()
		if valor_atual < valor:
			print('---> Preço do Bitcoin caindo: 1 Bitcoin vale %f dólares!' % valor_atual)
			nova_cotacao = True
		elif valor_atual > valor:
			print('---> Preço do Bitcoin subindo: 1 Bitcoin vale %f dólares!' % valor_atual)
			nova_cotacao = True
		else:
			if nova_cotacao == True:
				print('Aguardando uma nova cotação...')
				nova_cotacao = False
		valor = valor_atual
		time.sleep(tempo)

exibir_valores()