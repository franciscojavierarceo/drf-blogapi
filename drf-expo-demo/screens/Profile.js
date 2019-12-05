import React from 'react';
import { StyleSheet, Platform, Image, Text, View, Button } from 'react-native';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import { createAppContainer } from 'react-navigation';
import Icon from 'react-native-vector-icons/Ionicons';
import Login from './Login';
import { Component } from "react";

class Profile extends Component {
    state = { currentUser: null }
    render() {
        const { currentUser } = this.state
        return (
              <View style={styles.container}>
                <Text style={styles.headerText}>
                  Hi {currentUser && currentUser.email}! This is your profile page.
                </Text>

                    <Button
                      title="Signout"
                      onPress={() => this.props.navigation.navigate('SignUp')}
                    />
              </View>
            )
          }
        };

export default Profile;

const styles = StyleSheet.create({
  container: {
    marginTop: 60,
    // flex: 1,
    // justifyContent: 'center',
    // alignItems: 'center',
    // padding: 10
  },
  headerText: {
    marginTop: 60,
    textAlign: 'center',
    fontWeight: 'bold',
  },
  image: {
        width: 98,
        height: 98,
        // justifyContent: "center",
  },
  bottom: {
      // flex: 1,
      // justifyContent: 'flex-end',
    //   marginBottom: 36,
  }
});