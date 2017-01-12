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

	//3444462103 - thufik
	//3473352046 - Kano
	//3511235706 - messina


	function AssignTicket($ticketId, $userId)	{
		$client = new GuzzleHttp\Client();
		$response = $client->put('https://pagarme.zendesk.com/api/v2/tickets/'.$ticketId.'.json', [
			'auth' => [
				'henrique.kano@pagar.me', 
				'dq3iu9MUT4Nv83qQ'
			],
			'json' => [
				'ticket' => [
					'assignee_id' => $userId
				]
			]
		]);
	}

	$data = json_decode(file_get_contents('php://input'), true);

	if ($data["user"]["name"] == "rodrigo.ama") {
		//AssignTicket(,)
	} else if ($data["user"]["name"] == "henrique.kano") {
		AssignTicket('28632','3473352046');

	} else if ($data["user"]["name"] == "thufik") {
		AssignTicket('28632','3444462103');

	} else if ($data["user"]["name"] == "victormessina") {
		//AssignTicket(,'3511235706')

	}

?>