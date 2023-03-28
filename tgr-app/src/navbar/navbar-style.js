import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
  navbar: {
    flex: 0.05,
    padding: 20,
  },
  navbar_home: {
    left: (width * 0.2)-5,
  },
  navbar_public: {
    left: (width * 0.45)-20,
    top: -34
  }, 
  navbar_friends: {
    left: (width * 0.70)-20,
    top: -70
  },
});