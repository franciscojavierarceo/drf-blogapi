import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import SignUp from "./screens/SignUp";
import Loading from "./screens/Loading"; 
import Login from "./screens/Login";
import Main from "./screens/Main";
import { createSwitchNavigator, createAppContainer } from 'react-navigation';

const RootStack = createSwitchNavigator(
  {
    SignUp: SignUp,
    Loading: Loading,
    Login: Login,
    Main: Main,
  },
  {
    initialRouteName: 'Loading'
  }
);

const App = createAppContainer(RootStack);
export default App ;
