// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBN5fKyJsK8b5p9uniln_wODETVRQ4J2oI",
  authDomain: "love-256d2.firebaseapp.com",
  projectId: "love-256d2",
  storageBucket: "love-256d2.firebasestorage.app",
  messagingSenderId: "482910194629",
  appId: "1:482910194629:web:c7c4139f3dd357438259ac",
  measurementId: "G-2MXNQYNRYF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);