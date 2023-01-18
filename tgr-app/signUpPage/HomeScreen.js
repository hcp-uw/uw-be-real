import React, {setState} from 'react';
import { StyleSheet, Text, Image, SafeAreaView, TouchableWithoutFeedback, Button, TextInput } from 'react-native';

function HomeScreen({ navigation }) {
    return(
      <SafeAreaView style = {styles.background}>
        <Text style = {styles.logo}>
          _tgr.
        </Text>
        <Image 
        style={styles.image}
        source = {require("../assets/togetherlogo.png")}
        >
        </Image>
        <Button
          color = "white"
          title = "Sign Up"
          onPress={() => navigation.navigate('Name')}
        />
  
        <Button
          color = "white"
          title = "Log in"
          onPress={() => console.log("Log in")}
        />
      </SafeAreaView>
    );
  }

  const styles = StyleSheet.create({
    background: {
      backgroundColor: '#000',
      flex: 1,
      justifyContent: "center",
      alignItems: "center",
    },
    image: {
        width: 150,
        height: 150,
        position: "absolute",
        top: "25%",
        bottom: 0,
    },
});

export default HomeScreen;