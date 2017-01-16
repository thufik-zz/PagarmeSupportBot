<?php
	require __DIR__ . '/vendor/autoload.php';

	function FindAssigneeId($userEmail) {
		$client = new GuzzleHttp\Client();
		$response = $client->put('http://pagarme.zendesk.com/api/v2/users', [
			'query_params' => [
				'role' => 'agent'
			]
		]);
		
		return array_filter($response, function($agent){
		});
	}

	function AssignTicket($ticketId, $userId){
		$client = new GuzzleHttp\Client();
		$response = $client->put('https://pagarme.zendesk.com/api/v2/tickets/'.$ticketId.'.json', [
			'auth' => [
				'henrique.kano@pagar.me', 
				'dq3iu9MUT4Nv83qQ'
			],
			'json' => [
				'ticket' => [
					'assignee_id' => $userId,
					'status' => 'open'
				]
			]
		]);
	}

	function SendTicketToAtendimento($ticketId){
		$client = new GuzzleHttp\Client();
		$response = $client->put('https://pagarme.zendesk.com/api/v2/tickets/'.$ticketId.'.json', [
			'auth' => [
				'henrique.kano@pagar.me', 
				'dq3iu9MUT4Nv83qQ'
			],
			'json' => [
				'ticket' => [
					'group_id' => '22774519',
				]
			]
		]);		
	}

	function ReplaceSlack($data,$userName,$atendimento = false){
			
			$userName = $data['user']['name'];
			$subject = $data['attachments'][0]['title'];
			$ticketLink = $data['attachments'][0]['title_link'];
			$responseUrl = $data['response_url'];
			$ticketId = $data['callback_id'];
			$token = $data['token'];

			if ($atendimento == true){
				$message = 'O ticket'.$ticketId.'foi enviado para atendimento';
			}else{
				$message = 'O ticket '.$ticketId.' já foi pego pelo '.$userName;
			}

			$client = new GuzzleHttp\Client();

			$response = $client->put($responseUrl,['json' => ['text' => $message,'attachments' => [
						'token' => 'xoxp-2465752868-87168214994-127188328743-d5591c799a0db4da58d3bbc631fd3367',
						'pretext' => 'Texto X',
						'fallback'=> 'qualquer coisa',
						'title' => 'Ufa',
						'title_link' => 'https://pagarme.zendesk.com/agent/tickets/', 
						'text' => 'Pegaram o ticket',
						'color' => '#7CD197']]]);
	}


		$data = json_decode($_POST['payload'],true);
		$userName = $data['user']['name'];
		$action = $data['actions'][0]['value'];
		

		switch ($action) {
    		case 1:
				if ($userName == "rodrigo.ama") {
					AssignTicket($data["callback_id"],"1813524773");
					ReplaceSlack($data,$userName);
				} else if ($userName == "henrique.kano") {
					AssignTicket($data["callback_id"],'3473352046');
					ReplaceSlack($data,$userName);
				} else if ($userName == "thufik") {
					AssignTicket($data["callback_id"],'3444462103');
					ReplaceSlack($data,$userName);
				} else if ($userName == "victormessina") {
					AssignTicket($data["callback_id"],'3511235706');
					ReplaceSlack($data,$userName);
				}
        	break;
    		case 2:
				SendTicketToAtendimento($data["callback_id"]);
				ReplaceSlack($data,$userName,true);
        		break;
		}

	
?>