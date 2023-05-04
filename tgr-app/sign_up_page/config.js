// firebase config key setup

import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

// Web app's firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAha9-I5lK0edhOxzKI27pm04T_YUBITM8",
  authDomain: "uw-be-real.firebaseapp.com",
  projectId: "uw-be-real",
  storageBucket: "uw-be-real.appspot.com",
  messagingSenderId: "105892944278",
  appId: "1:105892944278:web:966f7cca52fb5f66f0e5b7",
  measurementId: "G-SYS9TDH3Q7"
}

if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig)
}

export {firebase};