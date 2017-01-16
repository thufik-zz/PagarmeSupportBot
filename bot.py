import requests,json,time,os,urllib,unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    only_ascii = nfkd_form.encode("ASCII", "ignore")
    return only_ascii.decode("UTF-8").encode("UTF-8")



r = requests.get('https://pagarme.zendesk.com/api/v2/views/39073217/tickets.json',auth=('fellipe.thufik@pagar.me','thufik19'))

jayson = json.loads(r.text)
count = jayson['count']



if count > 0:

	tickets = jayson['tickets']
	file = open("newfile.txt","ab+") 
	readedFile = file.read()
	newTickets = 03

	for ticket in tickets:
		if  not str(ticket['id']) in readedFile:
			
			subject =  remove_accents(ticket['subject'])
			description = remove_accents(ticket['description'])

			file.write(str(ticket['id']) + ' ')
			#if ticket.get('via').get('source').get('from'):
			#	name = '<!here> New Ticket from {0}'.format(ticket['via']['source']['from']['name']) 
			#else:
			#
			name = '<!here> New ticket on queue'

			dic = {
				"username" : "BOT SUPORTE",
				"attachments": [
					{
						"token" : "xoxp-2465752868-87168214994-127188328743-d5591c799a0db4da58d3bbc631fd3367",
						"fallback": "Novo ticket na fila",
						"pretext": name,
						"title": "Ticket #{0} : {1}".format(ticket['id'],subject),
						"title_link": "https://pagarme.zendesk.com/agent/tickets/{0}".format(ticket['id']),
						"text": "{0}".format(description),
						"color": "#7CD197",
						"icon_emoji": ":monkey_face:",
						"callback_id" : "{0}".format(ticket['id']),
						"actions": [
                		{
                    		"name": "btnAceitar",
                    		"text": "Aceitar",
                    		"style" : "primary",
                    		"type": "button",
                    		"value": "1"
                		},
                		{
                    		"name": "btnAtendimento",
                    		"text": "Atendimento",
                    		"style" : "primary",
                    		"type": "button",
                    		"value": "2"                	
                		}	
					]
						
					}
				]

			}

			x = urllib.urlencode(dic)
			print x

			##requests.post("https://hooks.slack.com/services/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",json = dic)
			requests.post("https://hooks.slack.com/services/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",json = dic)
			
	file.close()





