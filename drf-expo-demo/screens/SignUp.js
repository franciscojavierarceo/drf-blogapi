import React from 'react';
import { StyleSheet, Text, TextInput, View, Image, Button } from 'react-native';
import MaterialButtonViolet from "../components/MaterialButtonViolet";
import { TouchableOpacity } from 'react-native-gesture-handler';


export default class SignUp extends React.Component {
    state = { email: '', password: '', errorMessage: null }
    handleSignUp = () => {
        console.log('Sign Up state:')
        console.log(this.state)
        function allauthRegister(d) {
            try { 
                const myResponse = fetch("http://localhost:8000/api/v1/rest-auth/login/", {
                    method: 'POST',
                    headers: {
                        Accept: 'application/json',
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: d['email'],
                        email: d['email'],
                        password1: d['password'],
                        password2: d['password'],
                    }),
                });
                console.log(myResponse);
        } catch (error){
            console.log(error);
        }
        };
        allauthRegister(this.state);
    };

render() {
    return (
      <View style={styles.container}>
          <Image source={require("../assets/images/logo.png")}
          resizeMode="contain"
          style={styles.image}
          ></Image>
        <Text>Let's create an account</Text>
        {this.state.errorMessage &&
          <Text style={{ color: 'red' }}>
            {this.state.errorMessage}
          </Text>}
        <TextInput
          placeholder="Email"
          autoCapitalize="none"
          style={styles.textInput}
          onChangeText={email => this.setState({ email })}
          value={this.state.email}
        />
        <TextInput
          secureTextEntry
          placeholder="Password"
          autoCapitalize="none"
          style={styles.textInput}
          onChangeText={password => this.setState({ password })}
          value={this.state.password}
        />
        <Button title="Sign Up" onPress={this.handleSignUp} style={styles.buttonContainer}/>

        <Button
          title="Already have an account? Login"
          onPress={() => this.props.navigation.navigate('Login')}
        />
      </View>
    )
  }
}
const styles = StyleSheet.create({
    image: {
        width: 98,
        height: 98,
        justifyContent: "center",
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
    materialButtonViolet: {
      backgroundColor: "rgba(0,140,255,1)",
      width: 160,
      height: 40,
      borderRadius: 5,
      marginTop: 17,
      marginLeft: 108
    },
});