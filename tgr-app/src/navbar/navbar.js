import { View, TouchableWithoutFeedback } from 'react-native';
import { Foundation, MaterialIcons, Ionicons } from '@expo/vector-icons';
import { styles } from './navbar-style';

export default function Navbar({navigation, route, pfp}) {
  return (
    <View style={styles.navbar}>
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Feed')
        }>
          <Foundation name="home" size={35} color="white" />
        </TouchableWithoutFeedback>
        
        <TouchableWithoutFeedback  onPress={() => 
        navigation.navigate('Profile')
        }>
          <MaterialIcons name="public" size={35} color="white" />
        </TouchableWithoutFeedback>
        
        <TouchableWithoutFeedback  onPress={() => 
        navigation.navigate('Social', { pfp: pfp})
        }>
          <Ionicons name="people" size={35} color="white" />
        </TouchableWithoutFeedback>
  </View>
  );
}