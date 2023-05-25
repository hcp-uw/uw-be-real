import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View,  Button, TouchableOpacity, Dimensions } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera, CameraType} from 'expo-camera';
import * as MediaLibrary from 'expo-media-library'; 
import { useIsFocused } from '@react-navigation/native';
import { IMAGE_HEIGHT, IMAGE_WIDTH } from './CameraStyles';
import Ionicons from '@expo/vector-icons/Ionicons';

const CameraScreen = ({navigation, route}) => {
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

  // We could probably set up a screen for these, though I'm not going to do it 
  // rn. 
  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text>Permission for camera not granted. Please change this in settings.</Text>
  }

  async function takePic() {
    let options = {
      quality: 1,
      base64: true,
      exif: false
    };
    
      let newPhoto = await cameraRef.current.takePictureAsync(options);
      
      
      // cameraRef.current.pausePreview();
      setPhoto(newPhoto);
      toggleCameraType();
      // cameraRef.current.resumePreview();
      setTimeout(async ()  => {
        newPhoto = await cameraRef.current.takePictureAsync(options);
        setBackPhoto(newPhoto);
      }, 1000);
      
      
    
    // else if (!backPhoto) {
    //   
    // }
    
    
  };
  function navigateToPreview(photo, backPhoto) {
  let payload = {photo: photo, backPhoto: backPhoto}; 
    setPhoto(undefined);
    setBackPhoto(undefined);
    navigation.navigate("Preview", payload);
  }

  if (photo && backPhoto) {
    navigateToPreview(photo, backPhoto);
    // let payload = {photo: photo, backPhoto: backPhoto}; 
    // setPhoto(undefined);
    // setBackPhoto(undefined);
    // navigation.navigate("Preview", payload);
    
  }
  function toggleCameraType() {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
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

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'black'
  },
  buttonContainer: {
    flexDirection: 'row',
    alignItems: "center",
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
    margin: 10,
    justifyContent: 'center'
  },
  roundCamera: {
    borderRadius: 75
  }

});

export default CameraScreen;