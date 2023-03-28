import { View, TouchableWithoutFeedback } from 'react-native';
import { Foundation, MaterialIcons, Ionicons } from '@expo/vector-icons';
import { styles } from './navbar-style';

export default function Navbar({navigation, route, pfp}) {
  return (
    <View style={styles.navbar}>
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Feed')
        }>
          <Foundation style={styles.navbar_home} name="home" size={35} color="white" />
        </TouchableWithoutFeedback>
        
        <TouchableWithoutFeedback  onPress={() => 
        navigation.navigate('Profile')
        }>
          <MaterialIcons style={styles.navbar_public} name="public" size={35} color="white" />
        </TouchableWithoutFeedback>
        
        <TouchableWithoutFeedback  onPress={() => 
        navigation.navigate('Friends', { pfp: pfp})
        }>
          <Ionicons style={styles.navbar_friends} name="people" size={35} color="white" />
        </TouchableWithoutFeedback>
  </View>
  );
}