import { View, Text, TouchableWithoutFeedback } from 'react-native';
import { Ionicons, Entypo } from '@expo/vector-icons'; 
import { styles } from './profile-header-style';

export default function Header({navigation, leftnav, mid, rightnav}) {
    return (
        <View style={styles.header}>
            <TouchableWithoutFeedback onPress={() => navigation.navigate(leftnav)}>
                <Ionicons name="arrow-back" size={24} color="white" />
            </TouchableWithoutFeedback>

            <Text style={styles.text}>{mid}</Text>

            <TouchableWithoutFeedback onPress={() => navigation.navigate(rightnav)}>
                <Entypo name="dots-three-horizontal" size={24} color="white" />
            </TouchableWithoutFeedback>
        </View>
    );
}