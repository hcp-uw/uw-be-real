import React, { useState } from "react";
import {
    StyleSheet,
    Text,
    Keyboard,
    SafeAreaView,
    TextInput,
    View,
    TouchableOpacity,
    KeyboardAvoidingView,
    TouchableWithoutFeedback,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const EnterName = () => {
    const navigation = useNavigation();
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");

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
                        }}
                    >
                        <Text style={styles.default}>Enter your name</Text>
                        <SafeAreaView
                            style={{
                                flexDirection: "row",
                                justifyContent: "center",
                                gap: "15%",
                                marginBottom: 15,
                            }}
                        >
                            <TextInput
                                style={styles.textbox}
                                onChangeText={(firstName) =>
                                    setFirstName(firstName)
                                }
                                placeholder="First"
                                placeholderTextColor="#3C3C3C"
                                autoCorrect={false}
                            />
                            <TextInput
                                style={styles.textbox}
                                onChangeText={(lastName) =>
                                    setLastName(lastName)
                                }
                                placeholder="Last"
                                placeholderTextColor="#3C3C3C"
                                autoCorrect={false}
                            />
                        </SafeAreaView>
                    </View>
                    <View
                        style={{
                            height: 25,
                            minHeight: 10,
                        }}
                    ></View>
                    <View
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
                            <Text style={styles.textbutton}>Back</Text>
                        </TouchableOpacity>
                        <TouchableOpacity
                            style={styles.button}
                            onPress={() => {
                                if (
                                    this.validateName(firstName) &&
                                    this.validateName(lastName)
                                ) {
                                    navigation.navigate("Username", {
                                        firstName: firstName,
                                        lastName: lastName,
                                    });
                                } else {
                                    alert("Error: Please enter your full name");
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
        width: "45%",
        textAlign: "center",
        overflow: "hidden",
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

export default EnterName;
