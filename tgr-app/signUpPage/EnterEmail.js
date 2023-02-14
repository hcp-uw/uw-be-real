import React, {setState} from 'react';
import { StyleSheet, Text, SafeAreaView, TextInput } from 'react-native';

function EnterEmail({ navigation }) {
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
        placeholder = "example@uw.edu"
        placeholderTextColor = "#3C3C3C"
        onSubmitEditing = {(value) => navigation.navigate("Verification")}
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

export default EnterEmail;