import { memo } from 'react';
import { Text, Image, View, TouchableWithoutFeedback, TouchableOpacity } from 'react-native';
import { styles } from './request-list-style';


function RequestList({ navigation, item }) {
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
        
        <TouchableOpacity
          style={styles.submitBtn}
        >
            <Text style={styles.submitText}>Accept</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.rejectBtn}
        >
            <Text style={styles.rejectText}>Reject</Text>
        </TouchableOpacity>
    </View>)
}

export default memo(RequestList);