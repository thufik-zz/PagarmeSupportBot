import requests,json,time,os,urllib,unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    only_ascii = nfkd_form.encode("ASCII", "ignore")
    return only_ascii.decode("UTF-8").encode("UTF-8")



r = requests.get('https://pagarme.zendesk.com/api/v2/views/52583723/tickets.json',auth=('fellipe.thufik@pagar.me','thufik19'))

jayson = json.loads(r.text)
count = jayson['count']



if count > 0:

	tickets = jayson['tickets']
	file = open("newfile.txt","ar+") 
	readedFile = file.read()
	newTickets = 0

	for ticket in tickets:
		if  not str(ticket['id']) in readedFile:
			
			x =  remove_accents(ticket['subject'])
			print x

			file.write(str(ticket['id']) + ' ')
			if bool(ticket['via']['source']['from']):
				name = '<!here> New Ticket from {0}'.format(ticket['via']['source']['from']['name']) 
			else:
				name = '<!here> New ticket on queue'

			dic = {
				"token" : "xoxp-2465752868-87168214994-124135080481-9c2f8f0ce5fa52664403fe521dcb4e97",
				"username" : "BOT SUPORTE",
				"title" : "Warning",
				"channel" : "testbotzendesk",
				"attachments": [
					{
						"fallback": "New ticket from Andrea Lee - Ticket #1943: Can't rest my password - https://groove.hq/path/to/ticket/1943",
						"pretext": name,
						
						#"title": "Ticket #{0}: {1}".format('z',ticket['subject'].encode('utf-8')),
						"title_link": "https://pagarme.zendesk.com/agent/tickets/{0}".format(ticket['id']),
						"text": "Help! I tried to reset my password but nothing happened!",
						"color": "#7CD197",
						'title' : x,
					}
				]

			}
			##print dic
			queryString  = urllib.urlencode(dic)

			print queryString

			requests.post("https://slack.com/api/chat.postMessage?{0}".format(queryString))

	file.close()

	##if not newTickets == 0:
	##message = "<!here> Tem {0} ticket(s) novo(s) na fila".format(newTickets)



##else:
	##message = "<!here> Nao tem nenhum ticket novo"
	##requests.post("https://slack.com/api/chat.postMessage?token=xoxp-2465752868-87168214994-124135080481-9c2f8f0ce5fa52664403fe521dcb4e97&channel=testbotzendesk&text={0}".format(message))
	##os.remove('newfile.txt')
	##open("newfile.txt","w").close()


