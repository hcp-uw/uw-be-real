import { useMemo, useState } from 'react';
import { FlatList, View } from 'react-native';
import { styles } from './feed-style.js';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import Post from "../posts/post";
import "../../Constants.js";

export default function Feed({navigation, route}) {
  const [posts, setPosts] = useState([]);
  const [pfp, setPfp] = useState(" ");
  const { username } = route.params;
  useMemo(() => {
    fetch('http://' + ip + ':5000/api/user-profile?netid=' + username)
    .then(response => response.text())
    .then(text => console.log(text)).catch((err) => {
      console.log("API call error");
    });
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
      />

      <Navbar navigation={navigation}
              pfp={pfp}/>
    </View>
  );
}
