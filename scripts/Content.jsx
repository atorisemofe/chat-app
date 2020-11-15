    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';
import { Login } from './Login';
import { Logout } from './Logout';
import Linkify from 'react-linkify';

export function Content() {
    const [messages, setMessages] = React.useState([]);
 
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('messages received', (data) => {
                console.log("Received addresses from server: " + data['allMessages']);
                setMessages(data['allMessages']);
            })
        })
    }
    

    getNewMessages();
    
    
    
    return (
        <Linkify>
            <div>
                
                <h1>Aketi Chatroom</h1>
                <Login />
                <dl className="container">
                    {
                        messages.map((message, index) =>
                        <dt key={index}>{message}</dt>)
                    }
                </dl>
                
                <div className="b1">
                    <Button />
                </div>
                <Logout />
            </div>
        </Linkify>
    );
}
