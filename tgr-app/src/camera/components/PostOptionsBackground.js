import React, { useMemo } from "react";

import { View } from "react-native";

const PostOptionBackground = ({ animatedIndex, style }) => {


  // styles
  const containerStyle = useMemo(
    () => [
      style,
      {
        backgroundColor: "#000000",
        opacity: 1,
      },
    ],
    [style]
  );

  return <View style={containerStyle} />;
};

export default PostOptionBackground;