import { memo } from 'react';
import { Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles } from './reaction-style';

function Reaction({ navigation, item }) {
  return (
    <View style={styles.postContainer}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
                <TouchableWithoutFeedback  onPress={() => 
                    navigation.navigate('Profile')
                }>
                    <Image
                            style={styles.postProfPic} 
                            source={{uri: item.icon}}
                            />
                </TouchableWithoutFeedback>
                <Text style={styles.username}>{item.username}</Text>
        </View>
        <Text style={styles.reactionTime}>{ parseInt((parseInt(Date.now() / 1000) - item.reaction_time) / 3600) } hrs ago</Text>
    </View>)
}

export default memo(Reaction);