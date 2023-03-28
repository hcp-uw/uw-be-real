import { View, Text, TouchableWithoutFeedback } from 'react-native';
import { Ionicons, Entypo } from '@expo/vector-icons'; 
import { styles } from './profile-header-style';

export default function Header({navigation}) {
    return (
        <View style={styles.header}>
            <TouchableWithoutFeedback onPress={() => navigation.navigate('Feed')}>
                <Ionicons name="arrow-back" size={24} color="white" />
            </TouchableWithoutFeedback>

            <Text style={styles.text}>Profile</Text>

            <TouchableWithoutFeedback>
                <Entypo name="dots-three-horizontal" size={24} color="white" />
            </TouchableWithoutFeedback>
        </View>
    );
}