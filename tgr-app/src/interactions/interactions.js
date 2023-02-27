import { useMemo, useState } from 'react';
import { FlatList, Text, Image, View, TouchableWithoutFeedback } from 'react-native';
import { Foundation, MaterialIcons, Ionicons } from '@expo/vector-icons';
import { styles } from './interactions-style';

export default function Interactions({navigation, route}) {
  const [firstPost, setFirst] = useState();
    useMemo(() => {
      const fetchData = fetch('https://haosenli.com/data/tgr_dummy_posts.json').then(res => res.json()).then(data => {
      setFirst(data[0].author_icon);
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
              source={{uri: firstPost}}
            />
        </TouchableWithoutFeedback >
      </View>

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
