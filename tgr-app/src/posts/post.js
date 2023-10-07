import { memo, useMemo, useState } from 'react';
import { FlatList, Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles} from './post-style.js';
import InteractionsList from "../interactions/interactions-list";
function Post({ navigation, item, curr_user_id }) {
  const [frontURI, setFrontURI] = useState(item.front_image);
  const [backURI, setBackURI] = useState(item.back_image);
  const [reactions, setReactions] = useState([{}]);

  function swap(front, back) {
    setFrontURI(front)
    setBackURI(back)
  }

// Gets the reactions
  function getReactions() {
    fetch('http://' + ip + ':5000/api/get-reactions?post_id=' + item._id)
    .then(response => response.text())
    .then(text => {
        if (JSON.parse(text) != {}) {
            let parsedArr = JSON.parse(text)
            if (JSON.parse(text).length > 0) {
                parsedArr = []
                for (let i=0; i < JSON.parse(text).length; i++) {
                    let entry = JSON.parse(parsedArr[i]);
                    // console.log(typeof(entry))
                    parsedArr.push(entry);
                    // console.log(typeof(JSON.parse(parsedArr[i])))
                }
            }
            setReactions(parsedArr);
        }
    })
    .catch((err) => {
      console.log("Could not retrieve reactions");
    });
  }

  useMemo(() => {
    getReactions();
  }, []);

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
            () => navigation.navigate('CreateReaction', {reactor_id: curr_user_id, post_id: item._id})}>
            <Image
            source={require('../../assets/emoji-round-plus.png')}
            style={styles.reactionButtonIcon}
            />
        </TouchableWithoutFeedback>
        </View>
        
        {/* Space in between the big photo and interactions */}
        <View style={styles.interactionsContainer}>
        {/* Reactions preview */}
        <FlatList
            horizontal={true}
            // scrollEnabled={false}
            data={reactions}
            ItemSeparatorComponent={() => <View style={styles.reactionSpace} />}
            renderItem={({ filler, index }) => <InteractionsList item={item} index={index}/>}
        />
        {/* Interactions section of post */}
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Interactions', { username: item.author_id, post_id: item._id})
        }>
            <Text style={styles.interactionsText}>View interactions ({reactions.length})</Text>
        </TouchableWithoutFeedback>
        </View>
    </View>)
}

export default memo(Post);