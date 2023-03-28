import { View, Text} from 'react-native';
import styles from '../CameraStyles.js'
import Ionicons from '@expo/vector-icons/Ionicons';

// has an icon prop, text prop and a selected boolean prop
const PostOptionBlock = (props) => {
  const curColor = props.selected ? 'black' : 'white';
  return (
    <View style={props.selected ? styles.postOptionBlockSelected : styles.postOptionBlock}> 
      <Ionicons name={props.icon} size={23} color={curColor}/>
      <Text size={20} color={curColor}>{props.text}</Text>
    </View>
  );
};

export default PostOptionBlock;