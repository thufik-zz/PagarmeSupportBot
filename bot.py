import requests,json,time,os,urllib,unicodedata,xml.etree.ElementTree as ET

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    only_ascii = nfkd_form.encode("ASCII", "ignore")
    return only_ascii.decode("UTF-8").encode("UTF-8")


configs = ET.parse('config.xml')
username = configs.find('username').text
password = configs.find('password').text

response = requests.get('https://pagarme.zendesk.com/api/v2/views/39073217/tickets.json',auth=(username,password))


jsonReturned = json.loads(response.text)
count = jsonReturned['count']

if count > 0:

	tickets = jsonReturned['tickets']
	file = open("newfile.txt","ab+") 
	readedFile = file.read()
	newTickets = 0

	for ticket in tickets:
		if  not str(ticket['id']) in readedFile:
			
			subject =  remove_accents(ticket['subject'])
			description = remove_accents(ticket['description'])
			name = '<!here> New ticket on queue'

			file.write(str(ticket['id']) + ' ')

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

			requests.post("https://hooks.slack.com/services/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",json = dic)
			##requests.post("https://hooks.slack.com/services/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",json = dic)
			
	file.close()





