import { Text, Image, SafeAreaView, TouchableWithoutFeedback } from 'react-native';
import { styles } from './header-style';

export default function Header({navigation, route, pfp}) {
  return (
    <SafeAreaView style={styles.header}>
        <Text style={styles.headerText}>_.tgr</Text>
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