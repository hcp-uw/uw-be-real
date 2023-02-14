import React, { Component } from 'react';
import { StyleSheet, Dimensions } from 'react-native';

const {width} = Dimensions.get('window');

export default StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        padding: 20,
        backgroundColor: 'black',
    },
    profileImage: {
        width: width / 3,
        height: width / 3,
        borderRadius: width / 6,
        marginVertical: 20,
    },
    name: {
        fontSize: 24,
        fontWeight: 'bold',
        marginVertical: 20,
        color: 'white',
    },
    caption: {
        fontSize: 10,
        fontWeight: 'bold',
        marginVertical: 20,
        color: 'white',
    },
})