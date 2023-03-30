import { 
  SafeAreaView, 
  SectionList, 
  FlatList, 
  Image, 
  View, 
  Text 
} from 'react-native';
import { React, useEffect, useRef, useState, useContext } from 'react';
import { ProfileContext } from '../ProfileContext';
import { styles } from './profile-edit-style'
import Header from '../profile-header/profile-header'

const Edit = ({navigation}) => {
    const profileContext = useContext(ProfileContext);

    return (
        <SafeAreaView style={styles.container}>
            {/* Header Bar */}
            <Header
                navigation={navigation}
                leftnav={'Profile'}
                mid={'Edit Profile'}
                rightnav={'Profile'}
            />

            {/* Profile Image Change */}
            <Text style={styles.text}>Test1</Text>
            <View style={styles.image}>
                <Image
                    style={styles.profileImage}
                    source={{uri: profileContext.profilePhoto}}
                    // source={{uri:'https://media.istockphoto.com/id/1129084458/photo/real-chinese-young-man-with-very-excited-expression-and-closed-eyes.jpg?s=612x612&w=0&k=20&c=ghZ6gG4oJr0PWvsKU3Gac7xacyj4-OnAjUB375M9T0I='}}        
                />
            </View>

            {/* User Info Change */}
           <View>

           </View>

        </SafeAreaView>
    )

}

export default Edit;