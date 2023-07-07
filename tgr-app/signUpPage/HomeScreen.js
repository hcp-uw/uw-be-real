import React, { setState } from "react";
import {
    View,
    StyleSheet,
    Text,
    Image,
    SafeAreaView,
    TouchableOpacity,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const HomeScreen = () => {
    const navigation = useNavigation();
    return (
        <SafeAreaView style={styles.background}>
            <Text style={styles.logo}>_tgr.</Text>
            <SafeAreaView
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
                <Text style={styles.text}>Welcome to _tgr!</Text>
                <SafeAreaView style={{ marginTop: 70 }}></SafeAreaView>
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
                        onPress={() => navigation.navigate("Name")}
                    >
                        <Text style={styles.textbutton}>Sign Up</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                        style={styles.button}
                        onPress={() => navigation.navigate("Login")}
                    >
                        <Text style={styles.textbutton}>Log In</Text>
                    </TouchableOpacity>
                </SafeAreaView>
                <SafeAreaView
                    style={{
                        height: 110,
                        minHeight: 10,
                    }}
                ></SafeAreaView>
            </SafeAreaView>
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
    },
    image: {
        width: 130,
        height: 130,
        padding: 20,
    },
    text: {
        color: "white",
        fontWeight: "bold",
        fontSize: 20,
        marginTop: 20,
    },
    textbutton: {
        color: "#000",
        fontWeight: "400",
        fontSize: 19,
        textAlign: "center",
    },
    button: {
        width: "37.5%",
        padding: 8.5,
        // padding: "2.2%",
        paddingHorizontal: 25,
        // paddingHorizontal: "6.47%",
        borderRadius: 100,
        // borderRadius: "100%",
        backgroundColor: "white",
    },
});

export default HomeScreen;
