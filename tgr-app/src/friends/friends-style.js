import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black'
  },
  searchContainer: {
    flex: 0.1,
    width: width * 0.98,
    left: 5
  }
});