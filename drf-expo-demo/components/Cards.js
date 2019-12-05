import React from 'react';
import { StyleSheet, TouchableOpacity, Image, Text, View} from 'react-native';
import { Component } from "react";

class Card extends React.PureComponent {
  render() {
    return (
      <TouchableOpacity style={styles.card} >
        <Text styles={styles.cardText}>Card Title</Text>
        <Image style={styles.cardImage} source={{ uri:'http://blog.edx.org/wp-content/uploads/2016/03/Business-Management.jpg'}} />
      </TouchableOpacity>
    );
  }
};

export default Card;

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    marginBottom: 10,
    marginLeft: '2%',
    width: '96%',
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowRadius: 1, 
    shadowOffset: {
      width: 3,
      height: 3,
    }
  },
  cardImage: {
    width: '100%',
    height: 200,
    resizeMode: 'cover',
  },
  cardText: {
    padding: 10,
    fontSize: 16,
  },
});