import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    commentContainer: {
        paddingTop: width * 0.05,
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between'
    },
    postProfPic: {
        width: width * 0.1,
        height: width * 0.1,
        borderRadius: width * 0.3,
    },
    username: {
        color: '#FFFFFF',
        fontWeight: 'bold',
        marginLeft: width * 0.05
    },
    comment: {
        color: '#FFFFFF',
        marginLeft: width * 0.05,
        flexShrink: 1
    },
    commentTime: {
        color: '#565359',
        marginRight: width * 0.05
    }
})