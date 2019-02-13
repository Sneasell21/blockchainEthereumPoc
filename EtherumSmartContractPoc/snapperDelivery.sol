pragma solidity ^0.4.25;

contract SnapDeliveryContract { 

  // This dictionary will store the address of the received delivery notification.
    mapping (address => bool) received;
    string comment;
    // will be announce to the blockchain
    event deliveryBroadcast(address _snapCustomer, string _comment);

    // constructor
    function SnapDeliveryContract() public {

    }

    // Read-only function that returns the current opinion
    function getCurrentComment() public view returns(string) {
        return comment;
    }

    //Our function that modifies the state on the blockchain
    function broadcastDelivery(string _comment) public view returns (bool success) {
        // Looking up the address of the sender will return false if the sender isn't approved   
        opinion = _opinion;
        emit deliveryBroadcast(msg.sender, _comment);
        return true;
    }


}