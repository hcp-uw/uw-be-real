import React, { useEffect } from 'react'; 
import { SafeAreaView, Button, StyleSheet, Pressable, TextInput, Animated, View, Keyboard, Dimensions} from 'react-native';
import { useState, useRef } from 'react';
import styles,{ IMAGE_HEIGHT, IMAGE_HEIGHT_SMALL, IMAGE_WIDTH, IMAGE_WIDTH_SMALL} from './CameraStyles.js';
import { THUMBNAIL_HEIGHT, THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT_SMALL, THUMBNAIL_WIDTH_SMALL } from './CameraStyles.js';
const PreviewScreen = ({route, navigation}) => {
  const {photo, backPhoto} = route.params;
  const [showFront, setShowFront] = useState(true);
  const [caption, setCaption] = useState('');
  const keyboardHeight = useRef(new Animated.Value(0)).current;
  const imageHeight = useRef(new Animated.Value(IMAGE_HEIGHT)).current;
  const imageWidth = useRef(new Animated.Value(IMAGE_WIDTH)).current;
  const thumbnailHeight = useRef(new Animated.Value(THUMBNAIL_HEIGHT)).current;
  const thumbnailWidth = useRef(new Animated.Value(THUMBNAIL_WIDTH)).current;

  console.log("Actual image height: " + IMAGE_HEIGHT);
  console.log(imageHeight);
  console.log("Image small height: " + IMAGE_HEIGHT_SMALL);
  useEffect(() => {
    const keyboardWillShowSub = Keyboard.addListener('keyboardDidShow', keyboardWillShow);
    const keyboardWillHideSub = Keyboard.addListener('keyboardDidHide', keyboardWillHide);

    return () => {
      keyboardWillShowSub.remove();
      keyboardWillHideSub.remove();
    }
  }, []);

  let sharePic = () => {
    navigation.navigate("PostPhoto", {photo: photo, backPhoto: backPhoto});
  }
  
  const keyboardWillShow = (event) => {
    console.log("Keyboard appearing: " + imageHeight);
    Animated.parallel([
      Animated.timing(keyboardHeight, {
        duration: event.duration,
        toValue: event.endCoordinates.height,
        useNativeDriver: false
      }),
      Animated.timing(imageHeight, {
        duration: event.duration,
        toValue: IMAGE_HEIGHT_SMALL,
        useNativeDriver: false
      }),
      Animated.timing(imageWidth, {
        duration: event.duration,
        toValue: IMAGE_WIDTH_SMALL,
        useNativeDriver: false
      }),
      Animated.timing(thumbnailHeight, {
        duration: event.duration,
        toValue: THUMBNAIL_HEIGHT_SMALL,
        useNativeDriver: false
      }),
      Animated.timing(thumbnailWidth, {
        duration: event.duration,
        toValue: THUMBNAIL_WIDTH_SMALL,
        useNativeDriver: false
      }),
    ]).start();
  };
  
  const keyboardWillHide = (event) => {
    console.log(imageHeight);
    Animated.parallel([
      Animated.timing(keyboardHeight, {
        duration: 100,
        toValue: 0,
        useNativeDriver: false
      }),
      Animated.timing(imageHeight, {
        duration: 100,
        toValue: IMAGE_HEIGHT,
        useNativeDriver: false
      }),
      Animated.timing(imageWidth, {
        duration: 100,
        toValue: IMAGE_WIDTH,
        useNativeDriver: false
      }),
      Animated.timing(thumbnailHeight, {
        duration: 100,
        toValue: THUMBNAIL_HEIGHT,
        useNativeDriver: false
      }),
      Animated.timing(thumbnailWidth, {
        duration: 100,
        toValue: THUMBNAIL_WIDTH,
        useNativeDriver: false
      }),
    ]).start();
  };
  return (
    <SafeAreaView style={styles.container}>
      <Animated.View style={[styles.container, {paddingBottom: keyboardHeight},]} >
      <Pressable  onPress={() => setShowFront(!showFront)}>
        <Animated.Image
          style={[
            {height: imageHeight, width: imageWidth}
          ]} 
          source={{
            uri: "" +  (showFront ? photo.uri: backPhoto.uri)
          }}
        />
        <Animated.Image 
          style={[
            styles.thumbnail,
            {height: thumbnailHeight, width: thumbnailWidth},
          ]} 
          source={{
            uri: "" + (showFront ? backPhoto.uri: photo.uri)
          }} 
        />
        </Pressable>
       <TextInput
        style={styles.input}
        text={caption}
        onChangeText={(newValue) => {
          setCaption(newValue);
        }}
        textAlign='center'
        placeholder="Test Caption"
        placeholderTextColor="grey"
      />
      
      </Animated.View>
      <View style={styles.horizontalLayout}>
        <Button title="Post" onPress={sharePic} />
        <Button title="Retake" onPress={() => {navigation.goBack()}} />
      </View>
    </SafeAreaView>
  );

  };

export default PreviewScreen;