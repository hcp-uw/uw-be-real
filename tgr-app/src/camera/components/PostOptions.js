import { TouchableHighlight, TouchableOpacity } from '@gorhom/bottom-sheet';
import React, {useState} from 'react';
import {View, Text} from 'react-native';
import styles from '../CameraStyles';
import PostOptionBlock from './PostOptionBlock';

export default function PostOptions({front_uri, back_uri, username, caption}) {
  const [postGlobal, setPostGlobal] = useState(false);
  
  // Function to make a call to create the post
  function createPost() {
    fetch('http://' + ip + ':5000/api/post-create', 
          {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
              "metadata": {
                "author_id": username,
                "is_global": postGlobal
              },
              "content": {
                "file": [back_uri, front_uri],
                "caption": caption
              }
            }),
          })
    .then((res) => res.json()).then((data) => {
      console.log(data);
    })
    .catch(err => {console.log(err)});
  }
  
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
        <TouchableOpacity style={styles.postButton} 
                          onPress={createPost}>
          <Text style={{color: 'black'}} textAlign='center'>Post</Text>
        </TouchableOpacity>
      </View>
  );
};