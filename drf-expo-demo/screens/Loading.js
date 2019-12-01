import React from 'react';
import { View, Text, ActivityIndicator, StyleSheet, Image } from 'react-native';

const DEFAULT_LOAD_TIME = 5000; // Five second default 

export default class Loading extends React.Component {
    componentDidMount(){
        setTimeout(() => {
            // this.props.navigation.navigate('SignUp');
            this.props.navigation.navigate('Login');
            }, DEFAULT_LOAD_TIME);
    }
    render() {
        return (
        <View style={styles.container}>
          <Image source={require("../assets/images/logo.png")}
          resizeMode="contain"
          style={styles.image}
          ></Image>
          {/* <Text>Loading</Text> */}
          <ActivityIndicator size="small" />
        </View>
    )
  }
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  image: {
    width: 157,
    height: 157,
    marginTop: 0,
    alignSelf: "center"
  },
});