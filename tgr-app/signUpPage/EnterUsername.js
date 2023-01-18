import React, {setState} from 'react';
import { StyleSheet, Text, Image, SafeAreaView, TouchableWithoutFeedback, Button, TextInput } from 'react-native';

function EnterUsername({ navigation }) {
    const [text, onChangeText] = React.useState(null);
    return(
      <SafeAreaView style = {styles.background}>
        <Text style = {styles.logo}>
          _tgr.
        </Text>
        <Text style = {styles.default}>
          Choose your username
        </Text>
        <TextInput
        style = {styles.textbox}
        onChangeText={onChangeText}
        value={text}
        placeholder = "username"
        placeholderTextColor = "#3C3C3C"
        onSubmitEditing = {(value) => navigation.navigate("PhoneNumber")}
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
    default: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        position: "absolute",
        textAlign: "center",
        top: "28%",
        bottom: 0,
    },
      textbox: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        position: "absolute",
        top: "-35%",
        bottom: 0,
    },
});

export default EnterUsername;