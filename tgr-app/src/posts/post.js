import { memo } from 'react';
import { FlatList, Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { styles, width } from './post-style.js';
function Post({ item }) {
  return (
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

              {/* Username and other info on post */}
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

            {/* Interactions section of post */}
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
    </View>)
}

export default memo(Post);