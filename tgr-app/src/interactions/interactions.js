import { useMemo, useState } from 'react';
import { TextInput, FlatList, Text, View, SafeAreaView, 
         KeyboardAvoidingView, TouchableWithoutFeedback,
        TouchableOpacity, Dimensions } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { styles } from './interactions-style';
import Reaction from './reaction';
import Comment from './comment';

export default function Interactions({navigation, route}) {
  const { username } = route.params;
  const [commentsBool, setCommentsBool] = useState(true);
  const [commentsList, setCommentsList] = useState([]);
  const [reactionsList, setReactionsList] = useState([]);
  paddingSpace = Dimensions.get('window').width * 0.001;
  
  useMemo(() => {
    const fetchInteractions = fetch('https://raw.githubusercontent.com/AantLe12/DummyData/main/dummy_interactions.json').then(res => res.json()).then(data => {
      setCommentsList(data.comments);
      setReactionsList(data.reactions);
    }).catch(err => { console.log("ERROR")});
  }, []);

  if (commentsBool) {
    return (
      <View style={styles.container}>
          <TouchableWithoutFeedback onPress={() => 
            navigation.navigate('Feed')
            }>
              <AntDesign style={styles.backArrow} name="arrowleft" size={35} color="white" />
          </TouchableWithoutFeedback>    
    
          <Text style={styles.username}>{username}</Text>
          <View style={styles.tabs}>
            <TouchableWithoutFeedback  onPress={() => setCommentsBool(1) }>
              <View style={styles.underlineContainer}>
                <Text style={styles.tabsText}>Comments</Text>
              </View>
            </TouchableWithoutFeedback>
            <TouchableWithoutFeedback  onPress={() => setCommentsBool(0) }>
                <Text style={styles.tabsText} onClick>Reactions</Text>
            </TouchableWithoutFeedback>
          </View>

        <KeyboardAvoidingView behavior='height' keyboardVerticalOffset={5}>
          <FlatList
            style={styles.commentsList}
            data={commentsList}
            renderItem={({ item }) => <Comment item={item}
                                              navigation={navigation}/>}
            ItemSeparatorComponent={() => <View style={styles.commentSpace} />}
          />
          <View style={{backgroundColor: 'black'}}>
            <TouchableOpacity style={styles.sendBtn}>
            <Text style={styles.sendText}>Send</Text>
            </TouchableOpacity>
            <View>
              <TextInput style={styles.input}/>
            </View>
          </View>
        </KeyboardAvoidingView>
      </View>
    );
  } else {
    return (
      <SafeAreaView style={styles.container}>
        <TouchableWithoutFeedback onPress={() => 
          navigation.navigate('Feed')
          }>
            <AntDesign style={styles.backArrow} name="arrowleft" size={35} color="white" />
        </TouchableWithoutFeedback>    
  
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
