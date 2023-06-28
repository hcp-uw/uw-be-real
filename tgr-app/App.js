import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import React, {useState, useEffect} from 'react';
import CameraScreen from "./src/camera/CameraScreen"
import PreviewScreen from "./src/camera/PreviewScreen"
import Feed from "./src/posts/feed"
import Profile from "./profile/profile"
import Edit from "./profile/profile-edit/profile-edit"
import Interactions from "./src/interactions/interactions"
import Social from "./src/social/social"
import ExpandedFriends from "./src/social/expanded-friends";
import ExpandedRequests from "./src/social/expanded-requests";
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
import { StatusBar } from "expo-status-bar";
import CreateReaction from "./src/camera/CreateReactionScreen";


const Stack = createNativeStackNavigator();
// web: 873886857509-5lo9vtdg31c3aru5008nmng2rntn62k3.apps.googleusercontent.com
// ios: 873886857509-gnpmq1hs3jsgrabemsinhmgarf5b110b.apps.googleusercontent.com
// android: 873886857509-7226c6m3un9pvrinnds9517msvknpnnj.apps.googleusercontent.com
function App() {
  const [initializing, setInitializing] = useState(true);
  const [user, setUser] = useState();
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
  let isNewUser = !user || (user && !firebase.auth().currentUser.emailVerified);
  return (
    
    <NavigationContainer>
    {isNewUser ? (
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
    ) :
    (
      
      <Stack.Navigator initialRouteName="Feed">
        {/* At the moment, initialRouteName doesn't work
          not sure why it doesn't work, so keep Feed as the first screen 
          If you want to start on a different screen for testing purposes, you'll
          have to move your screen to be above Feed temporarily
        */}
          <Stack.Screen name="Feed" component={Feed}
                        options={{
                          headerShown: false,
                        }}/>
        <Stack.Screen name="Camera" component={CameraScreen} options={{unmountOnBlur: true, headerShown: false,}}/>
        <Stack.Screen name="CreateReaction" component={CreateReaction} options={{unmountOnBlur: true,headerShown: false }}/>

          <Stack.Screen name="Preview" component={PreviewScreen}/>
          <Stack.Screen name="Edit" component={Edit} 
            options={{
              headerShown: false,
              animation: "slide_from_right",
            }}/>
          <Stack.Screen name="Profile" component={Profile} 
            options={{
              headerShown: false,
            }}/>
          <Stack.Screen name="Interactions" component={Interactions}
                        options={{
                          headerShown: false,
                        }}/>
          <Stack.Screen name="Social" component={Social}
                        options={{
                          headerShown: false,
                        }}/>
          <Stack.Screen name="ExpandedFriends" component={ExpandedFriends}
                        options={{
                          headerShown: false,
                        }}/>
          <Stack.Screen name="ExpandedRequests" component={ExpandedRequests}
                        options={{
                          headerShown: false,
                        }}/>
          
      </Stack.Navigator>
                        
  )}
  </NavigationContainer>
  );
}

export default App;
