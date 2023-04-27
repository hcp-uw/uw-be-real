import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
  container: {
    flex: 2,
    backgroundColor: 'black'
  },
  searchContainer: {
    paddingBottom: 50,
    width: width * 0.98,
    left: 5
  },
  friendsText: {
    color: '#FFFFFF',
    left: 5,
    paddingBottom: 10,
    fontWeight: 'bold'
  },
  friendsList: {
    flex: 0.1,
    left: 5
  },
  requestsText: {
    color: '#FFFFFF',
    left: 5,
    paddingBottom: 10,
    fontWeight: 'bold'
  },
  requestList: {
    flex: 0.1,
    left: 5
  },
});