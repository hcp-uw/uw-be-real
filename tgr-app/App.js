import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import CameraScreen from "./src/camera/CameraScreen"
import PreviewScreen from "./src/camera/PreviewScreen"
import Feed from "./posts/feed"


const Stack = createNativeStackNavigator();
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Camera">
        <Stack.Screen name="Camera" component={CameraScreen} options={{
          unmountOnBlur: true,
          headerStyle: {
            backgroundColor: 'black',
            
          }, 
          title: '',
          headerTintColor: 'white'
        }}/>
        <Stack.Screen name="Preview" component={PreviewScreen} options={
          {
            headerStyle: {
              backgroundColor: 'black'
            },
            title: '',
            headerTintColor: 'white'
          }
        }/>
        <Stack.Screen name="Feed" component={Feed}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
