import React, { Component } from "react";
import { StyleSheet, View, TextInput } from "react-native";
import Icon from "react-native-vector-icons/MaterialCommunityIcons";

function MaterialIconTextbox3(props) {
  return (
    <View style={[styles.container, props.style]}>
      <Icon name="security" style={styles.iconStyle}></Icon>
      <TextInput
        placeholder="Verification Code"
        style={styles.inputStyle}
      ></TextInput>
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
    fontFamily: "Roboto",
    fontSize: 24,
    paddingLeft: 8
  },
  inputStyle: {
    width: 204,
    color: "#000",
    alignSelf: "stretch",
    marginLeft: 16,
    paddingTop: 14,
    paddingRight: 5,
    paddingBottom: 8,
    fontSize: 16,
    fontFamily: "roboto-regular",
    lineHeight: 16
  }
});

export default MaterialIconTextbox3;
