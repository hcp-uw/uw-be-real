import {React} from 'react';
import { SafeAreaView } from 'react-native-safe-area-context';
import {Text, Image, View} from 'react-native';
import styles from './CameraStyles';
const PostScreen = ({navigation, route}) => {
  const {photo, backPhoto} = route.params;
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.previewText}>Preview</Text>
      <View>
      <Image style={styles.smallImageDimensions} source={{uri: photo.uri}}/>
      <Image style={[styles.thumbnail, styles.smallThumbnailDimensions]} source={{uri: backPhoto.uri}}/>
      </View>
    </SafeAreaView>
  ); 
}

export default PostScreen;