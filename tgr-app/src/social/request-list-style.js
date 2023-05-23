import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    requestItem: {
        justifyContent: 'space-between',
        flexDirection: 'row',
        paddingBottom: '5%',
        marginHorizontal: '1%',
        marginRight: '4%'
    },
    profile: {
        flexDirection: 'row',
        columnGap: width * 0.03
    },
    postProfPic: {
        width: width * 0.1,
        height: width * 0.1,
        borderRadius: width * 0.05,
        borderWidth: width * 0.005,
        borderColor: 'white'
    },
    names: {
        flexDirection: 'column'
    },
    name: {
        color: '#FFFFFF',
    },
    username: {
        color: '#959499',
    },
    buttons: {
        flexDirection: 'row',
        columnGap: width * 0.03
    },
    submitBtn: {
        width: width * 0.2,
        borderRadius: width * 0.1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#FFFFFF',
    },
    submitText: {
        color: '#000000'
    },
    rejectBtn: {
        width: width * 0.2,
        borderRadius: width * 0.1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#414141',
    },
    rejectText: {
        color: '#FFFFFF'
    },
})