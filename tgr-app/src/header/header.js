import { View, Text, Image, SafeAreaView, TouchableWithoutFeedback } from 'react-native';
import { styles } from './header-style';
import { Entypo } from '@expo/vector-icons';

export default function Header({navigation, route, pfp}) {
  return (
    <SafeAreaView style={styles.headerContainer}>
        <Text style={styles.headerText}>_tgr.</Text>
        <View style={styles.profile}>
            {/* Profile picture leading back to profile when clicked on */}
            <TouchableWithoutFeedback  onPress={() => 
              navigation.navigate('Camera')}>
              <Entypo name="camera" size={35} color="white"/>
            </TouchableWithoutFeedback>
            {/* Space between camera and profile pic */}
            <View style={{margin: 5}}></View>
            <TouchableWithoutFeedback  onPress={() => 
                navigation.navigate('Profile')}>
                <Image
                    style={styles.userProfilePic}
                    source={{uri: pfp}}
                />
            </TouchableWithoutFeedback>
          </View>
    </SafeAreaView>
  );
}