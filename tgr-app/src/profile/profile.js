import { useMemo, useState } from 'react';
import { Text, TextInput, View, TouchableWithoutFeedback, Image, FlatList } from 'react-native';
import { AntDesign, MaterialCommunityIcons, Ionicons, Octicons } from '@expo/vector-icons';
import { styles } from './profile-style';
import FriendItem from '../profile/friend-item';

export default function Profile({navigation, route}) {
  const [name, setName] = useState(" ");
  const [username, setUsername] = useState(" ");
  const [pfp, setPfp] = useState(" ");
  const [bkg, setBkg] = useState(" ");
  const [msg, setMsg] = useState(" ");
  const [major, setMajor] = useState(" ");
  const [location, setLocation] = useState(" ");

  const [friends, setFriends] = useState();
  const [numFriends, setNumFriends] = useState(0);
  const [isEditing, setEdit] = useState(false);
    
  useMemo(() => {
    const fetchUserProf = fetch('https://raw.githubusercontent.com/AantLe12/DummyData/main/dummy_profile.json').then(res => res.json()).then(data => {
      setName(data[0].author_name);
      setUsername("@" + data[0].author_username);
      setPfp(data[0].author_icon);
      setBkg(data[0].author_bkg);
      setMajor(data[0].author_major);
      setMsg(data[0].author_message);
      setLocation(data[0].author_location);
    }).catch(err => { console.log("ERROR")});

    const fetchFriends = fetch('https://raw.githubusercontent.com/AantLe12/DummyData/main/dummy_friends.json').then(res => res.json()).then(data => {
        setFriends(data.friends);
        setNumFriends(Object.keys(data.friends).length);
    });
  }, []);

    return (
      <View style={styles.container}>
          
          {/* Header composed of back btn, profile text, & edit profile btn
            */}
          <View style={styles.profileHeader}>
            <TouchableWithoutFeedback onPress={() => 
              navigation.navigate('Feed')
            }>
                <AntDesign name="arrowleft" size={35} color="white" />
            </TouchableWithoutFeedback>    
            
            <Text style={styles.profileText}>Profile</Text>

            <TouchableWithoutFeedback onPress={() => {
              if(!isEditing) {
                setEdit(true);
              } else {
                setEdit(false);
              }
              }}>
              <MaterialCommunityIcons name="account-cog" size={24} color="white"/>
            </TouchableWithoutFeedback>
          </View>

        <View>
            <Image
              style={styles.bkg} 
              source={{uri: bkg}}
            />

            {/* Container composed of icon, name, & username */}
            <View style={styles.profileIconAndUser}>
              <Image
                            style={styles.pfp} 
                            source={{uri: pfp}}
              />
              <View style={styles.namesContainer}>
                <TextInput style={styles.name} editable={isEditing} value={name} onChangeText={(newName) => setName(newName)}></TextInput>
                <TextInput style={styles.username} editable={isEditing} value={username} onChangeText={(newUser) => setUsername(newUser)}></TextInput>
              </View>
            </View>
          </View>

            {/* User's bio info is composed of location, major, & bio msg */}
          <View style={styles.bioContainer}>
            <View style={styles.bioWithoutMessage}>
              <Octicons name="location" size={24} color="white" />
              <TextInput style={styles.bioInfoText} editable={isEditing} value={location} onChangeText={(newLoc) => setLocation(newLoc)}></TextInput>
              {/* Space between the components */}
              <View style={{margin: 5}}></View>
              <Ionicons name="school" size={24} color="white"/>
              <TextInput style={styles.bioInfoText} editable={isEditing} value={major} onChangeText={(newMajor) => setMajor(newMajor)}></TextInput>
            </View>
            <TextInput style={styles.bioMsg} editable={isEditing} value={msg} onChangeText={(newMsg) => setMsg(newMsg)}></TextInput>
          </View>

          {/* Friends container composed of friends count text,
            * view all friends text, & lost of friends
            */}
          <View style={styles.friendsContainer}>
            <View style={styles.friendsTextContainer}>
              <Text style={styles.sectionText}>Friends({numFriends})</Text>
              <Text style={styles.viewFriendsText}>View All Friends</Text>
            </View>
            <FlatList
              style={styles.friendsList}
              horizontal={true}
              data={friends}
              ItemSeparatorComponent={() => <View style={styles.friendsSpace} />}
              renderItem={({ item }) => <FriendItem item={item}/>}
            />
          </View>
          
          <View style={styles.prevPostsContainer}>
            <Text style={styles.sectionText}>Previous Posts</Text>
          </View>
      </View>
    );
}
