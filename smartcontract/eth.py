import time
from web3 import Web3, HTTPProvider
import contract_abi


w3 = Web3(HTTPProvider('http://rinkeby.infura.io/v3/3d366b121560446f8885ebc007722cdd'))

w3.eth.enable_unaudited_features()

contract_address     = w3.toChecksumAddress('0x4425216fee0fa3fc5a88b6e24908f0c95c16124e')
wallet_private_key   = 'E2A2CD40A71C5A7146D2999EFECBEEF2B17974CD9CF9323E9F8580ACF2794C0E'
wallet_address       = w3.toChecksumAddress('0x491179f035fdf219798d186f576ABDF842C14cA6')
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)


def set(covfefe):
    print("dsd")
    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = contract.functions.set(covfefe).buildTransaction({
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

    processed_receipt = contract.events.set().processReceipt(tx_receipt)

    print(processed_receipt)

    output = "Address {} broadcasted the opinion: {}" \
        .format(processed_receipt[0].args._soapboxer, processed_receipt[0].args._opinion)
    print(output)

    return {'status': 'added', 'processed_receipt': processed_receipt}


set(50)