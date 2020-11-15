import React from 'react';
import { GoogleLogin } from 'react-google-login';
import { Socket } from './Socket';

const clientId = '925708452618-1e0v9qhoat5ferhbs8s9jdvkghpalrre.apps.googleusercontent.com';
var isLoggedIn = true;

export function Login() {
    
    const onSuccess = (res) => {
        console.log('[Login Success] currentUser:', res.profileObj);
        alert('Login Succesfull')
        Socket.emit('login', {'isLoggedIn': isLoggedIn})
    };
    
    const onFailure = (res) => {
        console.log('[Login Failed] res:', res);
    };
    
    return (
        <div className="login">
            <GoogleLogin
                clientId={clientId}
                buttonText="Login"
                onSuccess={onSuccess}
                onFailure={onFailure}
                cookiePolicy={'single_host_origin'}
                isSignedIn={true} />
        </div>
            );
}

