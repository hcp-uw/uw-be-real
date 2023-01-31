import React from 'react'; 
import { SafeAreaView, Image, Button, StyleSheet, Pressable, TextInput, KeyboardAvoidingView, View} from 'react-native';
import { useState } from 'react';

const PreviewScreen = ({route, navigation}) => {
  const {photo, backPhoto} = route.params;
  const [showFront, setShowFront] = useState(true);
  const [caption, setCaption] = useState('');
  let sharePic = () => {
  }
  
    
    
    return (
      <SafeAreaView style={styles.container}>
        <KeyboardAvoidingView style={styles.preview}behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
        <Pressable style={styles.preview} onPress={() => setShowFront(!showFront)}>
          <Image style={styles.preview} source={{ uri: "data:image/jpg;base64," +  (showFront ? photo.base64: backPhoto.base64) }}/>
        <Image style={styles.thumbnail} source={{ uri: "data:image/jpg;base64," + (showFront ? backPhoto.base64: photo.base64) }} />
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
        </KeyboardAvoidingView>
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
    
  },
  horizontalLayout: {
    flexDirection:'row'
  }, 
  thumbnail: {
        position: 'absolute',
        top: 0,
        left: 0,
        width: 80,
        height: 80,
    },
})
export default PreviewScreen;