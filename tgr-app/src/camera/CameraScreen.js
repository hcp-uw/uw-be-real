import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View,  Button, TouchableOpacity, Dimensions } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera, CameraType} from 'expo-camera';
import * as MediaLibrary from 'expo-media-library'; 
import { useIsFocused } from '@react-navigation/native';
import { IMAGE_HEIGHT, IMAGE_WIDTH } from './CameraStyles';

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

  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text>Permission for camera not granted. Please change this in settings.</Text>
  }

  let takePic = async () => {
    let options = {
      quality: 1,
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
      <View style={styles.roundCamera}>
        {isFocused && <Camera
          ratio="4:3" style={styles.camera} ref={cameraRef} type={type} borderRadius={15} resizeMode="cover" overflow="hidden"
          >
      
      <StatusBar style="auto" />
     
      </Camera>
       }
       </View>
      
      <View style={styles.buttonContainer}>
        <TouchableOpacity onPress={takePic}>
          <View style={styles.ring}/>
        </TouchableOpacity>
        
        <Button title="Reverse" onPress={toggleCameraType}/>
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
    flexDirection: 'row'
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
  }

});

export default CameraScreen;