pragma solidity >=0.4.21 <0.6.0;
contract logistics {
  mapping (address => uint) shares;

  uint  v_data;
 

  function set(uint x) public {
        v_data = x;
    }

  function get() public view returns (uint) {
        return v_data;
    }
  }
}