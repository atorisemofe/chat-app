import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';
 

export function GoogleButton() {
    function handleSubmit(response) {
     console.log(response);
    // TODO replace with name from oauth
    let name = response.profileObj.name;
    Socket.emit('new google user', {
      'name': name,
   });
    
   console.log('Sent the name ' + name + ' to server!');
}
    return (
          <GoogleLogin
            clientId="925708452618-1e0v9qhoat5ferhbs8s9jdvkghpalrre.apps.googleusercontent.com"
            buttonText="Login"
            onSuccess={handleSubmit}
            onFailure={handleSubmit}
            cookiePolicy={'single_host_origin'}
          />
          
    );
}
