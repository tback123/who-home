import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { ThemeProvider } from "@material-ui/core/styles";
import theme from "./theme";
import "typeface-roboto";

import LoginPage from "./pages/LoginPage";
import MainPage from "./pages/MainPage";

class App extends Component {
  render() {
    return (
      <Router>
        <ThemeProvider theme={theme}>
          <Switch>
            <Route path={["/", "/login"]} component={LoginPage} exact />
            <Route path="/home" component={MainPage} />
          </Switch>
        </ThemeProvider>
      </Router>
    );
  }
}

export default App;
