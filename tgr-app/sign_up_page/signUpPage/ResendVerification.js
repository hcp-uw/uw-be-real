import React, { useState } from "react";
import { View, StyleSheet, Text, SafeAreaView, TextInput } from "react-native";
import { useNavigation } from "@react-navigation/native";
import { firebase } from "../config";

const ResendVerification = () => {
    const navigation = useNavigation();
    const [email, setEmail] = useState("");

    verification = async (email) => {
        try {
            await firebase
                .auth()
                .fetchSignInMethodsForEmail(email)
                .then((result) => {
                    if (result.length > 0) {
                        if (firebase.auth().currentUser.emailVerified) {
                            alert("Error: This email is already verified.");
                        } else {
                            alert("Verification email sent");
                        }
                    } else {
                        alert("Error: Email is not registered.");
                    }
                });
        } catch (error) {
            alert(error.message);
        }
    };

    return (
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <Text style={styles.default}>Enter your email</Text>
            <TextInput
                style={styles.textbox}
                onChangeText={(email) => setEmail(email)}
                placeholder="email@uw.edu"
                placeholderTextColor="#3C3C3C"
                autoCapitalize="none"
                keyboardType="email-address"
            />
            <Text
                style={styles.next}
                onPress={() => {
                    if (this.validateEmail(email)) {
                        verification(email);
                    } else {
                        alert("Error: Invalid Email!");
                    }
                }}
            >
                Resend
            </Text>
            <Text
                style={styles.next}
                onPress={() => {
                    navigation.navigate("Login");
                }}
            >
                Back to Login
            </Text>
        </SafeAreaView>
    );
};

validateEmail = (email) => {
    var re = /^\S*@uw.edu$/;
    return re.test(email);
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

export default ResendVerification;
