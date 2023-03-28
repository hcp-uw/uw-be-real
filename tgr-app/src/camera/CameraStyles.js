import { StyleSheet, Dimensions } from "react-native";


const {width} = Dimensions.get('window');


export const IMAGE_HEIGHT = width * 4/3;
export const IMAGE_WIDTH = width;
export const IMAGE_HEIGHT_SMALL = IMAGE_HEIGHT / 2;
export const IMAGE_WIDTH_SMALL = IMAGE_WIDTH / 2;
export const THUMBNAIL_HEIGHT = IMAGE_HEIGHT / 3;
export const THUMBNAIL_WIDTH = width / 3;
export const THUMBNAIL_HEIGHT_SMALL = THUMBNAIL_HEIGHT / 2;
export const THUMBNAIL_WIDTH_SMALL = THUMBNAIL_WIDTH / 2;


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
        // padding: "10%",
        top: "5%",
        left: "5%",
        borderRadius: 20
  },
  smallImageDimensions: {
    height: IMAGE_HEIGHT_SMALL,
    width: IMAGE_WIDTH_SMALL,
    borderRadius: 20
  },
  smallThumbnailDimensions: {
    height: THUMBNAIL_HEIGHT_SMALL,
    width: THUMBNAIL_WIDTH_SMALL,
    
    borderRadius: 10
  },
  previewText: {
    color: 'white',
    fontSize: 30,
    fontWeight: 'bold'
  },
  postOptionsLayout: {
    flexDirection: 'column'
  },
  postOptionsHeaderText: {
    fontSize: 20,
    color: 'white',
    marginLeft: 24
  },
  separator: {
    marginVertical: 8,
    marginHorizontal: 16,
    borderBottomColor: '#737373',
    borderBottomWidth: StyleSheet.hairlineWidth,
  },
  postOptionBlock: {
    flexDirection: 'row',
    backgroundColor: 'black',
    padding: 10
  },
  postOptionBlockSelected: {
    flexDirection: 'row',
    backgroundColor: 'white',
    padding: 10
  }

})