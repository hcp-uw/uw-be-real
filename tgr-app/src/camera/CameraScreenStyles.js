import { StyleSheet, Dimensions, Platform } from 'react-native';
import { IMAGE_HEIGHT, IMAGE_WIDTH } from './CameraStyles';

export const {width} = Dimensions.get('window');

export const styles = StyleSheet.create({
    container: {
      flex: 1,
      height: '100%',
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: 'black'
    },
    buttonContainer: {
      flexDirection: 'row',
      alignItems: 'center'
    },
    smallPreview: {
      alignSelf: 'flex-start',
      aspectRatio: 0.5,
      marginLeft: 50,
    }, 
    camera: {
      margin: 5,
      width: IMAGE_WIDTH,
      height: IMAGE_HEIGHT,
    },
    ring: {
      width: 150,
      height: 150,
      borderRadius: 75,
      backgroundColor: "transparent",
      borderColor: "white",
      borderWidth: 5,
      alignSelf: 'center', 
      margin: 10,
      justifyContent: 'center'
    },
    roundCamera: {
      borderRadius: 75
    },
  
  });