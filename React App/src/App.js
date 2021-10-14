import './App.css';
import Header from './Components/Header';
import Login from './Components/Login';
import {Fragment, useEffect, useState} from 'react';
import {auth} from './service/firebase';
import Items from './Components/Items/Items';

function App() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        auth.onAuthStateChanged(user => {
            setUser(user);
        })

        return () => {
            auth.signOut();
        };
    }, [])

    return (
        <Fragment>
            <Header user={user}/>
            {user ? <Items/> : <Login/>}
        </Fragment>
    );
}

export default App;
