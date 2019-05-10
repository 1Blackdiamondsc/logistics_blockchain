pragma solidity >=0.4.21 <0.6.0;
contract Logdemo {
  mapping (address => uint) logdemo;

  uint  v_data;

  function getCount(address addr) public view returns(uint) {
    return logdemo[addr];
  }

  function set(uint x) public {
        v_data = x;
  }

  function updateCount(uint l) public {
    logdemo[msg.sender] = getCount(msg.sender) + l;
  }

  function get() public view returns (uint) {
        return v_data;
  }

  }


