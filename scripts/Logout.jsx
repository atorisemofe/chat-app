import React from 'react';
import { GoogleLogout } from 'react-google-login';

const clientId = '925708452618-1e0v9qhoat5ferhbs8s9jdvkghpalrre.apps.googleusercontent.com';

export function Logout () {
    const onSuccess = () => {
        alert('Logout Succesfull')
    };
    
    return (
        <div className="logout">
            <GoogleLogout
                clientId={clientId}
                buttonText="Logout"
                onLogoutSuccess={onSuccess} />
        </div>
        );
}

