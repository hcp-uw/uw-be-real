import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
  header: {
    top: 30,
    flex: 0.06,
    padding: 30
  },
  headerText: {
    fontSize: 20,
    top: 4,
    fontWeight: 'bold',
    color: 'white',
  },
  userProfilePic: {
    right: -340,
    top: -25,
    width: '10%',
    height: width * 0.09,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: 'white'
  },
});