import { memo } from 'react';
import { Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles } from './friend-list-style';


function FriendList({ navigation, item }) {
  return (
    <View style={styles.item}>
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

export default memo(FriendList);