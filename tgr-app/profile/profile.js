import React from 'react';
import { 
  SafeAreaView, 
  SectionList, 
  FlatList, 
  Image, 
  View, 
  Text 
} from 'react-native';
import { useEffect, useRef, useState } from 'react';
import styles from './profile-style.js';
import Header from './profile-header/profile-header';
import Recap from './profile-recap/profile-recap';


const Profile = ({navigation, route}) => {

  const [userData, setData] = useState(null);
  const [dummyPosts, setDummyPosts] = useState(null);
  const [profilePhoto, setProfilePhoto] = useState(null);
  const [username, setUsername] = useState(null);
  const [loading, setLoading] = useState(true);

  const [testPhoto, setPhoto] = useState(null);

  useEffect(() => {
    fetchData();
    fetchDummyData();
  }, []);

  const fetchData = async () => {
    const resp = await fetch('https://haosenli.com/data/tgr_dummy_users.json');
    const userData = await resp.json();

    setProfilePhoto(userData[0].details.profile_icon);
    setUsername(userData[0].details.username);
    setLoading(false);
  }

  const fetchDummyData = async () => {
    const resp = await fetch('https://haosenli.com/data/tgr_dummy_posts.json');
    const dummyPosts = await resp.json();

    setDummyPosts(dummyPosts);
    setPhoto(dummyPosts[0].content.front_image);
    setLoading(false);
  }

  return (
    <SafeAreaView style={styles.container}>
      {/* Header */}
      <Header navigation={navigation}/>

      {/* Profile Image */}
      <View style={styles.center}>
      <Image
          style={styles.profileImage}
          source={{uri:profilePhoto}}        
        />
      </View>


      {/* User information */}
      <View style={styles.userInfo}>
        <Text style={styles.text1}>Public Name</Text>
        <Text style={styles.text2}>{username}</Text>
        <Text style={styles.text3}>Bio</Text>
        <Text style={styles.text4}>Location</Text>
      </View>
      

      {/* Recap List */}
      <View style={styles.recap}>
        <Text style={styles.text5}>
          Your Recap
        </Text>
        <Recap data={dummyPosts}/>
      </View>
    </SafeAreaView>
  );
}


export default Profile;