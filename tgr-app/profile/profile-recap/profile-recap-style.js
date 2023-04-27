import { StyleSheet, Dimensions } from 'react-native';

const width = Dimensions.get('window').width;
const height = Dimensions.get('window').height;

export default StyleSheet.create({
    recap: {
        paddingTop: (height * 0.02),
    },
    text: {
        color: 'white',
    },
    listItem: {
        width: width / 3.25,
        height: width / 2,
        borderRadius: 30,
        margin: (width * 0.0125),
    },
});