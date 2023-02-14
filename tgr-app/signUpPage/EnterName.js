import React, {setState} from 'react';
import { StyleSheet, Text, SafeAreaView, TextInput } from 'react-native';

function EnterName({ navigation }) {
    const [text, onChangeText] = React.useState(null);
    return(
      <SafeAreaView style = {styles.background}>
        <Text style = {styles.logo}>
          _tgr.
        </Text>
        <Text style = {styles.default}>
          Enter your full name
        </Text>
        <TextInput
        style = {styles.textbox}
        onChangeText={onChangeText}
        value={text}
        placeholder = "First Last"
        placeholderTextColor = "#3C3C3C"
        onSubmitEditing = {(value) => navigation.navigate("Username")}
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
    logo: {
        color: "white",
        fontWeight: "bold",
        fontSize: 16,
        position: "absolute",
        top: "5%",
        left: "7%",
        bottom: 0,
        right: 0,
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

export default EnterName;