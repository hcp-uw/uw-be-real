import { memo, useState } from 'react';
import { FlatList, Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles} from './post-style.js';
import InteractionsList from "../interactions/interactions-list";
function Post({ navigation, item }) {
  const [frontURI, setFrontURI] = useState(item.front_image);
  const [backURI, setBackURI] = useState(item.back_image);
  
  function swap(front, back) {
    setFrontURI(front)
    setBackURI(back)
  }

// Gets the comments
//   function getPosts() {
//     fetch('http://' + ip + ':5000/api/get-posts?is_global=' + global)
//     .then(response => response.text())
//     .then(text => {
//       // Convert JSON string to JSON
//       if (text != null) {
//         setPosts(JSON.parse(text))
//       }
//     })
//     .catch((err) => {
//       console.log("Could not retrieve posts");
//     });
//   }

// Gets the reactions


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
                <Text style={{color: 'white',}}>{item.author_id}</Text>
                <Text style={{color: '#adadad',}}>
                    { parseInt((parseInt(Date.now() / 1000) - item.datetime) / 3600)} hr Late
                </Text>
            </View>
        </View>
        
        {/* User's big post photo */}
        <View>
        <TouchableWithoutFeedback  onPress={() => {swap(backURI, frontURI)}}>
            <Image
                style={styles.bigPostImg} 
                source={{uri: frontURI}}
            />
        </TouchableWithoutFeedback>
        {/* User's small post photo */}
        <TouchableWithoutFeedback  onPress={() => {swap(backURI, frontURI)}}>
            <Image
                style={styles.smallPostImg} 
                source={{uri: backURI}}
            />
        </TouchableWithoutFeedback>

        {/* Button to create a reaction */}
        <TouchableWithoutFeedback onPress={
            () => navigation.navigate('CreateReaction', {username: item.author_username, id: item._id})}>
            <Image
            source={require('../../assets/emoji-round-plus.png')}
            style={styles.reactionButtonIcon}
            />
        </TouchableWithoutFeedback>
        </View>
        
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