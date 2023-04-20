import { TouchableHighlight, TouchableOpacity } from '@gorhom/bottom-sheet';
import React, {useState} from 'react';
import {View, Text} from 'react-native';
import styles from '../CameraStyles';
import PostOptionBlock from './PostOptionBlock';
const PostOptions = (props) => {
  const [postGlobal, setPostGlobal] = useState(false);
  return (
      <View style={styles.postOptionsLayout}>
        <Text style={styles.postOptionsHeaderText}>Post Visibility</Text>
        <View style={styles.separator}/>
        <TouchableOpacity onPress={() => setPostGlobal(false)}>
          <PostOptionBlock icon="md-people" text="My friends only" selected={!postGlobal}/>
        </TouchableOpacity>
        <View style={styles.separator}/>
        <TouchableOpacity onPress={() => setPostGlobal(true)}>
          <PostOptionBlock icon="earth" text="Everyone (Discovery)" selected={postGlobal}/>
        </TouchableOpacity>
        <TouchableOpacity style={styles.postButton}>
          <Text style={{color: 'black'}} textAlign='center'>Post</Text>
        </TouchableOpacity>
      </View>
  );
};

export default PostOptions;