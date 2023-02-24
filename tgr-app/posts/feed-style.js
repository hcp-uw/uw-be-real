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
    flex: 0.06,
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
  bigPostImg: {
    padding: 10,
    width: '100%',
    height: ITEM_LENGTH * 1.5,
    borderRadius: 20,
  },
  smallPostImg: {
    position: 'absolute',
    top: 70,
    left: 20,
    width: '45%',
    height: ITEM_LENGTH * 0.6,
    borderRadius: 20,
    borderColor: 'black',
    borderWidth: 3
  },
  postProfPic: {
    width: '10%',
    height: width * 0.10,
    borderRadius: 60,
    borderWidth: 1,
    borderColor: 'white'
  },
  navbar: {
    flex: 0.05,
    padding: 20,
  },
  navbar_home: {
    position: 'absolute',
    left: (width * 0.23)-5,
    bottom: 30
  },
  navbar_public: {
    position: 'absolute',
    left: (width * 0.5)-20,
    bottom: 30
  }, 
  navbar_friends: {
    position: 'absolute',
    left: (width * 0.76)-20,
    bottom: 30
  }, 
  feed: {
    flex: 1
  },
  profileInfo: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  userContainer: {
    flexDirection: 'row',
  },
  streakText: {
    color: '#adadad',
    fontSize: 10,
    position: "relative",
    left: 4,
    top: 2
  },
  streakEmoji: {
    color: 'white',
    fontSize: 10,
    position: "relative",
    left: 4,
    top: 2.5
  },
  interactionsText: {
    position: 'absolute',
    color: '#adadad',
    right: 50,
    fontWeight: 'bold',
    bottom: 9
  }
});