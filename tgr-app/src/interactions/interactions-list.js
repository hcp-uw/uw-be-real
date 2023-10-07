import { memo } from 'react';
import { Image, View, Dimensions } from 'react-native';
export const {width} = Dimensions.get('window');
function InteractionsList({ item, index }) {
  // console.log(item)
  return (
    <View>
        <Image
        style={{width: '560%',
                height: width * 0.075,
                borderRadius: 30,
                borderWidth: 2.8,
                borderColor: 'white',
                // opacity: (1 -0.1 * index),
        }} 
        source={{uri: item.reaction_uri}}
        />
    </View>)
}

export default memo(InteractionsList);