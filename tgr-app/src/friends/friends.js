import { useMemo, useState } from 'react';
import { FlatList, Text, View, Keyboard, TouchableWithoutFeedback } from 'react-native';
import { SearchBar } from "@rneui/base";
import { styles } from './friends-style';
import Header from "../header/header";
import Navbar from "../navbar/navbar";

export default function Friends({navigation, route}) {
  const { pfp } = route.params

  const [friends, setFriends] = useState();
  const [numFriends, setNumFriends] = useState(0);

    useMemo(() => {
      const fetchFriends = fetch('https://raw.githubusercontent.com/AantLe12/DummyData/main/dummy_friends.json').then(res => res.json()).then(data => {
        setFriends(data.friends);
        setNumFriends(Object.keys(data.friends).length);
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

      <Navbar navigation={navigation} 
              pfp={pfp}/>
    </View>
  );
}
