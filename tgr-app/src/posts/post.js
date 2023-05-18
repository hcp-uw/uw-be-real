import { memo } from 'react';
import { FlatList, Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles } from './post-style.js';
import InteractionsList from "../interactions/interactions-list";
function Post({ navigation, item }) {
  return (
    <View style={styles.postContainer}>
        {/* Profile info is the pfp, username, and time post */}
        <View style={styles.profileInfo}>

            <TouchableWithoutFeedback  onPress={() => 
                navigation.navigate('Profile')
            }>
                <Image
                        style={styles.postProfPic} 
                        source={{uri: item.author_icon}}
                />
            </TouchableWithoutFeedback>

            {/* Username and time posted on the same row */}
            <View style={styles.userContainer}>
                <Text style={{color: 'white',}}>{item.author_username}</Text>
                <Text style={{color: '#adadad',}}>
                    { parseInt((parseInt(Date.now() / 1000) - item.post_time) / 3600)} hr Late
                </Text>
            </View>
        </View>
        
        {/* User's big post photo */}
        <Image
            style={styles.bigPostImg} 
            source={{uri: item.post_front}}
        />
        {/* User's small post photo */}
        <Image
            style={styles.smallPostImg} 
            source={{uri: item.post_back}}
        />

        {/* Space in between the big photo and interactions */}
        <View style={styles.interactionsContainer}>
        <FlatList
            horizontal={true}
            // scrollEnabled={false}
            data={item.post_interactions}
            ItemSeparatorComponent={() => <View style={styles.reactionSpace} />}
            renderItem={({ filler, index }) => <InteractionsList item={item} index={index}/>}
        />
        {/* Interactions section of post */}
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Interactions', { username: item.author_username })
        }>
            <Text style={styles.interactionsText}>View interactions ({item.post_comments})</Text>
        </TouchableWithoutFeedback>
        </View>
    </View>)
}

export default memo(Post);