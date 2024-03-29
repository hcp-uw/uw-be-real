import { FlatList, Text, View } from 'react-native';
import { styles as requestListStyles } from './request-list-style';
import { styles as socialStyles } from './social-style';
import Header from "../header/header";
import Navbar from "../navbar/navbar";
import CustomSearchBar from './search-bar';
import RequestList from './request-list';

export default function ExpandedRequests({navigation, route}) {
  const { pfp, requests, numRequests } = route.params

  return (
    <View style={socialStyles.container}>
      <Header navigation={navigation} 
              pfp={pfp}/>
              
      <Text style={socialStyles.requestsText}>My Requests ({numRequests})</Text>

      <CustomSearchBar/>

      {/* List of friends */}
      <FlatList
        style={requestListStyles.friendsList}
        data={requests}
        renderItem={({ item }) => <RequestList item={item}
                                              navigation={navigation}/>}
      />

      <Navbar navigation={navigation} 
              pfp={pfp}/>
    </View>
  );
}
