#from gpiozero import MCP3008
#import time
#pot = MCP3008(7)
import numpy as np
pot=np.random.rand()
import js2py
threshold=25



js = """
    import Web3 from 'web3';
    
    const web3 = new Web3('ws://localhost:8546');

      if (typeof window !== 'undefined' && typeof window.web3 !== 'undefined') {
       var web3 = new Web3(window.web3.currentProvider);
      }
      else {
        const provider = new Web3.providers.HttpProvider('rinkeby.infura.io/v3/3d366b121560446f8885ebc007722cdd');
       var web3 = new Web3(provider);

      }

      var abi = [
	{
		"constant": false,
		"inputs": [
			{
				"name": "x",
				"type": "uint256"
			}
		],
		"name": "set",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "share",
				"type": "uint256"
			}
		],
		"name": "updateShares",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "get",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
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
				"name": "addr",
				"type": "address"
			}
		],
		"name": "getShares",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]

      var SharesContract = web3.eth.contract(abi);
      var contractAddress = '0x264771b9c23ca3706ac014db408e0a4f86c02aa8';
      var instance = SharesContract.at(contractAddress);
      var buyerAddress = '0x491179f035fdf219798d186f576abdf842c14ca6';



      instance.getShares(buyerAddress, function (err, res) {
        $('#numShares').text(res.toString())
      })



      function setvalue() {5

        abi = [
	{
		"constant": false,
		"inputs": [
			{
				"name": "x",
				"type": "uint256"
			}
		],
		"name": "set",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "share",
				"type": "uint256"
			}
		],
		"name": "updateShares",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "get",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
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
				"name": "addr",
				"type": "address"
			}
		],
		"name": "getShares",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
      try {

      var contractaddress = '0x67e8ed416798c4826a3e0c45a5915587e2e59f2e';
      var myAbi = web3.eth.contract(abi);
      var myfunction = myAbi.at(contractaddress);

      myfunction.set.sendTransaction(document.getElementById("xvalue").value, { from: web3.eth.accounts[0], gas: 4000000 }, function (error, result) {
      if (!error) {console.log(result);} else {console.log(error);}
      })
      } catch (err) {
      document.getElementById("xvalue").innerHTML = err;
      }
      }

window.onload = function () {
      setvalue();
}

"""
while(True):
    if pot>threshold:(js2py.eval_js(js.replace("document.write", "return ")))

