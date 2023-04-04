import { memo } from 'react';
import { Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles } from './social-list-style';


function SocialList({ navigation, item }) {
  return (
    <View>
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Profile')
            }>
                <Image
                        style={styles.postProfPic} 
                        source={{uri: item.icon}}
                />
        </TouchableWithoutFeedback>
        <Text style={styles.name}>{item.name}</Text>
        <Text style={styles.username}>{item.username}</Text>
        <Text style={styles.editText}>. . .</Text>
    </View>)
}

export default memo(SocialList);