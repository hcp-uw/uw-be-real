import { memo } from 'react';
import { Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles } from './comment-style';

function Comment({ navigation, item }) {
  return (
    <View style={styles.commentContainer}>
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Profile')
        }>
            <Image
                    style={styles.postProfPic} 
                    source={{uri: item.icon}}
            />
        </TouchableWithoutFeedback>

        {/* Username and time sent same line
          * Comment right under the user & time
        */}
        <View style={styles.nonProfContainer}>
            <View style={styles.userTimeContainer}>
                <Text style={styles.username}>{item.username}</Text>
                <Text style={styles.commentTime}>{ parseInt((parseInt(Date.now() / 1000) - item.comment_time) / 3600) } hrs ago</Text>
            </View>
            <Text style={styles.comment}>{item.comment}</Text>
            <Text style ={styles.reply}>Reply</Text>
        </View>
    </View>)
}

export default memo(Comment);