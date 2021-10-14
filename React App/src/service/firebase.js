import firebase from 'firebase/compat';
import 'firebase/auth';

const firebaseConfig = {
    apiKey: "AIzaSyCRlWKtAI1WAlRTwnzngEVuet7asH_aYe8",
    authDomain: "react-app-4ee0b.firebaseapp.com",
    projectId: "react-app-4ee0b",
    storageBucket: "react-app-4ee0b.appspot.com",
    messagingSenderId: "407072633743",
    appId: "1:407072633743:web:05d88be4cb8bc876bed1fa"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
export const auth = firebase.auth();

const provider = new firebase.auth.GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account' });

export const signInWithGoogle = () => auth.signInWithPopup(provider);
export const signOut = () => auth.signOut();
export default firebase;