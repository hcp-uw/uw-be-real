import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View,  Button, TouchableOpacity, Dimensions } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera, CameraType} from 'expo-camera';
import * as MediaLibrary from 'expo-media-library'; 
import { useIsFocused } from '@react-navigation/native';
import { styles } from './CameraScreenStyles.js';

export default function CameraScreen({navigation, route}) {
  let cameraRef = useRef();
  const isFocused = useIsFocused();
  const [hasCameraPermission, setHasCameraPermission] = useState();
  const [hasMediaLibraryPermission, setHasMediaLibraryPermission] = useState();
  const [photo, setPhoto] = useState(undefined);
  const [type, setType] = useState(CameraType.back);
  const [backPhoto, setBackPhoto] = useState(undefined);
  const [backPhotoReady, setBackPhotoReady] = useState(false);
  
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
      
      console.log(cameraRef.current.getAvailablePictureSizesAsync());
      console.log(cameraRef.current.getSupportedRatiosAsync());
      
      // cameraRef.current.pausePreview();
      setPhoto(newPhoto);
      toggleCameraType();
      // cameraRef.current.resumePreview();
      setTimeout(async ()  => {
        newPhoto = await cameraRef.current.takePictureAsync(options);
        setBackPhoto(newPhoto);
      }, 500);
      
      
    
    // else if (!backPhoto) {
    //   
    // }
    
    
  };

  if (photo && backPhoto) {
    
    navigation.navigate("Preview", {photo: photo, backPhoto: backPhoto});
    setPhoto(undefined);
    setBackPhoto(undefined);
    
  }
  function toggleCameraType() {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
  }
  
  return (
    <View style={styles.container}>
      {/* Camera itself */}
      <View style={styles.roundCamera}>
        {isFocused ? <Camera
          ratio="4:3" style={styles.camera} ref={cameraRef} type={type} borderRadius={15} resizeMode="cover" overflow="hidden"
          > 
      
      <StatusBar style="auto" />
     
      </Camera> : null
       }
       </View>
      
      <View style={styles.buttonContainer}>
        {/* Button to take a picture */}
        <TouchableOpacity onPress={takePic}>
          <View style={styles.ring}/>
        </TouchableOpacity>
        {/* Button to reverse the camera */}
        <TouchableOpacity
            style={styles.reverseBtn}
            onPress={toggleCameraType}
          >
              <Text style={styles.reverseText}>Reverse</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}