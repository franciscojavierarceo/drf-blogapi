import React from 'react';
import { Text } from 'react-native';
import PlaidLink from 'react-native-plaid-link-sdk';

export default () => (
  <PlaidLink
    publicKey='ff190afeabe7020fd5df34efa775bb'
    clientName='5e0dd57b1a2d810011a28cd8'
    env='sandbox'
    product={['transactions']}
    webviewRedirectUri = "drf://redirect"
    onSuccess={data => console.log('success: ', data)}
    onExit={data => console.log('exit: ', data)}
    language='en'
    countryCodes={['US']}
  >
    <Text>Add Account</Text>
  </PlaidLink>
);
