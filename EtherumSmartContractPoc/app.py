import time
import contract_abi ## Application Binary Interface (ABI)
from web3 import Web3, HTTPProvider

contract_address     = '0x6F143B784D474D3e5F87E4C3543d3a0370CfDd78'
wallet_private_key   = '6ED5F3804A8386E05425A43A1F9A1E5E240B612297A64FD6845E520CBFA5B976'
wallet_address       = '0x3fEA86d9e8D36C5f0df137C059a17970Dc4054B9'

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/6ca76c853ef24a7bbba88d95385046f2'))

w3.eth.enable_unaudited_features()

contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)

def send_ether_to_contract(amount_in_ether):

    amount_in_wei = w3.toWei(amount_in_ether,'ether');

    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = {
            'to': contract_address, # send to
            'value': amount_in_wei, # how much we are sending Wei
            'gas': 2000000, # computational effort that goes into executing a transaction on Etherum
            'gasPrice': w3.toWei('40', 'gwei'), # how much we are willing to pay
            'nonce': nonce, # proof of work , prevent double spending
            'chainId': 3 # Etherum Network chain ID Ropsten is 3
    }

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction) ## transaction unique hash useful to query whether
    # transaction has been included in a block or not.

    txn_receipt = None

    count = 0
    ## check if the tx is included into a block, receive a receipt
    while txn_receipt is None and (count < 30):

        txn_receipt = w3.eth.getTransactionReceipt(txn_hash)

        print(txn_receipt)

        time.sleep(10)


    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}


def check_whether_address_is_approved(address):

    return contract.functions.isApproved(address).call()


def broadcast_an_opinion(covfefe):

    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = contract.functions.broadcastOpinion(covfefe).buildTransaction({
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

    processed_receipt = contract.events.OpinionBroadcast().processReceipt(tx_receipt)

    print(processed_receipt)

    output = "Address {} broadcasted the opinion: {}"\
        .format(processed_receipt[0].args._soapboxer, processed_receipt[0].args._opinion)
    print(output)

    return {'status': 'added', 'processed_receipt': processed_receipt}

if __name__ == "__main__":

    send_ether_to_contract(0.03)

    is_approved = check_whether_address_is_approved(wallet_address)
    
    print(is_approved)

    broadcast_an_opinion('Despite the Constant Negative Press')