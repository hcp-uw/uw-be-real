import React, { Component } from 'react';
import { StyleSheet, Dimensions } from 'react-native';

const {width} = Dimensions.get('window');

export default styles = StyleSheet.create({
    container: {
    },
    profile: {
      width: '10%',
      height: width * 0.09,
      borderRadius: 20,
      borderWidth: 1,
      borderColor: 'white'
    },
    bigImage: {
      padding: 10,
      width: '100%',
      height: ITEM_LENGTH * 1.5,
      borderRadius: 20,
    },
    smallImage: {
      position: 'absolute',
      top: 70,
      left: 20,
      width: '45%',
      height: ITEM_LENGTH * 0.6,
      borderRadius: 20,
      borderColor: 'black',
      borderWidth: 3
    },
    profImage: {
      width: '10%',
      height: width * 0.10,
      borderRadius: 60,
      borderWidth: 1,
      borderColor: 'white'
    },
    logo: {
      top: 30,
      flex: 0.06,
      padding: 30,
    },
    navbar: {
      flex: 0.05,
      padding: 20,
    },
    navbar_home: {
      position: 'absolute',
      left: (width * 0.23)-5,
      bottom: 30
    },
    navbar_public: {
      position: 'absolute',
      left: (width * 0.5)-20,
      bottom: 30
    }, 
    navbar_friends: {
      position: 'absolute',
      left: (width * 0.76)-20,
      bottom: 30
    }, 
    feed: {
      flex: 1
    },
    profileInfo: {
      flexDirection: 'row',
      flexWrap: 'wrap',
      justifyContent: 'left'
    },
    profileInfoText: {
  
    },
    userContainer: {
      flexDirection: 'row',
    },
    item_reaction: {
      width: '560%',
      height: width * 0.08,
      borderRadius: 30,
      borderWidth: 2.8,
      borderColor: 'white'
    },
    interactionsText: {
      position: 'absolute',
      color: '#adadad',
      right: 50,
      fontWeight: 'bold',
      bottom: 11
    }
  });