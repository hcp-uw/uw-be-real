import { useMemo, useState } from 'react';
import { FlatList, Text, View, Keyboard, TouchableWithoutFeedback } from 'react-native';
import { SearchBar } from "@rneui/base";
import { styles } from './social-style';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import SocialList from "./social-list";

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
              
      <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
        <View style={styles.searchContainer}>
            <SearchBar
              inputContainerStyle={{backgroundColor: '#1A1A1A'}}
              containerStyle={{backgroundColor: 'black', borderRadius: 100, height: 20}}
              placeholderTextColor={'#C0C0C0'}
              placeholder={'Add or search friends'}
          />
        </View>
      </TouchableWithoutFeedback>

      <Text style={styles.friendsText}>My Friends ({numFriends})</Text>

      {/* List of friends */}
      <FlatList
        style={styles.friendsList}
        data={friends}
        renderItem={({ item }) => <SocialList item={item}
                                               navigation={navigation}/>}
        // ItemSeparatorComponent={() => <View style={{height: 100}} />}
      />

      <View style={{margin: 10}}></View>


      <Text style={styles.requestsText}>Pending Requests ({numRequests})</Text>

      {/* List of requests */}
      <FlatList
        style={styles.requestList}
        data={requests}
        renderItem={({ item }) => <SocialList item={item}
                                               navigation={navigation}/>}
        // ItemSeparatorComponent={() => <View style={{height: 100}} />}
      />


      <Navbar navigation={navigation} 
              pfp={pfp}/>
    </View>
  );
}
