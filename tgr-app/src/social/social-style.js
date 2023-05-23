import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black'
  },
  lists: {
    flex: 1,
    left: '2%'
  },
  searchContainer: {
    paddingBottom: '10%',
    width: '98%',
  },
  friendsText: {
    color: '#FFFFFF',
    paddingBottom: '2%',
    fontWeight: 'bold'
  },
  friendsList: {
    flex: 0.1,
    paddingBottom: '10%'
  },
  requestsText: {
    color: '#FFFFFF',
    paddingBottom: '2%',
    fontWeight: 'bold'
  },
  requestList: {
    flex: 0.1,
  },
});