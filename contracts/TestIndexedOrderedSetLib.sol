pragma solidity ^0.4.7;


import {IndexedEnumerableSetLib} from "./IndexedEnumerableSetLib.sol";


contract TestIndexedEnumerableSetLib {
  using IndexedEnumerableSetLib for IndexedEnumerableSetLib.IndexedEnumerableSet;

  IndexedEnumerableSetLib.IndexedEnumerableSet theSet;

  bytes32 public lastPop;
  bool public lastAdd;
  bool public lastRemove;

  function size() constant returns (uint) {
    return theSet.size();
  }

  function contains(bytes32 value) constant returns (bool) {
    return theSet.contains(value);
  }

  function indexOf(bytes32 value) constant returns (uint) {
    return theSet.indexOf(value);
  }

  function pop(uint idx) public returns (bytes32) {
    lastPop = theSet.pop(idx);
    return lastPop;
  }

  function remove(bytes32 value) public returns (bool) {
    lastRemove = theSet.remove(value);
    return lastRemove;
  }

  function get(uint idx) public returns (bytes32) {
    return theSet.get(idx);
  }

  function add(bytes32 value) public returns (bool) {
    lastAdd = theSet.add(value);
    return lastAdd;
  }
}
