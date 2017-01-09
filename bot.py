import requests,json,time

while(1):
	time.sleep(20)

	r = requests.get('https://pagarme.zendesk.com/api/v2/views/39073217/tickets.json',auth=('fellipe.thufik@pagar.me','thufik19'))

	jayson = json.loads(r.text)
	count = jayson['count']

	if count > 0:
		
		message = "<!here> Olha o zendesk, tem {0} tickets novos".format(count)
		requests.post("https://slack.com/api/chat.postMessage?token=xoxp-2465752868-87168214994-124135080481-9c2f8f0ce5fa52664403fe521dcb4e97&channel=testbotzendesk&text={0}".format(message))



