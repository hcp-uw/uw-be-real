import React, { useState } from "react";
import { StyleSheet, Text, SafeAreaView, TextInput } from "react-native";

function EnterPhoneNumber({ navigation, route }) {
    const [number, setNumber] = useState("");
    const { firstName, lastName, username } = route.params;

    return (
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <Text style={styles.default}>Enter your phone number</Text>
            <TextInput
                keyboardType="numeric"
                style={styles.textbox}
                onChangeText={(number) => setNumber(number)}
                value={number}
                placeholder="xxx-xxx-xxxx"
                placeholderTextColor="#3C3C3C"
            />
            <Text
                style={styles.next}
                onPress={() => {
                    if (this.validatePhone(number)) {
                        navigation.navigate("Email", {
                            firstName: firstName,
                            lastName: lastName,
                            username: username,
                            phoneNumber: number,
                        });
                    } else {
                        alert("Error: Please enter your phone number!");
                    }
                }}
            >
                Next
            </Text>
        </SafeAreaView>
    );
}

validatePhone = (phone) => {
    var re = /^\d{10}$/;
    return re.test(phone);
};

const styles = StyleSheet.create({
    background: {
        backgroundColor: "#000",
        flex: 1,
        flexDirection: "column",
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

export default EnterPhoneNumber;
