import React from 'react'
import { StyleSheet, Text, TextInput, View, Button, Image } from 'react-native';


export default class Login extends React.Component {
    state = { email: '', password: '', errorMessage: null }
    handleLogin = () => {
      // TODO: Firebase stuff...
      console.log('login state:')
      console.log(this.state)
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
          <Button title="Login" onPress={this.handleLogin} style={styles.buttonContainer}/>
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
});