import { useMemo, useState } from 'react';
import { Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles } from './header-style';

export default function Header({navigation, route, pfp}) {
  return (
    <View style={styles.header}>
        <Text style={styles.headerText}>_.tgr</Text>
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Profile')}>
            <Image
                style={styles.userProfilePic}
                source={{uri: pfp}}
            />
        </TouchableWithoutFeedback>
    </View>
  );
}