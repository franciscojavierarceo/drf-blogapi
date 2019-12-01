import React from 'react';
import { StyleSheet, Platform, Image, Text, View, Button } from 'react-native';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import { createAppContainer } from 'react-navigation';
import Icon from 'react-native-vector-icons/Ionicons';
import Login from './Login';
import { Component } from "react";

class Accounts extends Component {
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
                  Hi {currentUser && currentUser.email}! This is your accounts page.
                </Text>

                <View style={styles.bottom}>
                    <Button
                      title="Let's sign up"
                      onPress={() => this.props.navigation.navigate('Main')}
                    />
                </View>
              </View>
            )
          }
        };

export default Accounts;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 10
  },
  image: {
        width: 98,
        height: 98,
        justifyContent: "center",
  },
  bottom: {
      flex: 1,
      justifyContent: 'flex-end',
      // marginBottom: 36,
  }
});