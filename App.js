import React from 'react';
import { View, Text,Alert } from 'react-native';
import Mappers from './src/components/Mappers';
import Navigate from './src/components/Navigate';
import { Router, Scene } from 'react-native-router-flux';
import Trial from './src/components/Trial';

class App extends React.Component {
  render() {
    return (
      <Router>
        <Scene key="root">
          <Scene key="Mappers"
            component={Mappers}
            //initial
            hideNavBar={true}
          />
          <Scene key="Trial"
            component={Trial}
            initial
            hideNavBar={true}
          />
        </Scene>
      </Router>
    );
  }
}

export default App;