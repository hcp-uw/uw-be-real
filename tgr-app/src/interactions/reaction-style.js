import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    postContainer: {
        paddingTop: width * 0.05,
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between'
    },
    postProfPic: {
        width: width * 0.3,
        height: width * 0.3,
        borderRadius: width * 0.3,
    },
    username: {
        color: '#FFFFFF',
        fontWeight: 'bold',
        marginLeft: width * 0.05
    },
    reactionTime: {
        color: '#565359',
        marginRight: width * 0.05
    }
})