import { useMemo, useState } from 'react';
import { FlatList, Text, View, SafeAreaView, TouchableWithoutFeedback } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { styles } from './interactions-style';
import Reaction from './reaction';

export default function Interactions({navigation, route}) {
  const { username } = route.params;
  // const [interactions, setInteractions] = useState([]);
  const [commentsBool, setCommentsBool] = useState(true);
  const [commentsList, setCommentsList] = useState([]);
  const [reactionsList, setReactionsList] = useState([]);

  useMemo(() => {
    const fetchInteractions = fetch('https://raw.githubusercontent.com/AantLe12/DummyData/main/dummy_interactions.json').then(res => res.json()).then(data => {
      // setInteractions(data);
      setCommentsList(data.comments);
      setReactionsList(data.reactions);
    }).catch(err => { console.log("ERROR")});
  }, []);

  if (commentsBool) {
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
            <View style={styles.underlineContainer}>
              <Text style={styles.commentsText}>Comments</Text>
            </View>
          </TouchableWithoutFeedback>
          <TouchableWithoutFeedback  onPress={() => setCommentsBool(0) }>
              <Text style={styles.reactionsText} onClick>Reactions</Text>
          </TouchableWithoutFeedback>
        </View>
      </SafeAreaView>
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
              <Text style={styles.commentsText}>Comments</Text>
          </TouchableWithoutFeedback>
          <TouchableWithoutFeedback  onPress={() => setCommentsBool(0) }>
            <View style={styles.underlineContainer}>
              <Text style={styles.reactionsText} onClick>Reactions</Text>
            </View>
          </TouchableWithoutFeedback>
        </View>
        <FlatList
          style={styles.reactionsList}
          data={reactionsList}
          renderItem={({ item }) => <Reaction item={item}
                                                 navigation={navigation}/>}
          ItemSeparatorComponent={() => <View style={styles.itemSpace} />}
        />
      </SafeAreaView>
    );
  }
}
