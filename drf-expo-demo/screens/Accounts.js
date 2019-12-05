import React from 'react';
import { StyleSheet, ScrollView, TouchableOpacity, Platform, Image, Text, View, Button } from 'react-native';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import { createAppContainer } from 'react-navigation';
import Icon from 'react-native-vector-icons/Ionicons';
import Login from './Login';
import { Component } from "react";

class Card extends React.PureComponent {
  render() {
    return (
      <TouchableOpacity style={styles.card} >
        <Text styles={styles.cardText}>Card Title</Text>
        <Image style={styles.cardImage} source={{ uri:'http://blog.edx.org/wp-content/uploads/2016/03/Business-Management.jpg'}} />
      </TouchableOpacity>
    );
  }
};

class Accounts extends Component {
    state = { currentUser: null }
    render() {
        const { currentUser } = this.state
        return (
              <View style={styles.container}>
                <Text style={styles.headerText}>
                  Hi {currentUser && currentUser.email}! This is your accounts page.
                </Text> 
                <ScrollView>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                </ScrollView>
              </View>
            )
          }
        };

export default Accounts;

const styles = StyleSheet.create({
  container: {
    marginTop: 60,
    backgroundColor: '#F5FCFF',
  },
  headerText: {
    marginTop: 60,
    textAlign: 'center',
    fontWeight: 'bold',
  },
  card: {
    backgroundColor: '#fff',
    marginBottom: 10,
    marginLeft: '2%',
    width: '96%',
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowRadius: 1, 
    shadowOffset: {
      width: 3,
      height: 3,
    }
  },
  cardImage: {
    width: '100%',
    height: 200,
    resizeMode: 'cover',
  },
  cardText: {
    padding: 10,
    fontSize: 16,
  },
  image: {
        width: 98,
        height: 98,
        // justifyContent: "center",
  },
  bottom: {
      // flex: 1,
      // justifyContent: 'flex-end',
      // marginBottom: 36,
  }
});