import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import CameraScreen from "./src/camera/CameraScreen";
import PreviewScreen from "./src/camera/PreviewScreen";
import Feed from "./posts/feed";
import Profile from "./posts/profile";
import PostScreen from "./src/camera/PostScreen";
import { GestureHandlerRootView } from "react-native-gesture-handler";


const Stack = createNativeStackNavigator();
function App() {
  return (
    <NavigationContainer>
      <GestureHandlerRootView style={{flex: 1}}>
      <Stack.Navigator initialRouteName="Feed">
        <Stack.Screen name="Camera" component={CameraScreen} options={{
          unmountOnBlur: true,
          headerStyle: {
            backgroundColor: 'black',
            
          }, 
          title: '',
          headerTintColor: 'white'
          }}/>
        <Stack.Screen name="Preview" component={PreviewScreen} options={{
          headerStyle: {
              backgroundColor: 'black'
            },
            title: '',
            headerTintColor: 'white'
        }}/>
        <Stack.Screen name="Feed" component={Feed}
                      options={{
                        // title: 'Feed',
                        headerShown: false,
                        // headerStyle: {
                        //   backgroundColor: 'white',
                        // },
                        // headerTintColor: '#fff',
                      }}/>
        <Stack.Screen name="Profile" component={Profile}/>
        <Stack.Screen name="PostPhoto" component={PostScreen}/>
      </Stack.Navigator></GestureHandlerRootView>
    </NavigationContainer>
  );
}

export default App;
