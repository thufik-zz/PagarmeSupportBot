import requests,json,time,os,urllib,unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    only_ascii = nfkd_form.encode("ASCII", "ignore")
    return only_ascii.decode("UTF-8").encode("UTF-8")



r = requests.get('https://pagarme.zendesk.com/api/v2/views/39073247/tickets.json',auth=('fellipe.thufik@pagar.me','thufik19'))

jayson = json.loads(r.text)
count = jayson['count']



if count > 0:

	tickets = jayson['tickets']
	file = open("newfile.txt","r+b") 
	readedFile = file.read()
	newTickets = 0

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
				"title" : "Warning",
				"channel" : "testbotzendesk",
				"attachments": [
					{
						"token" : "xoxp-2465752868-87168214994-127188328743-d5591c799a0db4da58d3bbc631fd3367",
						"fallback": "New ticket from Andrea Lee - Ticket #1943: Can't rest my password - https://groove.hq/path/to/ticket/1943",
						"pretext": name,
						"title": "Ticket #{0} : {1}".format(ticket['id'],subject),
						"title_link": "https://pagarme.zendesk.com/agent/tickets/{0}".format(ticket['id']),
						"text": "{0}".format(description),
						"color": "#7CD197",
						"icon_emoji": ":monkey_face:",
						"callback_id" : "https://requestb.in/1mxoztj1",
						"actions": [
                		{
                    		"name": "chess",
                    		"text": "Aceitar",
                    		"type": "button",
                    		"value": "chess"
                		},
                		{
                    		"name": "chess",
                    		"text": "Atendimento",
                    		"type": "button",
                    		"value": "chess"                	
                		}	
					]
						
					}
				]

			}

			x = urllib.urlencode(dic)
			print x

			requests.post("https://hooks.slack.com/services/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",json = dic)

	file.close()


