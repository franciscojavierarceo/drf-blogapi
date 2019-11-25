import React, { Component } from "react";
import { StyleSheet, View, TextInput } from "react-native";
import Icon from "react-native-vector-icons/MaterialCommunityIcons";

function MaterialIconTextbox(props) {
  return (
    <View style={[styles.container, props.style]}>
      <Icon name="email" style={styles.iconStyle}></Icon>
      <TextInput placeholder="Email" style={styles.textInput}></TextInput>
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
  textInput: {
    width: 327,
    height: 43,
    color: "#000",
    alignSelf: "center",
    marginLeft: 16,
    paddingTop: 14,
    paddingRight: 5,
    paddingBottom: 8,
    borderColor: "#D9D5DC",
    fontSize: 16,
    lineHeight: 16
  }
});

export default MaterialIconTextbox;
