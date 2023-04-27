import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
  header: {
    height: width * 0.23,
    left: 20,
  },
  headerText: {
    fontSize: 20,
    top: 7,
    fontWeight: 'bold',
    color: 'white',
  },
  userProfilePic: {
    right: -345,
    top: -25,
    width: '10%',
    height: width * 0.1,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: 'white'
  },
});