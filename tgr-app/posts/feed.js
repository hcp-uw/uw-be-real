import { useMemo, useState } from 'react';
import { Dimensions, StyleSheet, FlatList, Text, Image, View } from 'react-native';
import { Foundation, MaterialIcons, Ionicons } from '@expo/vector-icons';

const {width} = Dimensions.get('window');

const ITEM_LENGTH = width;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black'
  },
  profile: {
    position: 'absolute',
    right: 7,
    top: 25,
    width: '10%',
    height: width * 0.09,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: 'white'
  },
  bigImage: {
    padding: 10,
    width: '100%',
    height: ITEM_LENGTH * 1.5,
    borderRadius: 20,
  },
  smallImage: {
    position: 'absolute',
    top: 70,
    left: 20,
    // padding: 10,
    width: '45%',
    height: ITEM_LENGTH * 0.6,
    borderRadius: 20,
    borderColor: 'black',
    borderWidth: 3
  },
  profImage: {
    width: '10%',
    height: width * 0.10,
    borderRadius: 60,
    borderWidth: 1,
    borderColor: 'white'
  },
  logo: {
    top: 30,
    flex: 0.06,
    padding: 30,
  },
  navbar: {
    flex: 0.05,
    padding: 20,
  },
  navbar_home: {
    position: 'absolute',
    left: (width * 0.23)-5,
    bottom: 30
  },
  navbar_public: {
    position: 'absolute',
    left: (width * 0.5)-20,
    bottom: 30
  }, 
  navbar_friends: {
    position: 'absolute',
    left: (width * 0.76)-20,
    bottom: 30
  }, 
  feed: {
    flex: 1
  },
  profileInfo: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'left'
  },
  profileInfoText: {

  },
  userContainer: {
    flexDirection: 'row',
  }
});

export default function App() {
  const [posts, setPosts] = useState([]);
  const [firstPost, setFirst] = useState();
  useMemo(() => {
    const fetchData = fetch('https://haosenli.com/data/tgr_dummy_posts.json').then(res => res.json()).then(data => {
      setPosts(data);
      setFirst(data[0].author_icon);
    });
  }, []);

  return (
    <View style={styles.container}>
      {/* Logo */}
      <View style={styles.logo}>
        <Text style={{
                     fontSize: 20,
                     fontWeight: 'bold',
                     color: 'white',
                     }}>_.tgr
        </Text>
        <Image
          style={styles.profile} 
          source={{uri: firstPost}}
        />
        
      </View>
      <FlatList
        style={styles.feed}
        data={posts}
        // keyExtractor={({ author_username }) => author_username.toString()}
        renderItem={({ item, index }) =>
                                    <View style={styles.itemImage}>
                                      {/* Profile portion of post */}
                                      <View style={styles.profileInfo}>
                                        <Image
                                                style={styles.profImage} 
                                                source={{uri: item.author_icon}}
                                        />

                                        {/* Username and info on post */}
                                        <View style={{
                                          margin: 5,
                                        }}>
                                          <View style={styles.userContainer}>
                                            <Text style={{
                                              color: 'white',
                                            }}>{item.author_username}
                                            </Text>

                                            <Text style={{
                                              color: '#adadad',
                                              fontSize: 10,
                                              position: "relative",
                                              left: 4,
                                              top: 2
                                            }}>{item.author_streak}
                                            </Text>

                                            <Text style={{
                                              color: 'white',
                                              fontSize: 10,
                                              position: "relative",
                                              left: 4,
                                              top: 2.5
                                            }}>{item.author_streak_emoji}
                                            </Text>
                                          </View>
                                          <Text style={{
                                              color: '#adadad',
                                            }}>{ parseInt((parseInt(Date.now() / 1000) - item.post_time) / 3600)} hr Late
                                            </Text>
                                        </View>
                                      </View>
                                      
                                      {/* Space in between who posted and the post itself */}
                                      <View style={{padding: 5}}></View>

                                      {/* User's bigger photo */}
                                      <Image
                                              style={styles.bigImage} 
                                              source={{uri: item.post_front}}
                                              // Easy blur effect for when the user hasn't posted
                                              // blurRadius={30}
                                      />

                                      {/* User's smaller photo */}
                                      <Image
                                                style={styles.smallImage} 
                                                source={{uri: item.post_back}}
                                      />

                                    </View>}
        ItemSeparatorComponent={() => <View style={{height: 120}} />}
      />
      <View style={styles.navbar}>
        <Foundation style={styles.navbar_home} name="home" size={35} color="white" />
        <MaterialIcons style={styles.navbar_public} name="public" size={35} color="white" />
        <Ionicons style={styles.navbar_friends} name="people" size={35} color="white" />
      </View>
    </View>
  );
}
