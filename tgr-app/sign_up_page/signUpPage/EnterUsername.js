import React, { useState } from "react";
import { StyleSheet, Text, SafeAreaView, TextInput } from "react-native";

function EnterUsername({ navigation, route }) {
    const [username, setUsername] = useState("");
    const { firstName, middleName, lastName } = route.params;

    return (
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <Text style={styles.default}>Choose your username</Text>
            <TextInput
                style={styles.textbox}
                onChangeText={(username) => setUsername(username)}
                placeholder="username"
                placeholderTextColor="#3C3C3C"
                autoCapitalize="none"
            />
            <Text
                style={styles.next}
                onPress={() => {
                    if (this.validateUsername(username)) {
                        navigation.navigate("PhoneNumber", {
                            firstName: firstName,
                            middleName: middleName,
                            lastName: lastName,
                            username: username,
                        });
                    } else {
                        alert("Error: Invalid Username!");
                    }
                }}
            >
                Next
            </Text>
        </SafeAreaView>
    );
}

validateUsername = (username) => {
    var re = /^[\S]{1,64}$/;
    return re.test(username);
};

const styles = StyleSheet.create({
    background: {
        backgroundColor: "#000",
        flex: 1,
        alignItems: "center",
    },
    logo: {
        color: "white",
        fontWeight: "bold",
        fontSize: 16,
        alignSelf: "flex-start",
        paddingLeft: 20,
    },
    default: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 20,
        paddingTop: 90,
    },
    textbox: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 20,
    },
    next: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 20,
    },
});

export default EnterUsername;
