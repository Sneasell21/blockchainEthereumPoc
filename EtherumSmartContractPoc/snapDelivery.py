import time
import snap_contract_abi ## Application Binary Interface (ABI)
from web3 import Web3, HTTPProvider

contract_address     = '0xB14cdd1bD7D788a1d1BbF00eFCCA9A49E7A94f92'
wallet_private_key   = '6ED5F3804A8386E05425A43A1F9A1E5E240B612297A64FD6845E520CBFA5B976'
wallet_address       = '0x3fEA86d9e8D36C5f0df137C059a17970Dc4054B9'

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/6ca76c853ef24a7bbba88d95385046f2'))

w3.eth.enable_unaudited_features()

contract = w3.eth.contract(address = contract_address, abi = snap_contract_abi.abi)


def broadcast_an_delivery_received(covfefe):

    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = contract.functions.broadcastDelivery(covfefe).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)

    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    tx_receipt = w3.eth.getTransactionReceipt(result)

    count = 0
    while tx_receipt is None and (count < 30):

        time.sleep(10)

        tx_receipt = w3.eth.getTransactionReceipt(result)

        print(tx_receipt)


    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    processed_receipt = contract.events.deliveryBroadcast().processReceipt(tx_receipt)

    print(processed_receipt)

    output = "Address {} broadcasted the received signal: {}"\
        .format(processed_receipt[0].args._snapCustomer, processed_receipt[0].args._comment)
    print(output)

    return {'status': 'added', 'processed_receipt': processed_receipt}

if __name__ == "__main__":
    broadcast_an_delivery_received('Received early in morning')