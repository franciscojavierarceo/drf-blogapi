import React from 'react';
import { 
  StyleSheet, 
  Platform, 
  Image, 
  Text, 
  View, 
  Button, 
  ScrollView,
  TouchableOpacity } from 'react-native';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import { createAppContainer } from 'react-navigation';
import Icon from 'react-native-vector-icons/Ionicons';
import Login from './Login';
import Profile from './Profile';
import Accounts from './Accounts';
import Card from '../components/Cards';

class Main extends React.Component {
    state = { currentUser: null }
    render() {
        const { currentUser } = this.state
        return (
              <View style={styles.container}>
                <Text style={styles.headerText}>
                  Hi {currentUser && currentUser.email}! this is your Main page.
                </Text>
          <ScrollView
            horizontal={false}
            contentContainerStyle={styles.scrollArea_contentContainerStyle}
          >
            <Card/>
          </ScrollView>
                <Button
                  title="Sign out"
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
      // tabBarIcon: ({ tintColor }) => (
      //   <Icon name="ios-home" color={tintColor} size={24} />
      // )
      tabBarIcon: () => (
        <Image source={require("../assets/images/logo_icon.png")}
        resizeMode="contain"
        style={styles.imageIcon}
        ></Image> 
      ) 
    },
  },
  Profile: {
    screen: Profile,
    navigationOptions: {
      tabBarLabel: 'Profile',
      tabBarIcon: ({ tintColor }) => (
        <Icon name="md-person" color={tintColor} size={24} />
      )
    },
  }, 
  Accounts: {
    screen: Accounts,
    navigationOptions: {
      tabBarLabel: 'Accounts',
      tabBarIcon: ({ tintColor }) => (
        <Icon name="md-add-circle-outline" color={tintColor} size={24} />
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
    marginTop: 60,
    // justifyContent: 'center',
    // flex: 1,
    // justifyContent: 'center',
    // alignItems: 'center',
    // marginTop: 20,
  },
  headerText: {
    marginTop: 60,
    textAlign: 'center',
    fontWeight: 'bold',
  },
  imageIcon: {
        width: 30,
        height: 30,
        justifyContent: "center",
  },
  scrollArea: {
    // top: 0,
    // left: 0,
    // flex: 1,
    // width: 375,
    // height: 620,
    backgroundColor: "rgba(248,248,248,5)",
    // position: "absolute"
  },
  scrollArea_contentContainerStyle: {
    // width: 375,
    // height: 600
    // flex: 1,
  },
  group: {
    // width: 308,
    // height: 576,
    // justifyContent: "space-between",
    marginTop: 22,
    // marginLeft: 34
  },
  scrollAreaStack: {
    // width: 375,
    // height: 674,
    // flex: 1,
    // marginTop: 1
    // justifyContent: "center",
  },
  card: {
    width: 308,
    height: 167,
    backgroundColor: "rgba(255,255,255,5)",
    elevation: 15,
    borderRadius: 25,
    shadowOffset: {
      height: 5,
      width: 5
    },
    shadowColor: "rgba(0,0,0,3)",
    shadowOpacity: 0.15,
    shadowRadius: 5,
    overflow: "hidden",
    marginBottom: 10,
    // justifyContent: "center",
  }
});