import { StyleSheet, Dimensions } from 'react-native';

export const {width} = Dimensions.get('window');

export const ITEM_LENGTH = width;

export const styles = StyleSheet.create({
  navbar: {
    height: width * 0.15,
    flexDirection: 'row',
    marginHorizontal: '25%',
    justifyContent: 'space-between'
    // columnGap: width * 0.15,
    // paddingTop: '1%'
  },
});