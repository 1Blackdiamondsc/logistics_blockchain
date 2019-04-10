pragma solidity >=0.4.21 <0.6.0;
contract Shares {
  mapping (address => uint) shares;
 
  function updateShares(uint share) public {


    shares[msg.sender] = getShares(msg.sender) + share;
  }
 
  function getShares(address addr) public view returns(uint) {
    return shares[addr];
  }
}