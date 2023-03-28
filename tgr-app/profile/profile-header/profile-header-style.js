import { StyleSheet, Dimensions } from 'react-native';

const width = Dimensions.get('window').width;
const height = Dimensions.get('window').height;

export const styles = StyleSheet.create({
    header: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        paddingHorizontal: (width * 0.05),
    },
    text: {
        color: 'white',
        fontSize: 19,
        fontWeight: 'bold',
    }
});