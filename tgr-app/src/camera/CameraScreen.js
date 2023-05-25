import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera, CameraType} from 'expo-camera';
import * as MediaLibrary from 'expo-media-library'; 
import { useIsFocused } from '@react-navigation/native';
import styles, { IMAGE_HEIGHT, IMAGE_WIDTH } from './CameraStyles';
import Ionicons from '@expo/vector-icons/Ionicons';

const CameraScreen = ({navigation, route}) => {
  let cameraRef = useRef();
  const isFocused = useIsFocused();
  const [hasCameraPermission, setHasCameraPermission] = useState();
  const [hasMediaLibraryPermission, setHasMediaLibraryPermission] = useState();
  const [photo, setPhoto] = useState(undefined);
  const [type, setType] = useState(CameraType.back);
  const [backPhoto, setBackPhoto] = useState(undefined);
  
  useEffect(() => {
    (async () => {
      const cameraPermission = await Camera.requestCameraPermissionsAsync();
      const mediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();
      setHasCameraPermission(cameraPermission.status === "granted");
      setHasMediaLibraryPermission(mediaLibraryPermission.status === "granted");
      setPhoto(undefined);
      setBackPhoto(undefined);
    })();  
  }, []);  
  
  async function takePic() {
    let options = {
      quality: 1,
      base64: true,
      exif: false,
      quality: 0.5
    };
    
      let newPhoto = await cameraRef.current.takePictureAsync(options);
      
      
      cameraRef.current.pausePreview();
      setPhoto(newPhoto);
      toggleCameraType();
      cameraRef.current.resumePreview();
      setTimeout(async ()  => {
        newPhoto = await cameraRef.current.takePictureAsync(options);
        setBackPhoto(newPhoto);
      }, 1000);
  };

  function navigateToPreview(photo, backPhoto) {
    let payload = {photo: photo, backPhoto: backPhoto}; 
    setPhoto(undefined);
    setBackPhoto(undefined);
    navigation.navigate("Preview", payload);
  }

  function toggleCameraType() {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
  }
  
  // We could probably set up a screen for these, though I'm not going to do it 
  // rn. 
  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text>Permission for camera not granted. Please change this in settings.</Text>
  }  

  if (photo && backPhoto) {
    navigateToPreview(photo, backPhoto);
  }
  
  return (
    <View style={styles.container}>
      
      <View style={styles.roundCamera}>
        {isFocused && <Camera
          ratio="4:3" style={styles.camera} ref={cameraRef} type={type} borderRadius={15} resizeMode="cover" overflow="hidden"
          >
      
      <StatusBar style="auto" />
     
      </Camera>
       }
       </View>
      
      <View style={styles.buttonContainer}>
        <View style={{flex: 0.6}}></View>
        <TouchableOpacity onPress={takePic} style={{flex: 1}} >
          <View style={styles.ring}/>
        </TouchableOpacity>
        
        <TouchableOpacity onPress={toggleCameraType} style={{flex: 0.5}}>
          <Ionicons name="camera-reverse-outline" size={60} color="white"/>
        </TouchableOpacity>
      </View>
    </View>
  );
}


export default CameraScreen;