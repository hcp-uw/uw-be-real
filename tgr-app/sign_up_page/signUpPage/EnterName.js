import React, { useState } from "react";
import { StyleSheet, Text, SafeAreaView, TextInput, View } from "react-native";
import { useNavigation } from "@react-navigation/native";

const EnterName = () => {
    const navigation = useNavigation();
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [middleName, setMiddleName] = useState("");

    return (
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <Text style={styles.default}>
                Enter your full name (Middle name Optional)
            </Text>
            <TextInput
                style={styles.textbox}
                onChangeText={(firstName) => setFirstName(firstName)}
                textAlign="center"
                placeholder="First"
                placeholderTextColor="#3C3C3C"
                autoCorrect={false}
            />
            <TextInput
                style={styles.textbox}
                onChangeText={(lastName) => setMiddleName(lastName)}
                textAlign="center"
                placeholder="Middle (Opt.)"
                placeholderTextColor="#3C3C3C"
                autoCorrect={false}
            />
            <TextInput
                style={styles.textbox}
                onChangeText={(lastName) => setLastName(lastName)}
                textAlign="center"
                placeholder="Last"
                placeholderTextColor="#3C3C3C"
                autoCorrect={false}
            />
            <Text
                style={styles.next}
                onPress={() => {
                    if (
                        this.validateName(firstName) &&
                        this.validateName(lastName)
                    ) {
                        navigation.navigate("Username", {
                            firstName: firstName,
                            middleName: middleName,
                            lastName: lastName,
                        });
                    } else {
                        alert("Error: Please enter your full name");
                    }
                }}
            >
                Next
            </Text>
        </SafeAreaView>
    );
};

validateName = (name) => {
    var re = /^[\S]{1,64}$/;
    return re.test(name);
};

const styles = StyleSheet.create({
    background: {
        backgroundColor: "#000",
        flex: 1,
        alignItems: "center",
        //flexDirection: "row",
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

export default EnterName;
