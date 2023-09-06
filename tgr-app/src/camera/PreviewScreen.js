import React, { useEffect } from 'react'; 
import { Text, SafeAreaView, Pressable, TextInput, Animated, View, Keyboard, TouchableOpacity} from 'react-native';
import { useState, useRef, useMemo, useCallback } from 'react';
import styles,{ IMAGE_HEIGHT, IMAGE_HEIGHT_SMALL, IMAGE_WIDTH, IMAGE_WIDTH_SMALL} from './CameraStyles.js';
import { THUMBNAIL_HEIGHT, THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT_SMALL, THUMBNAIL_WIDTH_SMALL } from './CameraStyles.js';
import BottomSheet, {BottomSheetBackdrop, useBottomSheetDynamicSnapPoints} from '@gorhom/bottom-sheet';
import { NativeViewGestureHandler } from 'react-native-gesture-handler';
import PostOptionBackground from './components/PostOptionsBackground.js';
import PostOptions from './components/PostOptions.js';

const PreviewScreen = ({route, navigation}) => {
  const {photo, backPhoto, username} = route.params;
  const [showFront, setShowFront] = useState(true);
  const [caption, setCaption] = useState('');
  const [postGlobal, setPostGlobal] = useState(false);
  const keyboardHeight = useRef(new Animated.Value(0)).current;
  const imageHeight = useRef(new Animated.Value(IMAGE_HEIGHT)).current;
  const imageWidth = useRef(new Animated.Value(IMAGE_WIDTH)).current;
  const thumbnailHeight = useRef(new Animated.Value(THUMBNAIL_HEIGHT)).current;
  const thumbnailWidth = useRef(new Animated.Value(THUMBNAIL_WIDTH)).current;
  const bottomSheetRef = useRef(null);
  const snapPoints = useMemo(() => ['25%', '50%' ], []);
  const openOptions = () => bottomSheetRef.current.expand();
  const previewPadding = useRef(new Animated.Value(0)).current;
  const bottomSheetPosition = useRef(new Animated.Value(0)).current;
  
  // renders
  const renderBackdrop = useCallback(
    props => (
      <BottomSheetBackdrop
        {...props}
        opacity={0.1}
        pressBehavior='close'
        
      />
    ),
    []
  ); 
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
  
  const shrinkPreview = () => {
    Animated.parallel([
      Animated.timing(imageHeight, {
        duration: 100,
        toValue: IMAGE_HEIGHT_SMALL,
        useNativeDriver: false
      }),
      Animated.timing(imageWidth, {
        duration: 100,
        toValue: IMAGE_WIDTH_SMALL,
        useNativeDriver: false
      }),
      Animated.timing(thumbnailHeight, {
        duration: 100,
        toValue: THUMBNAIL_HEIGHT_SMALL,
        useNativeDriver: false
      }),
      Animated.timing(thumbnailWidth, {
        duration: 100,
        toValue: THUMBNAIL_WIDTH_SMALL,
        useNativeDriver: false
      }),
      Animated.timing(previewPadding, {
        duration: 100,
        toValue: IMAGE_WIDTH / 1.5,
        useNativeDriver: false
      })
    ]).start();
  };

  const enlargenPreview = () => {
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
      Animated.timing(previewPadding, {
        duration: 100,
        toValue: 0,
        useNativeDriver: false
      })
    ]).start();
  };
  const previewChange = (fromIndex, toIndex) => {
    if (toIndex == 1) {
      shrinkPreview();
    } else {
      enlargenPreview();
    }
  };
  const keyboardWillShow = (event) => {
    console.log("Keyboard appearing: " + imageHeight);
    Animated.parallel([
      Animated.timing(previewPadding, {
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
      Animated.timing(previewPadding, {
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
  let sharePic = () => {
    // navigation.navigate("PostPhoto", {photo: photo, backPhoto: backPhoto});
    console.log("Opened bottom sheet")
    openOptions();
    shrinkPreview();
  };
  return (
    <NativeViewGestureHandler>
    <SafeAreaView style={styles.container}>
      <Animated.View style={[styles.container, {paddingBottom: previewPadding},]} >
      <Pressable onPress={() => setShowFront(!showFront)}>
        <Animated.Image
          style={[
            {height: imageHeight, width: imageWidth, borderRadius: 20}
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
        {/* Post button */}
        <TouchableOpacity
              style={styles.postRetakeBtns}
              onPress={openOptions}
        >
                <Text style={styles.postRetakeBtnsText}>Post</Text>
        </TouchableOpacity>
        {/* Space between post and retake buttons */}
        <View style={{margin: 5}}></View>
        {/* Retake button */}
        <TouchableOpacity
              style={styles.postRetakeBtns}
              onPress={() => {navigation.goBack()}}
        >
                <Text style={styles.postRetakeBtnsText}>Retake</Text>
        </TouchableOpacity>
      </View>
      <BottomSheet 
        ref={bottomSheetRef} index={-1} 
        snapPoints={snapPoints} 
        backdropComponent={renderBackdrop} onAnimate={previewChange}
        backgroundComponent={PostOptionBackground}
        animatedPosition={bottomSheetPosition}>
        <PostOptions front_uri={photo.uri} back_uri={backPhoto.uri} username={username}/>
      </BottomSheet>
    </SafeAreaView>
    </NativeViewGestureHandler>
  );

  };

export default PreviewScreen;