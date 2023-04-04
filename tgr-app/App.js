import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import CameraScreen from "./src/camera/CameraScreen"
import PreviewScreen from "./src/camera/PreviewScreen"
import Feed from "./src/posts/feed"
import Profile from "./src/posts/profile"
import Interactions from "./src/interactions/interactions"
import Social from "./src/social/social"

const Stack = createNativeStackNavigator();
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Feed">
        <Stack.Screen name="Camera" component={CameraScreen} options={{unmountOnBlur: true}}/>
        <Stack.Screen name="Preview" component={PreviewScreen}/>
        <Stack.Screen name="Feed" component={Feed}
                      options={{
                        headerShown: false,
                      }}/>
        <Stack.Screen name="Profile" component={Profile}/>
        <Stack.Screen name="Interactions" component={Interactions}
                      options={{
                        headerShown: false,
                      }}/>
        <Stack.Screen name="Social" component={Social}
                      options={{
                        headerShown: false,
                      }}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
