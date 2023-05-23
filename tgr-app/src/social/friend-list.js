import { memo } from 'react';
import { Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles } from './friend-list-style';


function FriendList({ navigation, item }) {
  return (
    <View style={styles.friendItem}>
        <View style={styles.profile}>
            <TouchableWithoutFeedback  onPress={() => 
                navigation.navigate('Profile')
            }>
                    <Image
                            style={styles.postProfPic} 
                            source={{uri: item.icon}}
                    />
            </TouchableWithoutFeedback>
            <View style={styles.names}>
                <Text style={styles.name}>{item.name}</Text>
                <Text style={styles.username}>{item.username}</Text>
            </View>
        </View>
        <Text style={styles.editText}>. . .</Text>
    </View>)
}

export default memo(FriendList);