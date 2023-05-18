import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    commentContainer: {
        flexDirection: 'row',  
        columnGap: width * 0.04,
    },
    nonProfContainer: {
        flexShrink: width * 0.01,
        width: width * 0.8,
    },
    postProfPic: {
        width: width * 0.1,
        height: width * 0.1,
        borderRadius: width * 0.3,
    },
    userTimeContainer: {
        flexDirection: 'row',
        columnGap: width * 0.01,
    },
    username: {
        color: '#FFFFFF',
        fontWeight: 'bold',
    },
    comment: {
        color: '#FFFFFF',
    },
    commentTime: {
        color: '#808080',
    },
    reply: {
        color: '#808080'
    }
})