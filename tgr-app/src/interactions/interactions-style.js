import { StyleSheet, Dimensions, Platform } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
  container: {
    backgroundColor: 'black',
    paddingTop: '10%'
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
    paddingBottom: '3%'
  },
  tabs: {
    justifyContent: 'space-around',
    flexDirection: 'row',
    paddingBottom: '3%'
  },
  tabsText: {
    color: '#FFFFFF',
    textAlign: 'center',
    fontWeight: 'bold',
    fontSize: width * 0.05,
  },
  underlineContainer: {
    borderBottomColor: 'white',
    borderBottomWidth: width * 0.001
  },
  reactionsList: {
    left: 5
  },
  commentsList: {
    left: '3%',
    height: '80%'
  },
  commentSpace: {
    height: '6%'
  },
  reactionSpace: {
    height: '1%'
  },
  input: {
    width: '90%',
    borderBottomColor: '#808080',
    borderBottomWidth: width * 0.001,
    left: '5%',
  },
  sendBtn: {
      marginLeft: '75%',
      marginBottom: Platform.OS == 'android' ? '-5%' : '-3%',
      width: '20%',
      alignItems: 'center',
      padding: '2%',
      borderRadius: width * 0.2,
      borderWidth: width * 0.001,
      borderColor: '#808080'
  },
  sendText: {
      color: '#808080'
  }
});