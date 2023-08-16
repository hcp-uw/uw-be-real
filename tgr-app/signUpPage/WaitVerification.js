import React, { useState } from "react";
import {
    View,
    StyleSheet,
    Image,
    Text,
    SafeAreaView,
    TouchableOpacity,
} from "react-native";
import { firebase } from "../config";

function WaitVerification({ navigation, route }) {
    const { username, firstName, lastName, email } = route.params;

    verify = async () => {
        // Get the latest updates for the current user
        firebase.auth().currentUser.reload();
        // Check if the user verified their email
        if (firebase.auth().currentUser.emailVerified) {
            // Create the user once they verified their email
            fetch('http://' + ip + ':5000/api/user-create', 
                  {
                    method: "POST",
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        "username": username,
                        "firstname": firstName,
                        "lastname": lastName,
                        "email": (email + "@uw.edu")}),
                  }
            ).then((res) => res.json()).then((data) => {
                console.log(data);
                // Navigate to feed
                navigation.navigate("Feed", {username: username});
            }).catch(err => {console.log(err)});
        } else {
            alert("Please verify your email!");
        }
    };

    return (
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <View
                style={{
                    flex: 1,
                    alignItems: "center",
                    justifyContent: "center",
                }}
            >
                <Image
                    style={styles.image}
                    source={require("../assets/togetherlogo.png")}
                ></Image>
                <View style={{ marginTop: 10 }}></View>
                <Text style={styles.text}>
                    Please check your email for verification and proceed.
                </Text>
                <View
                    style={{
                        height: 25,
                        minHeight: 10,
                    }}
                ></View>
            </View>
            <SafeAreaView
                style={{
                    display: "flex",
                    flexDirection: "row",
                    justifyContent: "center",
                    gap: "15%",
                    marginBottom: 15,
                }}
            >
                <TouchableOpacity
                    style={styles.button}
                    onPress={() => navigation.navigate("Home")}
                >
                    <Text style={styles.text1}>Home</Text>
                </TouchableOpacity>
                {/* <View style={{ marginHorizontal: 15 }}></View> */}
                <TouchableOpacity
                    style={styles.button}
                    onPress={() => verify()}
                >
                    <Text style={styles.text1}>Proceed</Text>
                </TouchableOpacity>
            </SafeAreaView>
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    background: {
        backgroundColor: "#000",
        flex: 1,
        //alignItems: "center",
        //justifyContent: "center",
    },
    logo: {
        color: "white",
        fontWeight: "bold",
        fontSize: 16,
        alignSelf: "flex-start",
        paddingLeft: 20,
    },
    image: {
        width: 150,
        height: 150,
        padding: 20,
    },
    text: {
        color: "white",
        fontWeight: "bold",
        fontSize: 19,
        padding: 25,
        textAlign: "center",
    },
    text1: {
        color: "#000",
        fontWeight: "400",
        fontSize: 19,
        textAlign: "center",
    },
    loading: {
        width: 80,
        height: 80,
    },
    button: {
        width: "37.5%",
        padding: 8.5,
        paddingHorizontal: 25,
        borderRadius: 100,
        borderWidth: 0,
        backgroundColor: "white",
    },
});

export default WaitVerification;
