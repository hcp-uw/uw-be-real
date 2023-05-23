import { useState } from 'react';
import { View, Keyboard, TouchableWithoutFeedback } from 'react-native';
import { SearchBar } from "@rneui/base";
import { styles } from './social-style';

export default function CustomSearchBar() {
  const [value, setValue] = useState('');
  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
    <View style={styles.searchContainer}>
        <SearchBar
            inputContainerStyle={{backgroundColor: '#1A1A1A'}}
            containerStyle={{backgroundColor: 'black', borderRadius: 40, height: '2%'}}
            placeholderTextColor={'#C0C0C0'}
            placeholder={'Add or search friends'}
            onChangeText={text => setValue(text)}
            value={value}
        />
    </View>
    </TouchableWithoutFeedback>
  );
}
