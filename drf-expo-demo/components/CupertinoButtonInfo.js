import React, { Component } from "react";
import { StyleSheet, TouchableOpacity, TextInput } from "react-native";

function CupertinoButtonInfo(props) {
  return (
    <TouchableOpacity style={[styles.container, props.style]}>
      <TextInput
        placeholder="Send Code"
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
    borderRadius: 5
  },
  textInput: {
    width: 90,
    height: 34,
    color: "#fff",
    alignSelf: "center",
    fontSize: 14,
    fontFamily: "roboto-regular",
    textAlign: "center"
  }
});

export default CupertinoButtonInfo;
