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
    submitBtn: {
        top: -66,
        left: 200,
        width: width * 0.2,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 10,
        borderRadius: 100,
        backgroundColor: '#FFFFFF',
    },
    submitText: {
        color: '#000000'
    },
    rejectBtn: {
        top: -105,
        left: 300,
        width: width * 0.2,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 10,
        borderRadius: 100,
        backgroundColor: '#414141',
    },
    rejectText: {
        color: '#FFFFFF'
    },
})