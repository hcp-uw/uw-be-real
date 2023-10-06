import { useMemo, useState } from 'react';
import { FlatList, View, RefreshControl } from 'react-native';
import { styles } from './feed-style.js';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import Post from "../posts/post";
import "../../Constants.js";

export default function Feed({navigation, route}) {
  const [refreshing, setRefreshing] = useState(false);
  const { username, is_global } = route.params;
  const [user, setUser] = useState("");
  const [global, setGlobal] = useState(true)
  const [posts, setPosts] = useState([]);
  const [pfp, setPfp] = useState("");

  const refreshFeed = () => {
    setRefreshing(true)
    getPosts()
    setTimeout(() => {
      setRefreshing(false)
    }, 4000)
  }

  function getPosts() {
    fetch('http://' + ip + ':5000/api/get-posts?is_global=' + global)
    .then(response => response.text())
    .then(text => {
      // Convert JSON string to JSON
      setPosts(JSON.parse(text))
    })
    .catch((err) => {
      console.log("Could not retrieve posts");
    });
  }
  useMemo(() => {
    setUser(username);
    setGlobal(is_global);
    getPosts();
  }, []);

  return (
    <View style={styles.container}>
      {/* Header */}
      <Header navigation={navigation}
              username={user}
      />

      {/* List of posts */}
      <FlatList
        style={styles.feed}
        data={posts}
        renderItem={({ item }) => <Post navigation={navigation} 
                                        item={item} />}
        refreshControl={
                  <RefreshControl refreshing={refreshing} onRefresh={() => refreshFeed()} />
                                        }
      />

      {/* Navbar */}
      <Navbar navigation={navigation}
              pfp={pfp}
      />
    </View>
  );
}
