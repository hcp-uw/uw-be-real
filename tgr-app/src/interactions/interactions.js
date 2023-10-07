import { useMemo, useState } from 'react';
import { TextInput, FlatList, Text, View, SafeAreaView, 
         KeyboardAvoidingView, TouchableWithoutFeedback,
        TouchableOpacity, Dimensions } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { styles } from './interactions-style';
import Reaction from './reaction';
import Comment from './comment';

export default function Interactions({navigation, route}) {
  const { username, post_id } = route.params;
  const [comment, onChangeComment] = useState('Add a comment!');
  const [commentsBool, setCommentsBool] = useState(true);
  const [commentsList, setCommentsList] = useState([]);
  const [reactionsList, setReactionsList] = useState([]);
  
  const paddingSpace = Dimensions.get('window').width * 0.001;
  
  function createComment() {
    fetch('http://' + ip + ':5000/api/comment-create', 
          {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
              "comment": comment,
              "post_id": post_id,
              "commenter_id": username 
            }),
          })
    .then((res) => res.json()).then((data) => {
      console.log(data);
    })
    .catch(err => {console.log("Could not create comment")});
  }

  useMemo(() => {

  }, []);

  // Switches between the comments and reactions tab 
  if (commentsBool) {
    return (
      <View style={styles.container}>
          {/* Back arrow leads back to the feed */}
          <TouchableWithoutFeedback onPress={() => 
            navigation.navigate('Feed')
            }>
              <AntDesign style={styles.backArrow} name="arrowleft" size={35} color="white" />
          </TouchableWithoutFeedback>    
          {/* Username on top of tabs */}
          <Text style={styles.username}>{username}</Text>
          <View style={styles.tabs}>
            {/* Comments tab */}
            <TouchableWithoutFeedback  onPress={() => setCommentsBool(1) }>
              <View style={styles.underlineContainer}>
                <Text style={styles.tabsText}>Comments</Text>
              </View>
            </TouchableWithoutFeedback>
            {/* Reactions tab */}
            <TouchableWithoutFeedback  onPress={() => setCommentsBool(0) }>
                <Text style={styles.tabsText} onClick>Reactions</Text>
            </TouchableWithoutFeedback>
          </View>
        
        <KeyboardAvoidingView behavior='height' keyboardVerticalOffset={5}>
          {/* List of comments */}
          <FlatList
            style={styles.commentsList}
            data={commentsList}
            renderItem={({ item }) => <Comment item={item}
                                              navigation={navigation}/>}
            ItemSeparatorComponent={() => <View style={styles.commentSpace} />}
          />

          {/* Keyboard with send button */}
          <View>
            <TouchableOpacity style={styles.sendBtn} onPress={() => createComment()}>
              <Text style={styles.sendText}>Send</Text>
            </TouchableOpacity>
            {/* Text field to type comment */}
            <View>
              <TextInput style={styles.input} onChangeText={onChangeComment} value={comment}/>
            </View>
          </View>
        </KeyboardAvoidingView>
      </View>
    );
  } else {
    return (
      <SafeAreaView style={styles.container}>
        {/* Back arrow leads back to the feed */}
        <TouchableWithoutFeedback onPress={() => 
          navigation.navigate('Feed')
          }>
            <AntDesign style={styles.backArrow} name="arrowleft" size={35} color="white" />
        </TouchableWithoutFeedback>    
  
        {/* Username on top of tabs */}
        <Text style={styles.username}>{username}</Text>
        <View style={styles.tabs}>
          <TouchableWithoutFeedback  onPress={() => setCommentsBool(1) }>
              <Text style={styles.tabsText}>Comments</Text>
          </TouchableWithoutFeedback>
          <TouchableWithoutFeedback  onPress={() => setCommentsBool(0) }>
            <View style={styles.underlineContainer}>
              <Text style={styles.tabsText} onClick>Reactions</Text>
            </View>
          </TouchableWithoutFeedback>
        </View>
        <FlatList
          style={styles.reactionsList}
          data={reactionsList}
          renderItem={({ item }) => <Reaction item={item}
                                                 navigation={navigation}/>}
          ItemSeparatorComponent={() => <View style={styles.reactionSpace} />}
        />
        
      </SafeAreaView>
    );
  }
}
