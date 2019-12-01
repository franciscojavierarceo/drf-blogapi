import React from 'react';
import { StyleSheet, Platform, Image, Text, View, Button } from 'react-native';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import { createAppContainer } from 'react-navigation';
import Icon from 'react-native-vector-icons/Ionicons';
import Login from './Login';
import Profile from './Profile';

class Main extends React.Component {
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
                  Hi {currentUser && currentUser.email}! this is your home page.
                </Text>
                <Button
                  title="Let's sign up"
                  onPress={() => this.props.navigation.navigate('SignUp')}
                />
              </View>
            )
          }
        };

const MainTabs = createBottomTabNavigator({
  Main: {
    screen: Main,
    navigationOptions: {
      tabBarLabel: 'Main',
      tabBarIcon: ({ tintColor }) => (
        <Icon name="ios-home" color={tintColor} size={24} />
      )
    },
  },
  Profile: {
    screen: Profile,
    navigationOptions: {
      tabBarLabel: 'Profile',
      tabBarIcon: ({ tintColor }) => (
        <Icon name="ios-person" color={tintColor} size={24} />
      )
    },
  }, 
},
  {
  tabBarOptions: {
    activeTintColor: 'red',
    inactiveTintColor: 'grey',
    style: {
      backgroundColor: 'white',
      borderTopWidth: 0,
      shadowOffset: { width: 5, height: 3 },
      shadowColor: 'black',
      shadowOpacity: 0.5,
      elevation: 2
    }
  }
});


export default createAppContainer(MainTabs);

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