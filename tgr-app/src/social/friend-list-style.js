import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    item: {
        height: width * 0.15
    },
    postProfPic: {
        width: '10%',
        height: width * 0.10,
        borderRadius: 60,
        borderWidth: 1,
        borderColor: 'white'
    },
    name: {
        color: '#FFFFFF',
        top: -35,
        left: 50
    },
    username: {
        color: '#959499',
        top: -36,
        left: 50
    },
    editText: {
        color: '#FFFFFF',
        left: 370,
        top: -65
    }
})