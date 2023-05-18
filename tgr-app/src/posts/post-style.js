import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    postContainer: {
        marginHorizontal: '2%',
        paddingBottom: '5%'
    },
    profileInfo: {
        flexDirection: 'row',
        columnGap: width * 0.01
    },
    postProfPic: {
        width: width * 0.1,
        height: width * 0.1,
        borderRadius: width * 0.05,
        borderWidth: width * 0.005,
        borderColor: 'white'
    },
    userContainer: {
        flexDirection: 'column',
        paddingBottom: '3%'
    },
    bigPostImg: {
        height: width * 1.5,
        borderRadius: width * 0.05,
    },
    smallPostImg: {
        position: 'absolute',
        top: 80,
        left: 20,
        width: '45%',
        height: width * 0.6,
        borderRadius: 20,
        borderColor: 'black',
        borderWidth: 3
    },
    interactionsContainer: {
        flexDirection: 'row',
        marginHorizontal: '5%',
        columnGap: width * 0.1,
        paddingTop: '1%',
        textAlign: 'center'
    },
    interactionsText: {
        color: '#adadad',
        fontWeight: 'bold',
    },
    reactionSpace: {
        width: width * 0.04
    }
})