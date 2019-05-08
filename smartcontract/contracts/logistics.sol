pragma solidity >=0.4.21 <0.6.0;
contract Logistics {
  mapping (address => uint) logistics;

  uint  v_data;

  function getCount(address addr) public view returns(uint) {
    return logistics[addr];
  }

  function set(uint x) public {
        v_data = x;
  }

  function updateCount(uint logistics) public {
    logistics[msg.sender] = getCount(msg.sender) + logistics;
  }

  function get() public view returns (uint) {
        return v_data;
  }

  }


