import React, { useState } from "react";
import {
    StyleSheet,
    Text,
    View,
    SafeAreaView,
    TextInput,
    KeyboardAvoidingView,
    TouchableOpacity,
    TouchableWithoutFeedback,
    Keyboard,
} from "react-native";

function EnterUsername({ navigation, route }) {
    const [username, setUsername] = useState("");
    const { firstName, lastName } = route.params;

    return (
        <KeyboardAvoidingView
            behavior={Platform.OS == "ios" ? "padding" : null}
            style={{ flex: 1 }}
        >
            <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
                <SafeAreaView style={styles.background}>
                    <Text style={styles.logo}>_tgr.</Text>
                    <View
                        style={{
                            flex: 1,
                            justifyContent: "flex-start",
                            alignItems: "center",
                        }}
                    >
                        <Text style={styles.default}>Choose your username</Text>
                        <TextInput
                            style={styles.textbox}
                            onChangeText={(username) => setUsername(username)}
                            placeholder="username"
                            placeholderTextColor="#3C3C3C"
                            autoCapitalize="none"
                        />
                    </View>
                    <View
                        style={{
                            display: "flex",
                            flexDirection: "row",
                            justifyContent: "center",
                            gap: "15%",
                            marginBottom: 15,
                        }}
                        behavior="padding"
                    >
                        <TouchableOpacity
                            style={styles.button}
                            onPress={() => navigation.navigate("Name")}
                        >
                            <Text style={styles.textbutton}>Back</Text>
                        </TouchableOpacity>
                        <TouchableOpacity
                            style={styles.button}
                            onPress={() => {
                                if (this.validateUsername(username)) {
                                    navigation.navigate("Email", {
                                        firstName: firstName,
                                        lastName: lastName,
                                        username: username,
                                    });
                                } else {
                                    alert("Error: Invalid Username!");
                                }
                            }}
                        >
                            <Text style={styles.textbutton}>Next</Text>
                        </TouchableOpacity>
                    </View>
                </SafeAreaView>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
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
        textAlignVertical: "center",
    },
    textbutton: {
        color: "#000",
        fontWeight: "400",
        fontSize: 19,
        textAlign: "center",
    },
    button: {
        width: "42.5%",
        padding: 8.5,
        paddingHorizontal: 25,
        borderRadius: 100,
        backgroundColor: "white",
    },
});

export default EnterUsername;
