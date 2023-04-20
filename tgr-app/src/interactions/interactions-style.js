import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black'
  },
  backArrow: {
    top: width * 0.01,
    left: width * 0.05,
    width: width * 0.1
  },
  username: {
    color: '#FFFFFF',
    textAlign: 'center',
    fontWeight: 'bold',
    top: width * 0.01
  },
  tabs: {
    justifyContent: 'space-around',
    flexDirection: 'row'
  },
  commentsText: {
    color: '#FFFFFF',
    textAlign: 'center',
    fontWeight: 'bold',
    fontSize: width * 0.05,
    width: width * 0.3,
  },
  underlineContainer: {
    borderBottomColor: 'white',
    borderBottomWidth: 1
  },
  reactionsText: {
    color: '#FFFFFF',
    textAlign: 'center',
    fontWeight: 'bold',
    fontSize: width * 0.05,
    width: width * 0.3
  }

});