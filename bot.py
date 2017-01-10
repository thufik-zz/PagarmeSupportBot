import requests,json,time


r = requests.get('https://pagarme.zendesk.com/api/v2/views/39073217/tickets.json',auth=('fellipe.thufik@pagar.me','thufik19'))

jayson = json.loads(r.text)
count = jayson['count']


if count > 0:

	tickets = jayson['tickets']
	file = open("newfile.txt").read()
	newTickets = 0

	for ticket in tickets:
		if str(ticket['id']) in file:
			print 'x'
		else:
			newTickets = newTickets + 1
			open("newfile.txt","w").write(str(ticket['id']))


	message = "<!here> Olha o zendesk, tem {0} tickets novos".format(newTickets)
	requests.post("https://slack.com/api/chat.postMessage?token=xoxp-2465752868-87168214994-124135080481-9c2f8f0ce5fa52664403fe521dcb4e97&channel=testbotzendesk&text={0}".format(message))

else:
	message = "<!here> Nao tem nenhuma ticket novo"
	requests.post("https://slack.com/api/chat.postMessage?token=xoxp-2465752868-87168214994-124135080481-9c2f8f0ce5fa52664403fe521dcb4e97&channel=testbotzendesk&text={0}".format(message))
	open("newfile.txt","w").close()

