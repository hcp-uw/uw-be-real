import React, { useEffect } from 'react'; 
import { SafeAreaView, Button, StyleSheet, Pressable, TextInput, Animated, View, Keyboard, Dimensions} from 'react-native';
import { useState, useRef } from 'react';

const PreviewScreen = ({route, navigation}) => {
  const {photo, backPhoto} = route.params;
  const [showFront, setShowFront] = useState(true);
  const [caption, setCaption] = useState('');
  const IMAGE_HEIGHT = Dimensions.get('window').width * 1.5;
  const IMAGE_HEIGHT_SMALL = IMAGE_HEIGHT / 3;
  const keyboardHeight = useRef(new Animated.Value(0)).current;
  const imageHeight = useRef(new Animated.Value(IMAGE_HEIGHT)).current;

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
      })
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

      })
    ]).start();
  };
  return (
    <SafeAreaView style={styles.container}>
      <Animated.View style={[styles.container, {paddingBottom: keyboardHeight},]} >
      <Pressable  onPress={() => setShowFront(!showFront)}>
        <Animated.Image
          style={[
            {height: imageHeight, width: imageHeight}
          ]} 
          source={{
            uri: "" +  (showFront ? photo.uri: backPhoto.uri)
          }}
        />
        {/* <Animated.Image 
          style={[
            styles.thumbnail,
            {height: imageHeight / 4},
          ]} 
          source={{
            uri: "" + (showFront ? backPhoto.uri: photo.uri)
          }} 
        /> */}
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

const styles = StyleSheet.create({
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
        top: 0,
        left: 0,
        
        width: 20,
    },
})
export default PreviewScreen;