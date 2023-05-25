import { memo } from 'react';
import { Image, View } from 'react-native';
import { styles } from '../social/friend-list-style';

function FriendItem({ item }) {
  return (
    <View>
        <Image
                style={styles.postProfPic} 
                source={{uri: item.icon}}
        />
    </View>)
}

export default memo(FriendItem);