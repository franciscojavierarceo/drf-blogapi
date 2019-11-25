import React from 'react';
import { StyleSheet, Platform, Image, Text, View, Button } from 'react-native';

export default class Main extends React.Component {
    state = { currentUser: null }
    render() {
        const { currentUser } = this.state
        return (
              <View style={styles.container}>
                <Image source={require("../assets/images/logo.png")}
                resizeMode="contain"
                style={styles.image}
                ></Image>
                <Text>
                  Hi {currentUser && currentUser.email}!
                </Text>
                <Button
                  title="Let's sign up"
                  onPress={() => this.props.navigation.navigate('SignUp')}
                />
              </View>
            )
          }
        };

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  image: {
        width: 98,
        height: 98,
        justifyContent: "center",
  }
});