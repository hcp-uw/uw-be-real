import React, { useState } from "react";
import { StyleSheet, Text, SafeAreaView, TextInput } from "react-native";
import { firebase } from "../config";

function EnterEmail({ navigation, route }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const { firstName, middleName, lastName, username, phoneNumber } =
        route.params;

    registerUser = async (
        email,
        password,
        firstName,
        middleName,
        lastName,
        phoneNumber,
        username
    ) => {
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
                                    middleName,
                                    lastName,
                                    username,
                                    email,
                                    phoneNumber,
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
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <Text style={styles.default}>
                Enter your UW Email and set a new password
            </Text>
            <TextInput
                style={styles.textbox}
                onChangeText={(email) => setEmail(email)}
                value={email}
                placeholder="example@uw.edu"
                placeholderTextColor="#3C3C3C"
                autoCapitalize="none"
                autoCorrect={false}
                keyboardType="email-address"
            />
            <TextInput
                style={styles.textbox}
                onChangeText={(password) => setPassword(password)}
                value={password}
                placeholder="password"
                placeholderTextColor="#3C3C3C"
                autoCapitalize="none"
                autoCorrect={false}
                secureTextEntry={true}
            />
            <Text
                style={styles.next}
                onPress={() => {
                    navigation.navigate("WaitVerification"),
                        registerUser(
                            email,
                            password,
                            firstName,
                            middleName,
                            lastName,
                            phoneNumber,
                            username
                        );
                }}
            >
                Next
            </Text>
        </SafeAreaView>
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
    next: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 20,
    },
});

export default EnterEmail;
