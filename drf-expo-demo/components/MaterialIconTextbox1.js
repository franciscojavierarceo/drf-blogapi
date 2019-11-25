import React, { Component } from "react";
import { StyleSheet, View, TextInput } from "react-native";
import Icon from "react-native-vector-icons/MaterialCommunityIcons";

function MaterialIconTextbox1(props) {
  return (
    <View style={[styles.container, props.style]}>
      <Icon name="security-lock" style={styles.iconStyle}></Icon>
      <TextInput placeholder="Password" style={styles.inputStyle}></TextInput>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "transparent",
    flexDirection: "row",
    alignItems: "center"
  },
  iconStyle: {
    color: "rgba(0,140,255,1)",
    fontFamily: "roboto-regular",
    fontSize: 24,
    paddingLeft: 8
  },
  inputStyle: {
    width: 327,
    height: 43,
    color: "rgba(255,255,255,1)",
    marginLeft: 16,
    paddingTop: 14,
    paddingRight: 5,
    paddingBottom: 8,
    fontSize: 16,
    lineHeight: 16
  }
});

export default MaterialIconTextbox1;
