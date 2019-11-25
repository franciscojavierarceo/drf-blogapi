import React, { Component } from "react";
import { StyleSheet, View, TouchableOpacity, Text } from "react-native";
import MaterialCommunityIconsIcon from "react-native-vector-icons/MaterialCommunityIcons";

function MaterialIconTextButtonsFooter1(props) {
  return (
    <View style={[styles.container, props.style]}>
      <TouchableOpacity style={styles.buttonWrapper1}>
        <MaterialCommunityIconsIcon
          name="bank"
          style={styles.icon1}
        ></MaterialCommunityIconsIcon>
        <Text style={styles.btn1Text}>Accounts</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.activeButtonWrapper}>
        <MaterialCommunityIconsIcon
          name="alpha-u"
          style={styles.activeIcon}
        ></MaterialCommunityIconsIcon>
        <Text style={styles.activeContent}>Home</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.buttonWrapper2}>
        <MaterialCommunityIconsIcon
          name="library-books"
          style={styles.icon2}
        ></MaterialCommunityIconsIcon>
        <Text style={styles.btn2Text}>Content</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#FFF",
    flexDirection: "row",
    elevation: 3,
    shadowOffset: {
      height: -2,
      width: 0
    },
    shadowColor: "#111",
    shadowOpacity: 0.2,
    shadowRadius: 1.2
  },
  buttonWrapper1: {
    flex: 1,
    alignItems: "center",
    paddingTop: 8,
    paddingBottom: 10,
    minWidth: 80,
    maxWidth: 168,
    paddingHorizontal: 12
  },
  icon1: {
    backgroundColor: "transparent",
    color: "#616161",
    fontSize: 24,
    opacity: 0.8
  },
  btn1Text: {
    backgroundColor: "transparent",
    color: "#9E9E9E",
    paddingTop: 4,
    fontSize: 12,
    fontFamily: "roboto-regular"
  },
  activeButtonWrapper: {
    flex: 1,
    alignItems: "center",
    paddingTop: 6,
    paddingBottom: 10,
    minWidth: 80,
    maxWidth: 168,
    paddingHorizontal: 12
  },
  activeIcon: {
    backgroundColor: "transparent",
    color: "rgba(0,98,204,1)",
    fontSize: 24,
    opacity: 0.8
  },
  activeContent: {
    backgroundColor: "transparent",
    color: "rgba(0,98,204,1)",
    paddingTop: 4,
    fontSize: 14,
    fontFamily: "roboto-regular"
  },
  buttonWrapper2: {
    flex: 1,
    alignItems: "center",
    paddingTop: 8,
    paddingBottom: 10,
    minWidth: 80,
    maxWidth: 168,
    paddingHorizontal: 12
  },
  icon2: {
    backgroundColor: "transparent",
    color: "#616161",
    fontSize: 24,
    opacity: 0.8,
    height: 24,
    width: 24
  },
  btn2Text: {
    width: 44,
    height: 16,
    backgroundColor: "transparent",
    color: "#9E9E9E",
    paddingTop: 4,
    fontSize: 12,
    fontFamily: "roboto-regular"
  }
});

export default MaterialIconTextButtonsFooter1;
