import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
  navbar: {
    height: width * 0.15
  },
  navbar_home: {
    left: (width * 0.15),
    top: 10
  },
  navbar_public: {
    left: (width * 0.44),
    top: -25
  }, 
  navbar_friends: {
    left: (width * 0.75),
    top: -65
  },
});