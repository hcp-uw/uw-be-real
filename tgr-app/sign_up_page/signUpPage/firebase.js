import { initializeApp } from 'firebase/app';
// import {} from '/firebase/<service>';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';
import { firebase } from '@react-native-firebase/auth';

const firebaseApp = initializeApp ({
    apiKey: "AIzaSyAha9-I5lK0edhOxzKI27pm04T_YUBITM8",
    authDomain: "uw-be-real.firebaseapp.com",
    projectId: "uw-be-real",
    storageBucket: "uw-be-real.appspot.com",
    messagingSenderId: "105892944278",
    appId: "1:105892944278:web:966f7cca52fb5f66f0e5b7",
    measurementId: "G-SYS9TDH3Q7"
});

const auth = getAuth(firebaseApp);
const db = getFirebase(firebaseApp);

//detect auth state
// onAuthStateChanged(auth, user => {
//     if(user != null) {
//         console.log('logged in!');
//     }
//     else {
//         console.log('No user');
//     }
// });

if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

export {firebase};