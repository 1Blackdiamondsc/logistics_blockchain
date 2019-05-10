var Shares = artifacts.require('logdemo')

module.exports = function (deployer, network, accounts) {
  deployer.deploy(Shares)
}
