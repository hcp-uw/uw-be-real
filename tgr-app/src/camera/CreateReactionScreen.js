import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View,  Button, TouchableOpacity, Dimensions } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera, CameraType} from 'expo-camera';
import * as MediaLibrary from 'expo-media-library'; 
import { useIsFocused } from '@react-navigation/native';
import CameraStyles, { IMAGE_HEIGHT, IMAGE_WIDTH } from './CameraStyles';
import { SCREEN_HEIGHT, SCREEN_WIDTH } from '@gorhom/bottom-sheet';

const CreateReaction = ({navigation, route}) => {
  let cameraRef = useRef();
  const {username, id} = route.params;
  const isFocused = useIsFocused();
  const [hasCameraPermission, setHasCameraPermission] = useState();
  const [hasMediaLibraryPermission, setHasMediaLibraryPermission] = useState();
  const [photo, setPhoto] = useState(undefined);
  const PREVIEW_WIDTH = SCREEN_WIDTH * 0.9
  useEffect(() => {
    (async () => {
      const cameraPermission = await Camera.requestCameraPermissionsAsync();
      const mediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();
      setHasCameraPermission(cameraPermission.status === "granted");
      setHasMediaLibraryPermission(mediaLibraryPermission.status === "granted");
      setPhoto(undefined);
    })();
  }, []);

  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text>Permission for camera not granted. Please change this in settings.</Text>
  }
  let takePic = async () => {
    let options = {
      quality: 0.5,
      base64: true,
      exif: false
    };
    
      let newPhoto = await cameraRef.current.takePictureAsync(options);
      
      setPhoto(newPhoto);
      navigation.goBack();
  }
  return (
    <View style={CameraStyles.container}>

        <Text style={{color: 'white', fontSize: 20}}>Replying to @{username}</Text>
        <View style={{margin: 30, height: PREVIEW_WIDTH, width: PREVIEW_WIDTH, borderRadius: PREVIEW_WIDTH/2, overflow: 'hidden', borderColor: 'white', borderWidth: 3}}>

        <Camera ratio="1:1" useCamera2Api={false} style={{height: PREVIEW_WIDTH, width: PREVIEW_WIDTH}} type={CameraType.front} ref={cameraRef} />
        </View>

        <TouchableOpacity onPress={takePic}>
          <View style={CameraStyles.ring}/>
        </TouchableOpacity>
        


    </View>
  ) 
}

export default CreateReaction;