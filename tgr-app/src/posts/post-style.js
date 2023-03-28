import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
    profileInfo: {
        flexDirection: 'row',
        flexWrap: 'wrap',
    },
    postProfPic: {
        width: '10%',
        height: width * 0.10,
        borderRadius: 60,
        borderWidth: 1,
        borderColor: 'white'
    },
    bigPostImg: {
        padding: 10,
        width: '100%',
        height: ITEM_LENGTH * 1.5,
        borderRadius: 20,
    },
    smallPostImg: {
    position: 'absolute',
    top: 70,
    left: 20,
    width: '45%',
    height: ITEM_LENGTH * 0.6,
    borderRadius: 20,
    borderColor: 'black',
    borderWidth: 3
    },
    userContainer: {
        flexDirection: 'row',
      },
    streakText: {
    color: '#adadad',
    fontSize: 10,
    position: "relative",
    left: 4,
    top: 2
    },
    streakEmoji: {
    color: 'white',
    fontSize: 10,
    position: "relative",
    left: 4,
    top: 2.5
    },
    interactionsText: {
    position: 'absolute',
    color: '#adadad',
    right: 50,
    fontWeight: 'bold',
    bottom: 9
      }
})