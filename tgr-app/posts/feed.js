import { useMemo, useState } from 'react';
import { Dimensions, StyleSheet, FlatList, Text, Image, View } from 'react-native';
import { Foundation } from '@expo/vector-icons';


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
  itemImage: {
    padding: 10,
    width: '100%',
    height: ITEM_LENGTH * 1.5,
    borderRadius: 20,
    resizeMode: 'cover',
  },
  profImage: {
    width: '15%',
    height: width * 0.15,
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
    top: 10,
    width: '100%',
    height: ITEM_LENGTH * 40,
  }, 
  feed: {
    flex: 1
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
                                    <View>
                                      <Image
                                              style={styles.profImage} 
                                              source={{uri: item.author_icon}}
                                      />
                                    </View>
                                    {/* Space in between who posted and the post itself */}
                                    <View style={{padding: 10}}></View>
                                    {/* Default user's front photo */}
                                    <Image
                                            style={styles.itemImage} 
                                            source={{uri: item.post_front}}
                                            // Easy blur effect for when the user hasn't posted
                                            // blurRadius={30}
                                    />
                                    </View>}
        ItemSeparatorComponent={() => <View style={{height: 120}} />}
      />
      <View style={styles.navbar}>
        <Foundation name="home" size={35} color="white" />
      </View>
    </View>
  );
}
