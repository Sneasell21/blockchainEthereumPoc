abi = """ [
	{
		"constant": true,
		"inputs": [],
		"name": "getCurrentComment",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_comment",
				"type": "string"
			}
		],
		"name": "broadcastDelivery",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_snapCustomer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_comment",
				"type": "string"
			}
		],
		"name": "deliveryBroadcast",
		"type": "event"
	}
] """