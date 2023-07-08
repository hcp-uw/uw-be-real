import { Text, StyleSheet, SafeAreaView, TouchableOpacity } from "react-native";
import React, { useState, useEffect } from "react";
import { firebase } from "../config";

const tempDashboard = () => {
    const [name, setName] = useState("");

    useEffect(() => {
        firebase
            .firestore()
            .collection("users")
            .doc(firebase.auth().currentUser.uid)
            .get()
            .then((snapshot) => {
                if (snapshot.exists) {
                    setName(snapshot.data());
                } else {
                    console.log("User does not exist");
                }
            });
    }, []);
    return (
        <SafeAreaView style={styles.container}>
            <Text style={{ fontSize: 20, fontWeight: "bold", color: "white" }}>
                Hello {name.firstName}
            </Text>
            <TouchableOpacity
                onPress={() => {
                    firebase.auth().signOut();
                }}
                style={styles.button}
            >
                <Text style={{ fontSize: 22, fontWeight: "bold" }}>
                    Sign out
                </Text>
            </TouchableOpacity>
        </SafeAreaView>
    );
};

export default tempDashboard;

const styles = StyleSheet.create({
    container: {
        backgroundColor: "#000",
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
    },
    button: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        position: "absolute",
        top: "45%",
        bottom: 0,
    },
});
