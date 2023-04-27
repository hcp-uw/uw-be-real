import React, { Component } from 'react';
import { StyleSheet, Dimensions } from 'react-native';

const width = Dimensions.get('window').width;
const height = Dimensions.get('window').height;

export default StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
        backgroundColor: 'black',
    },
    center: {
        marginTop: (height * 0.0625),
        alignItems: 'center',

    },
    profileImage: {
        width: width / 3,
        height: width / 3,
        borderRadius: width,
        padding: 10,
    },
    userInfo: {
        marginTop: (height * 0.025),
        alignItems: 'center',
    },
    text1: {
        color: 'white',
        fontWeight: 'bold',
    },
    text2: {
        color: 'white',
        marginTop: (height * 0.0125),
        opacity: 0.75,
    },
    text3: {
        color: 'white',
        marginTop: (height * 0.0125),
        opacity: 0.50,
    },
    text4: {
        color: 'white',
        marginTop: (height * 0.0125),
        opacity: 0.25,
    },
    text5: {
        color: 'white',
        fontWeight: 'bold',
    },
    recap: {
        marginTop: (height * 0.025),
        alignItems: 'center',

    },
    horizontalLine: {
        borderBottomWidth: 1,
        borderBottomColor: 'white',
        marginVertical: 1,
        opacity: 1,
    },
})