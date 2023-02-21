import { StyleSheet, Dimensions } from "react-native";


const {width} = Dimensions.get('window');


export const IMAGE_HEIGHT = width * 4/3;
export const IMAGE_WIDTH = width;
export const IMAGE_HEIGHT_SMALL = IMAGE_HEIGHT / 3;
export const IMAGE_WIDTH_SMALL = IMAGE_WIDTH / 3;
export const THUMBNAIL_HEIGHT = IMAGE_HEIGHT / 3;
export const THUMBNAIL_WIDTH = width / 3;
export const THUMBNAIL_HEIGHT_SMALL = THUMBNAIL_HEIGHT / 3;
export const THUMBNAIL_WIDTH_SMALL = THUMBNAIL_WIDTH / 3;


export default StyleSheet.create({
  preview: {
    alignSelf: 'stretch',
    flex: 1,
    alignItems: 'flex-start',
    justifyContent: 'flex-start',
    borderRadius: 30
  }, 
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'black'
  },
  input: {
    backgroundColor: 'black',
    color: 'white',
    margin: 5,
    width: "100%"
    
  },
  horizontalLayout: {
    flexDirection:'row'
  }, 
  thumbnail: {
        position: 'absolute',
        padding: "10%",
        // top: "5%",
        // left: "5%",
  },
  // thumbnailDimensions: {
  //   height: THUMBNAIL_HEIGHT,
  //   width: THUMBNAIL_WIDTH,
  //   smallHeight: THUMBNAIL_HEIGHT_SMALL,
  //   smallWidth: THUMBNAIL_WIDTH_SMALL
  // }

})