import { StyleSheet, Dimensions, Platform } from 'react-native';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
  header: {
    justifyContent: 'space-between',
    flexDirection: 'row',
    paddingTop: Platform.OS == 'android' ? (width * 0.05) : 0,
    marginHorizontal: '3%',
    flexWrap: 'wrap',
    height: Platform.OS == 'android' ? (width * 0.17) : (width * 0.24)
  },
  headerText: {
    fontSize: width * 0.06,
    fontWeight: 'bold',
    color: 'white',
  },
  userProfilePic: {
    width: '10%',
    height: width * 0.1,
    borderRadius: width * 0.05,
    borderWidth: width * 0.003,
    borderColor: 'white'
  },
});