import React, { useState } from "react";
import {
    View,
    StyleSheet,
    Image,
    Text,
    SafeAreaView,
    TextInput,
    Alert,
} from "react-native";
import { useNavigation } from "@react-navigation/native";
import { firebase } from "../config";

const Login = () => {
    const navigation = useNavigation();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    loginUser = async (email, password) => {
        try {
            await firebase
                .auth()
                .signInWithEmailAndPassword(email, password)
                .then(() => {
                    if (firebase.auth().currentUser.emailVerified) {
                        //alert("Error: Email is verified.")
                    } else {
                        Alert.alert(
                            "Un-Verified Email",
                            "Resend UW email verification?",
                            [
                                {
                                    text: "Yes",
                                    onPress: () =>
                                        firebase
                                            .auth()
                                            .currentUser.sendEmailVerification({
                                                handleCodeInApp: true,
                                                url: "https://uw-be-real.firebaseapp.com",
                                            })
                                            .then(() => {
                                                alert(
                                                    "Verification email sent"
                                                );
                                            })
                                            .catch((error) => {
                                                alert(error.message);
                                            }),
                                },
                                { text: "No" },
                            ]
                        );
                    }
                });
        } catch (error) {
            alert(error.message);
        }
    };

    return (
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <Image
                style={styles.image}
                source={require("../assets/togetherlogo.png")}
            ></Image>
            <View style={{ marginTop: 20 }}>
                <TextInput
                    style={styles.textbox}
                    placeholder="Email"
                    placeholderTextColor="#3C3C3C"
                    onChangeText={(email) => setEmail(email)}
                    autoCapitalize="none"
                    autoCorrect={false}
                    keyboardType="email-address"
                />
                <TextInput
                    style={styles.textbox}
                    placeholder="Password"
                    placeholderTextColor="#3C3C3C"
                    onChangeText={(password) => setPassword(password)}
                    autoCapitalize="none"
                    autoCorrect={false}
                    secureTextEntry={true}
                />
            </View>
            <Text
                style={styles.button}
                onPress={() => loginUser(email, password)}
            >
                Login
            </Text>
            <Text
                style={styles.verification}
                onPress={() => {
                    navigation.navigate("ResendVerification");
                }}
            >
                Resend verification email
            </Text>
        </SafeAreaView>
    );
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
        paddingBottom: 50,
    },
    image: {
        width: 150,
        height: 150,
        padding: 20,
    },
    textbox: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 20,
        textAlign: "center",
    },
    button: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 20,
    },
    verification: {
        color: "white",
        fontWeight: "bold",
        fontSize: 12,
        padding: 20,
    },
});

export default Login;
