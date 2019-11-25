import React, { Component } from "react";
import { StyleSheet, TouchableOpacity, TextInput } from "react-native";

function MaterialButtonViolet1(props) {
  return (
    <TouchableOpacity style={[styles.container, props.style]}>
      <TextInput
        placeholder="Sign in"
        placeholderTextColor="rgba(255,255,255,1)"
        style={styles.textInput}
      ></TextInput>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "rgba(0,140,255,1)",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    paddingRight: 16,
    paddingLeft: 16,
    elevation: 2,
    minWidth: 88,
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
    width: 59,
    height: 28,
    color: "#fff",
    fontSize: 14,
    textAlign: "center"
  }
});

export default MaterialButtonViolet1;
