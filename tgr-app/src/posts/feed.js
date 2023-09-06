import { useMemo, useState } from 'react';
import { FlatList, View } from 'react-native';
import { styles } from './feed-style.js';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import Post from "../posts/post";
import "../../Constants.js";

export default function Feed({navigation, route}) {
  const { username } = route.params;
  const [posts, setPosts] = useState([]);
  // TEMPLATE FUNCTION TO RETRIEVE POSTS
  // function getPostInfo() {
  //   fetch('http://' + ip + ':5000/api/user-profile?netid=' + username)
  //   .then(response => response.text())
  //   .then(text => {
  //     // Access text
  //     console.log(text)
  //     // Set username
  //     // setUser()
  //     // Set pfp
  //     // setPfp()
  //   })
  //   .catch((err) => {
  //     console.log("Could not retrieve latest posts");
  //   });
  // }
  // useMemo(() => {
  //   getPostInfo();
  // }, []);

  return (
    <View style={styles.container}>
      <Header navigation={navigation}
              username={username}/>

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
