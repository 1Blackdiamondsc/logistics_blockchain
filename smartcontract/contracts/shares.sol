pragma solidity >=0.4.21 <0.6.0;
contract Shares {
  mapping (address => uint) shares;

  uint  v_data;
 
  function updateShares(uint share) public {


    shares[msg.sender] = getShares(msg.sender) + share;
  }
 
  function getShares(address addr) public view returns(uint) {
    return shares[addr];


  function set(uint x) public {
        v_data = x;
    }

  function get() public view returns (uint) {
        return v_data;
    }
  }
}