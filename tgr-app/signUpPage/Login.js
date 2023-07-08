import React, { useState } from "react";
import {
    View,
    StyleSheet,
    Image,
    Text,
    SafeAreaView,
    TextInput,
    Alert,
    TouchableOpacity,
    KeyboardAvoidingView,
    Keyboard,
    TouchableWithoutFeedback,
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
        <KeyboardAvoidingView
            behavior={Platform.OS == "ios" ? "padding" : null}
            style={{ flex: 1 }}
        >
            <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
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
                    <View
                        style={{
                            display: "flex",
                            flexDirection: "row",
                            justifyContent: "center",
                            gap: "15%",
                            marginBottom: 15,
                            marginTop: 30,
                        }}
                    >
                        <TouchableOpacity
                            style={styles.button}
                            onPress={() => navigation.navigate("Name")}
                        >
                            <Text style={styles.textbutton}>Sign Up</Text>
                        </TouchableOpacity>
                        <TouchableOpacity
                            style={styles.button}
                            onPress={() => loginUser(email, password)}
                        >
                            <Text style={styles.textbutton}>Log In</Text>
                        </TouchableOpacity>
                    </View>
                </SafeAreaView>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
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
        paddingBottom: 100,
    },
    image: {
        width: 120,
        height: 120,
        padding: 20,
    },
    textbox: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        padding: 5,
        textAlign: "center",
    },
    button: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
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

export default Login;
