import React, { useState, useEffect } from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import HomeScreen from "./signUpPage/HomeScreen";
import EnterName from "./signUpPage/EnterName";
import EnterUsername from "./signUpPage/EnterUsername";
import EnterPhoneNumber from "./signUpPage/EnterPhoneNumber";
import EnterEmail from "./signUpPage/EnterEmail";
import Login from "./signUpPage/Login";
import tempDashboard from "./signUpPage/tempDashboard";
import { firebase } from "./config";
import ResendVerification from "./signUpPage/ResendVerification";
import WaitVerification from "./signUpPage/WaitVerification";

const Stack = createStackNavigator();

// web: 873886857509-5lo9vtdg31c3aru5008nmng2rntn62k3.apps.googleusercontent.com
// ios: 873886857509-gnpmq1hs3jsgrabemsinhmgarf5b110b.apps.googleusercontent.com
// android: 873886857509-7226c6m3un9pvrinnds9517msvknpnnj.apps.googleusercontent.com
function App() {
    const [initializing, setInitializing] = useState(true);
    const [user, setUser] = useState();
    // const [firstName, setFirstName] = useState("");
    // const [lastName, setLastName] = useState("");

    // Handle user state changes
    function onAuthStateChanged(user) {
        setUser(user);
        if (initializing) setInitializing(false);
    }

    useEffect(() => {
        const subscriber = firebase
            .auth()
            .onAuthStateChanged(onAuthStateChanged);
        return subscriber;
    }, []);

    if (initializing) return null;

    if (!user || (user && !firebase.auth().currentUser.emailVerified)) {
        return (
            <Stack.Navigator initialRouteName="Home">
                <Stack.Screen
                    name="Home"
                    component={HomeScreen}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="Login"
                    component={Login}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="ResendVerification"
                    component={ResendVerification}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="Name"
                    component={EnterName}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="Username"
                    component={EnterUsername}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="PhoneNumber"
                    component={EnterPhoneNumber}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="Email"
                    component={EnterEmail}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="WaitVerification"
                    component={WaitVerification}
                    options={{ headerShown: false }}
                />
            </Stack.Navigator>
        );
    }

    return (
        <Stack.Navigator>
            <Stack.Screen
                name="tempDashboard"
                component={tempDashboard}
                options={{ headerShown: false }}
            />
        </Stack.Navigator>
    );
}

export default () => {
    return (
        <NavigationContainer>
            <App />
        </NavigationContainer>
    );
};
