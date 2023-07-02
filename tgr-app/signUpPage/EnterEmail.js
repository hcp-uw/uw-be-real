import React, { useState } from "react";
import {
    StyleSheet,
    Text,
    SafeAreaView,
    TextInput,
    View,
    KeyboardAvoidingView,
    TouchableOpacity,
    TouchableWithoutFeedback,
    Keyboard,
} from "react-native";
import { firebase } from "../config";

function EnterEmail({ navigation, route }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const { firstName, lastName, username } = route.params;
    const [textColor, setTextColor] = useState("#3C3C3C");

    registerUser = async (email, password, firstName, lastName, username) => {
        if (email.endsWith("@uw.edu")) {
            await firebase
                .auth()
                .createUserWithEmailAndPassword(email, password)
                .then(() => {
                    firebase
                        .auth()
                        .currentUser.sendEmailVerification({
                            handleCodeInApp: true,
                            url: "https://uw-be-real.firebaseapp.com",
                        })
                        .then(() => {
                            alert("Verification email sent");
                        })
                        .catch((error) => {
                            alert(error.message);
                        })
                        .then(() => {
                            // replace with neo4j database;
                            // right now, adding to firestore database
                            firebase
                                .firestore()
                                .collection("users")
                                .doc(firebase.auth().currentUser.uid)
                                .set({
                                    firstName,
                                    lastName,
                                    username,
                                    email,
                                    username,
                                });
                        })
                        .catch((error) => {
                            alert(error.message);
                        });
                })
                .catch((error) => {
                    alert(error.message);
                });
        } else {
            alert("Error: Email must end with @uw.edu");
        }
    };

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
                        <Text style={styles.default}>Create an account</Text>
                        <View style={styles.emailView}>
                            <TextInput
                                style={{
                                    color: "white",
                                    fontWeight: "bold",
                                    fontSize: 20,
                                    paddingRight: 2,
                                }}
                                onChangeText={(email) => {
                                    if (email.length > 0) {
                                        setTextColor("white");
                                    } else {
                                        setTextColor("#3C3C3C");
                                    }
                                    setEmail(email);
                                }}
                                placeholder="netid"
                                placeholderTextColor="#3C3C3C"
                                autoCapitalize="none"
                                autoCorrect={false}
                                keyboardType="email-address"
                            />
                            <Text
                                style={{
                                    color: textColor,
                                    fontWeight: "bold",
                                    fontSize: 20,
                                }}
                            >
                                @uw.edu
                            </Text>
                        </View>

                        <TextInput
                            style={styles.textbox}
                            onChangeText={(password) => setPassword(password)}
                            // value={password}
                            placeholder="Password"
                            placeholderTextColor="#3C3C3C"
                            autoCapitalize="none"
                            autoCorrect={false}
                            secureTextEntry={true}
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
                            onPress={() =>
                                navigation.navigate("Username", {
                                    firstName: firstName,
                                    lastName: lastName,
                                })
                            }
                        >
                            <Text style={styles.textbutton}>Back</Text>
                        </TouchableOpacity>
                        <TouchableOpacity
                            style={styles.button}
                            onPress={() => {
                                navigation.navigate("WaitVerification"),
                                    registerUser(
                                        email + "@uw.edu",
                                        password,
                                        firstName,
                                        lastName,
                                        username
                                    );
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
        textAlign: "center",
    },
    textbox: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 20,
    },
    emailView: {
        display: "flex",
        flexDirection: "row",
        padding: 20,
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

export default EnterEmail;
