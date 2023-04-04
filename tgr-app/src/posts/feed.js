import { useMemo, useState } from 'react';
import { FlatList, View } from 'react-native';
import { styles } from './feed-style.js';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import Post from "../posts/post";

export default function Feed({navigation, route}) {
  const [posts, setPosts] = useState([]);
  const [pfp, setPfp] = useState(" ");

  useMemo(() => {
    const fetchData = fetch('https://raw.githubusercontent.com/AantLe12/DummyData/main/dummy_posts.json').then(res => res.json()).then(data => {
      setPosts(data);
      setPfp(data[0].author_icon);
    }).catch(err => { console.log("ERROR")});
  }, []);

  return (
    <View style={styles.container}>
      <Header navigation={navigation}
              pfp={pfp}/>

      {/* List of posts */}
      <FlatList
        style={styles.feed}
        data={posts}
        renderItem={({ item }) => <Post navigation={navigation} 
                                        item={item} />}
        ItemSeparatorComponent={() => <View style={{height: 100}} />}
      />

      <Navbar navigation={navigation}
              pfp={pfp}/>
    </View>
  );
}
