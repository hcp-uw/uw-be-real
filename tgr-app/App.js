import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import CameraScreen from "./src/camera/CameraScreen"
import PreviewScreen from "./src/camera/PreviewScreen"
import Feed from "./posts/feed"


const Stack = createNativeStackNavigator();
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Feed">
        <Stack.Screen name="Camera" component={CameraScreen} options={{unmountOnBlur: true}}/>
        <Stack.Screen name="Preview" component={PreviewScreen}/>
        <Stack.Screen name="Feed" component={Feed}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
