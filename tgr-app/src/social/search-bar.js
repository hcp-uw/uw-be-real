import { View, Keyboard, TouchableWithoutFeedback } from 'react-native';
import { SearchBar } from "@rneui/base";
import { styles } from './social-style';

export default function CustomSearchBar() {
  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
    <View style={styles.searchContainer}>
        <SearchBar
            inputContainerStyle={{backgroundColor: '#1A1A1A'}}
            containerStyle={{backgroundColor: 'black', borderRadius: 100, height: 20}}
            placeholderTextColor={'#C0C0C0'}
            placeholder={'Add or search friends'}
        />
    </View>
    </TouchableWithoutFeedback>
  );
}
