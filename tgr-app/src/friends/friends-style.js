import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black'
  },
  header: {
    top: 30,
    flex: 0.4,
    padding: 30
  },
  headerText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: 'white',
  },
  userProfilePic: {
    position: 'absolute',
    right: 7,
    top: 25,
    width: '10%',
    height: width * 0.09,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: 'white'
  },
  input: {
    width: width * 0.9,
    height: width*0.1,
    backgroundColor: '#1A1A1A',
    color: '#FFFFFF',
    textAlign: 'left',
    left: 23,
    paddingHorizontal: 20,
    borderWidth: 1,
    borderRadius: 15, 
    fontSize: 16,
  },
  myFriendsText: {
    color: '#adadad',
    paddingTop: 10,
    paddingBottom: 10,
    left: 23,
    fontWeight: 'bold',
  },
  pendingFriendsText: {
    color: '#adadad',
    paddingTop: 10,
    paddingBottom: 10,
    left: 23,
    fontWeight: 'bold',
  },
  friendsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    left: 23
  },
  friendsList: {
    height: width * 0.45
  },
  requestsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    left: 23,
  },
  userText: {
    color: '#959499',
    top: 10,
    left: 5,
  },
  friendProfPic: {
    width: '10%',
    height: width * 0.10,
    borderRadius: 60,
  },
  navbar: {
    position: 'absolute',
    flex: 0.05,
    padding: 20,
  },
  navbar_home: {
    position: 'absolute',
    left: (width * 0.23)-5,
    bottom: -830
  },
  navbar_public: {
    position: 'absolute',
    left: (width * 0.5)-20,
    bottom: -830
  }, 
  navbar_friends: {
    position: 'absolute',
    left: (width * 0.76)-20,
    bottom: -830
  },
});