import { StyleSheet, Dimensions } from 'react-native';

const width = Dimensions.get('window').width;
const height = Dimensions.get('window').height;

export const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: 'black',
    },
    text: {
        color: 'white',
        fontSize: 19,
        fontWeight: 'bold',
    },
    image:{ 
        marginTop: (height * 0.0625),
        alignItems: 'center',
    },
    profileImage: {
        width: width / 3,
        height: width / 3,
        borderRadius: width,
    },
});