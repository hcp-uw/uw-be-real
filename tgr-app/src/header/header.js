import { View, Text, Image, SafeAreaView, TouchableWithoutFeedback } from 'react-native';
import { styles } from './header-style';
import { Entypo } from '@expo/vector-icons';

export default function Header({navigation, route, username}) {
  // const { username } = route.params;
  // const [pfp, setPfp] = useState("");
  // const [user, setUser] = useState("");

  // function getUserInfo() {
  //   fetch('http://' + ip + ':5000/api/user-profile?netid=' + username)
  //   .then(response => response.text())
  //   .then(text => {
  //     // Access text
  //     console.log(text)
  //     // Set username
  //     // setUser()
  //     // Set pfp
  //     // setPfp()
  //   })
  //   .catch((err) => {
  //     console.log("Could not retrieve " + username + "\'s info");
  //   });
  // }
  // useMemo(() => {
  //   // getUserInfo();
  // }, []);
  return (
    <SafeAreaView style={styles.headerContainer}>
        <Text style={styles.headerText}>_tgr.</Text>
        <View style={styles.profile}>
            {/* Profile picture leading back to profile when clicked on */}
            <TouchableWithoutFeedback  onPress={() => 
              navigation.navigate('Camera', {username: username})}>
              <Entypo name="camera" size={35} color="white"/>
            </TouchableWithoutFeedback>
            {/* Space between camera and profile pic */}
            <View style={{margin: 5}}></View>
            {/* <TouchableWithoutFeedback  onPress={() => 
                navigation.navigate('Profile')}>
                <Image
                    style={styles.userProfilePic}
                    source={{uri: pfp}}
                />
            </TouchableWithoutFeedback> */}
          </View>
    </SafeAreaView>
  );
}