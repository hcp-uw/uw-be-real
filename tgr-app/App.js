import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import CameraScreen from "./src/camera/CameraScreen"
import PreviewScreen from "./src/camera/PreviewScreen"
import Feed from "./posts/feed"
import Profile from "./profile/profile"

const Stack = createNativeStackNavigator();
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Profile">
        <Stack.Screen name="Camera" component={CameraScreen} options={{unmountOnBlur: true}}/>
        <Stack.Screen name="Preview" component={PreviewScreen}/>
        <Stack.Screen name="Feed" component={Feed}
                      options={{
                        // title: 'Feed',
                        headerShown: false,
                        // headerStyle: {
                        //   backgroundColor: 'white',
                        // },
                        // headerTintColor: '#fff',
                      }}/>
        <Stack.Screen name="Profile" component={Profile}
        options={{
          headerShown: false,
          }}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
