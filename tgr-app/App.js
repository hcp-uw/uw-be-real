import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { GestureHandlerRootView } from "react-native-gesture-handler";

import CameraScreen from "./src/camera/CameraScreen"
import PreviewScreen from "./src/camera/PreviewScreen"
import Feed from "./src/posts/feed"
import Profile from "./profile/profile"
import Edit from "./profile/profile-edit/profile-edit"
import Interactions from "./src/interactions/interactions"
import Social from "./src/social/social"
import ExpandedFriends from "./src/social/expanded-friends";
import ExpandedRequests from "./src/social/expanded-requests";

const Stack = createNativeStackNavigator();
function App() {
  return (
    <NavigationContainer>
      <GestureHandlerRootView style={{flex: 1}}>
      <Stack.Navigator initialRouteName="Camera">
        <Stack.Screen name="Camera" component={CameraScreen} options={{unmountOnBlur: true,
           headerStyle: {backgroundColor: 'black'},
           title: '',
           headerTintColor: 'white'
           }}/>
        <Stack.Screen name="Preview" component={PreviewScreen} options={{unmountOnBlur: true,
           headerStyle: {backgroundColor: 'black'},
           title: '',
           headerTintColor: 'white'
        }}
        />
        <Stack.Screen name="Feed" component={Feed}
                      options={{
                        headerShown: false,
                      }}/>
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
      </GestureHandlerRootView>
    </NavigationContainer>
  );
}

export default App;
