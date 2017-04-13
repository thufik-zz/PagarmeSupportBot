import operator,requests,json,time,os,urllib,unicodedata,xml.etree.ElementTree as ET

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    only_ascii = nfkd_form.encode("ASCII", "ignore")
    return only_ascii.decode("UTF-8").encode("UTF-8")

def send_message_slack(agent):
			
	subject =  remove_accents(ticket['subject'])
	description = remove_accents(ticket['description'])
	name = '<!here> New ticket on queue'

	dic = {
			"username" : "BOT SUPORTE",
			"attachments": [
			{
				"token" : "xoxp-2465752868-87168214994-127188328743-d5591c799a0db4da58d3bbc631fd3367",
				"fallback": "Novo ticket",
				"pretext": name,
				"title": "Ticket #{0} : {1}".format(ticket['id'],subject),
				"title_link": "https://pagarme.zendesk.com/agent/tickets/{0}".format(ticket['id']),
				"text": "{0}".format(description),
				"color": "#7CD197",
				"icon_emoji": ":monkey_face:",
				"callback_id" : "{0}".format(ticket['id']),
				"actions": [
          		{
               		"name": "btnDuvida",
        			"text": "Duvida",
            		"style" : "primary",
            		"type": "button",
            		"value": "1"
        		},
        		{
	           		"name": "btnProblema",
            		"text": "Problema",
            		"style" : "primary",
               		"type": "button",
            		"value": "2"                	
        		},
        		{
            		"name": "btnTarefa",
            		"text": "Tarefa",
            		"style" : "primary",
            		"type": "button",
            		"value": "3"                	
    			},
    			{
            		"name": "btnAtendimento",
            		"text": "Enviar para atendimento",
            		"style" : "primary",
            		"type": "button",
            		"value": "4"  
    			}
				]		
			}
			]
		}

	requests.post("https://hooks.slack.com/services/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",json = dic)
		##requests.post("https://hooks.slack.com/services/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",json = dic)



configs = ET.parse('config.xml')
username = configs.find('username').text
password = configs.find('password').text


response = requests.get('https://pagarme.zendesk.com/api/v2/views/39073217/tickets.json',auth=(username,password))

ticketsMessina = requests.get('https://pagarme.zendesk.com/api/v2/views/55225426/tickets.json',auth=(username,password))

ticketsJack = requests.get('https://pagarme.zendesk.com/api/v2/views/55144686/tickets.json',auth=(username,password))

ticketsThufik = requests.get('https://pagarme.zendesk.com/api/v2/views/56987786/tickets.json',auth=(username,password))

jsonReturned = json.loads(response.text)
jsonMessina = json.loads(ticketsMessina.text)
jsonJack = json.loads(ticketsMessina.text)
jsonThufik = json.loads(ticketsThufik.text)


count = jsonReturned['count']
countMessina = jsonMessina['count']
countJack = jsonJack['count']
countThufik = jsonThufik['count']

dictionaryTickets = {'messina' : countMessina, 'jack' : countJack, 'thufik' : countThufik}

print dictionaryTickets

if count > 0:

	tickets = jsonReturned['tickets']
	file = open("newfile.txt","ab+") 
	readedFile = file.read()
	newTickets = 0

	for ticket in tickets:
		if  not str(ticket['id']) in readedFile:

			file.write(str(ticket['id']) + ' ')

			agent = min(dictionaryTickets.iteritems(), key=operator.itemgetter(1))[0]

			if agent == 'messina':

				dictionaryTickets['messina'] = countMessina + 1

				parametros = {'ticket': {'assignee_id' : '3511235706','status' : 'open'}}

				requests.put('https://pagarme.zendesk.com/api/v2/tickets/'+ str(ticket['id']) + '.json',auth=(username,password),json=parametros)


			elif agent == 'thufik':

				dictionaryTickets['thufik'] = countThufik + 1

				parametros = {'ticket': {'assignee_id' : '3444462103','status' : 'open'}}

				x = requests.put('https://pagarme.zendesk.com/api/v2/tickets/'+ str(ticket['id']) + '.json',auth=(username,password),json=parametros)

				print x.text

			elif agent == 'jack':

				dictionaryTickets['jack'] = countJack + 1

				parametros = {'ticket': {'assignee_id' : '3473352046','status' : 'open'}}

				requests.put('https://pagarme.zendesk.com/api/v2/tickets/'+ str(ticket['id']) + '.json',auth=(username,password),json=parametros)

			send_message_slack(agent)
			
	file.close()





