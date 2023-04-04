import {
    View,
    Text,
    Image,
    FlatList,
} from 'react-native';
import styles from './profile-recap-style'

export default function Recap({data}) {
    const renderList = ({ item }) => {
        return(
            <View style={styles.listItem}>
                <Image
                style={styles.listItem}
                source={{uri:item.content.front_image}}        
                />
            </View>
        )
    }

    return (
        <View style={styles.recap}>
            <FlatList horizontal data={data} renderItem={renderList}/>
        </View>
    )
}