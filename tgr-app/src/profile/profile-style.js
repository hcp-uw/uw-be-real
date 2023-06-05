import { StyleSheet, Dimensions, Platform } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
  container: {
    backgroundColor: 'black',
    paddingTop: '10%',
    flex: 1
  },
  profileHeader: {
    justifyContent: 'space-evenly',
    flexDirection: 'row',
    alignItems: 'center',
    marginHorizontal: '-20%'
  },
  profileText: {
    color: '#FFFFFF',
    fontWeight: 'bold',
  },
  bkg: {
    height: width * 0.75,
    opacity: 0.9
  },
  profileIconAndUser: {
    flexDirection: 'row',
    alignItems: 'center',
    position: 'absolute',
    bottom: '3%',
    left: '3%',
    columnGap: width * 0.05
  },
  pfp: {
    width: width * 0.4,
    height: width * 0.4,
    borderRadius: width * 0.4,
    borderWidth: width * 0.005,
    borderColor: 'white'
  },
  namesContainer: {
    flexDirection: 'column',
    rowGap: width * 0.05
  },
  names: {
    textAlign: 'center',
    paddingBottom: '3%',
  },
  name: {
    color: '#FFFFFF',
    fontWeight: 'bold',
    fontSize: width * 0.05
  },
  username: {
    color: '#FFFFFF',
    fontWeight: 'bold',
    fontSize: width * 0.03
  },
  bioContainer: {
    flexDirection: 'column',
    rowGap: width * 0.03,
    left: '3%',
    paddingBottom: '5%'
  },
  bioWithoutMessage: {
    flexDirection: 'row',
    alignItems: 'center',
    columnGap: width * 0.01
  },
  bioInfoText: {
    color: '#FFFFFF'
  },
  bioMsg: {
    color: '#FFFFFF'
  },
  friendsContainer: {
    left: '3%'
  },
  friendsTextContainer: {
    flexDirection: 'row',
    justifyContent: 'flex-start',
    columnGap: width * 0.5
  },
  sectionText: {
    color: '#FFFFFF',
    fontWeight: 'bold',
    fontSize: width * 0.035
  },
  viewFriendsText: {
    color: '#A7A9AC',
    fontWeight: 'bold',
    fontSize: width * 0.035
  },
  friendsList: {
    paddingBottom: '5%',
    paddingTop: '5%'
  },
  friendsSpace: {
    width: width * 0.04
  },
  prevPostsContainer: {
    left: '3%'
  },
});