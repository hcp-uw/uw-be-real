import { useMemo, useState } from 'react';
import { FlatList, Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { Foundation, MaterialIcons, Ionicons } from '@expo/vector-icons';
import { styles, width } from './feed-style.js';

export default function Feed({navigation, route}) {
  const [posts, setPosts] = useState([]);
  const [firstPost, setFirst] = useState();
  useMemo(() => {
    const fetchData = fetch('https://drive.google.com/uc?export=view&id=1ywYz5du-nQn19uwKjhkO-KD0s7ii9Yzz').then(res => res.json()).then(data => {
      setPosts(data);
      setFirst(data[0].author_icon);
    });
  }, []);

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerText}>_.tgr</Text>
        <TouchableWithoutFeedback  onPress={() => 
          navigation.navigate('Profile')
        }>
            <Image
              style={styles.userProfilePic}
              source={{uri: firstPost}}
            />
        </TouchableWithoutFeedback >
      </View>

      {/* Feeds */}
      <FlatList
        style={styles.feed}
        data={posts}
        renderItem={({ item }) =>
                                    <View>
                                      {/* Profile portion of post */}
                                      <View style={styles.profileInfo}>

                                        <TouchableWithoutFeedback  onPress={() => 
                                          navigation.navigate('Profile')
                                        }>
                                          <Image
                                                  style={styles.postProfPic} 
                                                  source={{uri: item.author_icon}}
                                          />
                                        </TouchableWithoutFeedback>

                                        {/* Username and info on post */}
                                        <View style={{margin: 5}}>
                                          <View style={styles.userContainer}>
                                            <Text style={{color: 'white',}}>
                                              {item.author_username}
                                            </Text>

                                            <Text style={styles.streakText}>{item.author_streak}</Text>

                                            <Text style={styles.streakEmoji}>{item.author_streak_emoji}</Text>
                                          </View>
                                          <Text style={{color: '#adadad',}}>
                                            { parseInt((parseInt(Date.now() / 1000) - item.post_time) / 3600)} hr Late
                                          </Text>
                                        </View>
                                      </View>
                                      
                                      {/* Space in between who posted and the post itself */}
                                      <View style={{padding: 5}}></View>

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
                                      <View style={{padding: 10}}></View>

                                      <TouchableWithoutFeedback  onPress={() => 
                                        navigation.navigate('Interactions')
                                      }>
                                        <View style={{left: 15}}>
                                          <FlatList
                                            horizontal={true}
                                            scrollEnabled={false}
                                            data={item.post_interactions}
                                            ItemSeparatorComponent={() => <View style={{width: 20}} />}
                                            renderItem={({ filler, index }) =>
                                                                    <View>
                                                                            <Image
                                                                              style={{width: '560%',
                                                                                      height: width * 0.075,
                                                                                      borderRadius: 30,
                                                                                      borderWidth: 2.8,
                                                                                      borderColor: 'white',
                                                                                      // opacity: (1 -0.1 * index),
                                                                              }} 
                                                                              source={{uri: item.post_interactions[index]}}
                                                                            />
                                                                    </View>
                                            }
                                            />
                                          <Text style={styles.interactionsText}>View interactions ({item.post_comments})</Text>
                                        </View>
                                      </TouchableWithoutFeedback>


                                    </View>}
        ItemSeparatorComponent={() => <View style={{height: 100}} />}
      />

      {/* Navbar */}
      <View style={styles.navbar}>
        <TouchableWithoutFeedback  onPress={() => 
            navigation.navigate('Feed')
        }>
          <Foundation style={styles.navbar_home} name="home" size={35} color="white" />
        </TouchableWithoutFeedback>
        
        <TouchableWithoutFeedback  onPress={() => 
          navigation.navigate('Profile')
        }>
          <MaterialIcons style={styles.navbar_public} name="public" size={35} color="white" />
        </TouchableWithoutFeedback>
        
        <TouchableWithoutFeedback  onPress={() => 
          navigation.navigate('Friends')
        }>
          <Ionicons style={styles.navbar_friends} name="people" size={35} color="white" />
        </TouchableWithoutFeedback>
      </View>
    </View>
  );
}
