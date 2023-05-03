import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    commentContainer: {
        flexDirection: 'row',  
        columnGap: '10%',
    },
    nonProfContainer: {
        flexShrink: '1%',
        width: '85%',
    },
    postProfPic: {
        width: width * 0.1,
        height: width * 0.1,
        borderRadius: width * 0.3,
    },
    userTimeContainer: {
        flexDirection: 'row',
        columnGap: '6%',
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