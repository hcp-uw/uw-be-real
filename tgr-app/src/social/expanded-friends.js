import { FlatList, Text, View } from 'react-native';
import { styles as friendListStyles } from './friend-list-style';
import { styles as socialStyles } from './social-style';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import CustomSearchBar from './search-bar';
import FriendList from "./friend-list";

export default function ExpandedFriends({navigation, route}) {
  const { pfp, friends, numFriends } = route.params

  return (
    <View style={socialStyles.container}>
      <Header navigation={navigation} 
              pfp={pfp}/>
              
      <CustomSearchBar/>

      <Text style={{color: '#FFFFFF',
                    paddingBottom: '2%',
                    fontWeight: 'bold',
                    left: '2%'}}>
        My Friends ({numFriends})
      </Text>

      {/* List of friends */}
      <FlatList
        style={friendListStyles.friendsList}
        data={friends}
        renderItem={({ item }) => <FriendList item={item}
                                              navigation={navigation}/>}
      />

      <Navbar navigation={navigation} 
              pfp={pfp}/>
    </View>
  );
}
