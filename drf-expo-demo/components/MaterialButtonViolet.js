import React, { Component } from "react";
import { StyleSheet, TouchableOpacity, TextInput, Button } from "react-native";

function MaterialButtonViolet(props) {
  return (
    <TouchableOpacity
      /* Conditional navigation not supported at the moment */ style={[
        styles.container,
        props.style
      ]}
    >
      <Button
        title="Sign Up"
        color="rgba(255,255,255,1)"
        style={styles.textInput}
        onPress={() => console.log('Sign Up Button Pressed \n', this.props)}
      ></Button>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "rgba(0,140,255,1)",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    // paddingRight: 16,
    // paddingLeft: 16,
    elevation: 2,
    // minWidth: 88,
    borderRadius: 2,
    shadowOffset: {
      height: 1,
      width: 0
    },
    shadowColor: "#000",
    shadowOpacity: 0.35,
    shadowRadius: 5
  },
  textInput: {
    width: 72,
    height: 28,
    color: "#fff",
    margin: 0,
    fontSize: 14,
    textAlign: "center",
    justifyContent: 'center',
    alignItems: 'center'
  }
});

export default MaterialButtonViolet;
