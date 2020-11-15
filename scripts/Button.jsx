import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let userMessageValue = document.getElementById("message_input").value;
    let userNameValue = document.getElementById("name_input").value;
    let colon =': ';
    let newMessage = userNameValue + colon + userMessageValue;
    
    let newMessageField = document.getElementById("message_input");
    Socket.emit('new message input', {
        'message': newMessage
        
    });
     
    console.log('Sent the message ' + newMessage.value + ' to server!');
    newMessageField.value = ''
    
    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit}>
            <input id="name_input" placeholder="Enter your name"></input>
            <input id="message_input" placeholder="Enter a Message"></input>
            <button>Send</button>
        </form>
    );
}
