import { useMemo, useState } from 'react';
import { FlatList, Text, View, Keyboard, TouchableWithoutFeedback } from 'react-native';
import { styles } from './social-style';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import FriendList from "./friend-list";
import RequestList from "./request-list";
import CustomSearchBar from './search-bar';

export default function Social({navigation, route}) {
  const { pfp } = route.params

  const [friends, setFriends] = useState();
  const [numFriends, setNumFriends] = useState(0);

  const [requests, setRequest] = useState();
  const [numRequests, setNumRequest] = useState(0);

    useMemo(() => {
      const fetchSocial = fetch('https://raw.githubusercontent.com/AantLe12/DummyData/main/dummy_friends.json').then(res => res.json()).then(data => {
        setFriends(data.friends);
        setNumFriends(Object.keys(data.friends).length);
        setRequest(data.requests);
        setNumRequest(Object.keys(data.requests).length);
      });
  }, []);

  return (
    <View style={styles.container}>
      <Header navigation={navigation} 
              pfp={pfp}/>
              
      <CustomSearchBar/>

      <TouchableWithoutFeedback  onPress={() => 
        navigation.navigate('ExpandedFriends', { pfp: pfp, friends: friends, numFriends: numFriends })
      }>
        <Text style={styles.friendsText}>My Friends ({numFriends})</Text>
      </TouchableWithoutFeedback>

      {/* List of friends */}
      <FlatList
        style={styles.friendsList}
        data={friends}
        renderItem={({ item }) => <FriendList item={item}
                                              navigation={navigation}/>}
      />

      {/* Filler space */}
      <View style={{margin: 10}}></View>


      <TouchableWithoutFeedback  onPress={() => 
        navigation.navigate('ExpandedRequests', { pfp: pfp, requests: requests, numRequests: numRequests })
      }>
        <Text style={styles.requestsText}>Pending Requests ({numRequests})</Text>  
      </TouchableWithoutFeedback>

      {/* List of requests */}
      <FlatList
        style={styles.requestList}
        data={requests}
        renderItem={({ item }) => <RequestList item={item}
                                               navigation={navigation}/>}
      />

      <Navbar navigation={navigation} 
              pfp={pfp}/>
    </View>
  );
}
