import React from 'react';
import { AsyncStorage } from "react-native";
import { Dimensions, StyleSheet, Text, TextInput, View, Button, Image } from 'react-native';
// import { Block, Button as GaButton, theme } from "galio-framework";

const { width } = Dimensions.get("screen");

export default class Login extends React.Component {
    state = { email: '', password: '', errorMessage: null };
    handleLogin = () => {
      // TODO: API stuff...
      console.log('login state:')
      console.log(this.state)
      console.log(this.state['email'])
      async function allauthLogin() {
        try { 
            let response = await fetch("http://localhost:8000/api/v1/rest-auth/login/", {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: this.state['email'],
                    email: this.state['email'],
                    password: this.state['password'],
                }),
            });
            let responseJson = await response.json();
            if (response.status == 200){
              console.log('login succeeded; response = ');
              console.log(responseJson);
              // this.props['accessToken'] = responseJson['key'];
              // d.props.navigtion.navigate('Home')
            }
        } catch (error){
            console.error(error);
        }
    };
    allauthLogin();
    }
    render() {
      return (
        <View style={styles.container}>
          <Image source={require("../assets/images/logo.png")}
          resizeMode="contain"
          style={styles.image}
          ></Image>
          <Text>Welcome back</Text>
          {this.state.errorMessage &&
            <Text style={{ color: 'red' }}>
              {this.state.errorMessage}
            </Text>}
          <TextInput
            style={styles.textInput}
            autoCapitalize="none"
            placeholder="Email"
            onChangeText={email => this.setState({ email })}
            value={this.state.email}
          />
          <TextInput
            secureTextEntry
            style={styles.textInput}
            autoCapitalize="none"
            placeholder="Password"
            onChangeText={password => this.setState({ password })}
            value={this.state.password}
          />
          {/* <Block center>
            <Button textStyle={{ fontFamily: 'open-sans-bold' }} color="info" style={styles.button}>
              INFO
            </Button>
          </Block> */}
          <Button title="Login" 
          // onPress={this.handleLogin} 
          onPress={() => this.handleLogin()} 
          style={styles.buttonContainer}/>
          <Button
            title="Don't have an account? Sign Up"
            onPress={() => this.props.navigation.navigate('SignUp')}
          />
          <Button
            title="Take me home"
            onPress={() => this.props.navigation.navigate('Main')}
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
    textInput: {
      height: 40,
      width: '80%',
      borderColor: 'gray',
      borderWidth: 1,
      marginTop: 8,
      margin: 0,
      borderRadius: 5,
      padding: 5,
    },
    buttonContainer: {
        backgroundColor: "rgba(0,140,255,1)",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
        elevation: 2,
        borderRadius: 2,
        shadowOffset: {
          height: 1,
          width: 0
        },
        shadowColor: "#000",
        shadowOpacity: 0.35,
        shadowRadius: 5
    },
    image: {
        width: 98,
        height: 98,
        justifyContent: "center",
    },
    // button: {
    //   marginBottom: theme.SIZES.BASE,
    //   width: width - theme.SIZES.BASE * 2
    // },
});