import { Text, Image, SafeAreaView, TouchableWithoutFeedback } from 'react-native';
import { styles } from './header-style';

export default function Header({navigation, route, pfp}) {
  return (
    <SafeAreaView style={styles.header}>
        <Text style={styles.headerText}>_tgr.</Text>
        {/* Profile picture leading back to profile when clicked on */}
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Profile')}>
            <Image
                style={styles.userProfilePic}
                source={{uri: pfp}}
            />
        </TouchableWithoutFeedback>
    </SafeAreaView>
  );
}