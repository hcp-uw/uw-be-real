import { useEffect, useMemo, useState } from 'react';
import { FlatList, Text, Image, View, TouchableWithoutFeedback, TextInput, ScrollView } from 'react-native';
import { Foundation, MaterialIcons, Ionicons } from '@expo/vector-icons';
import { styles } from './friends-style';

export default function Friends({navigation, route}) {
  const [profilePic, setProfilePic] = useState();
  const [friends, setFriends] = useState();
  const [numFriends, setNumFriends] = useState(0);

    useEffect(() => {
      const fetchProfile = fetch('https://haosenli.com/data/tgr_dummy_posts.json').then(res => res.json()).then(data => {
        setProfilePic(data[0].author_icon);
      });

      const fetchFriends = fetch('https://haosenli.com/data/tgr_dummy_friends.json').then(res => res.json()).then(data => {
        setFriends(data.friends);
        setNumFriends(Object.keys(data.friends).length);
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
              source={{uri: profilePic}}
            />
        </TouchableWithoutFeedback >
      </View>

      {/* Friend search bar */}
      <View style={styles.searchBar}>
        <ScrollView keyboardShouldPersistTaps='handled'
                    scrollEnabled={false}>
            <TextInput style={styles.input} placeholder="Add or search friends"
                      placeholderTextColor="#C0C0C0"></TextInput>
        </ScrollView>
      </View>

      <Text style={styles.myFriendsText}>My Friends ({numFriends}) </Text>

      {/* Friends list */}
      <FlatList
        style={styles.friendsList}
        data={friends}
        scrollEnabled={false}
        renderItem={({ item }) =>                    
          <View style={styles.friendsContainer}>
            <TouchableWithoutFeedback  onPress={() => 
              navigation.navigate('Profile')
            }>
              <Image
                      style={styles.friendProfPic} 
                      source={{uri: item.icon}}
              />
            </TouchableWithoutFeedback>

            {/* Username and info on post */}
            <View>
            <Text style={styles.userText}>
              {item.username}
            </Text>
            </View>
          </View>}
        ItemSeparatorComponent={() => <View style={{height: 20}} />}
      />

      <Text style={styles.pendingFriendsText}>Pending Requests ({numFriends}) </Text>

      <FlatList
        data={friends}
        scrollEnabled={false}
        renderItem={({ item }) =>                    
          <View style={styles.requestsContainer}>
            <TouchableWithoutFeedback  onPress={() => 
              navigation.navigate('Profile')
            }>
              <Image
                      style={styles.friendProfPic} 
                      source={{uri: item.icon}}
              />
            </TouchableWithoutFeedback>

            {/* Username and info on post */}
            <View>
            <Text style={styles.userText}>
              {item.username}
            </Text>
            </View>
          </View>}
        ItemSeparatorComponent={() => <View style={{height: 20}} />}
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
