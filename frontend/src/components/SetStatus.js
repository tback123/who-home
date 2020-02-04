import React from "react";
import { Grid } from "@material-ui/core";
import people from "../data/people"

import SetPersonStatus from "./SetPersonStatus"

class SetStatus extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      home_status: 1
    };
    this.statusClick = this.statusClick.bind(this);
  }

  statusClick = (curr_name, new_status) => {
    people.find(item => item.name === curr_name).home_status = new_status
    this.setState({home_status: this.state.home_status})
  }

  render() {
    return (
      <Grid
        item
        container
        xs
        direction="column"
        justify="center"
        alignItems="center"
        zeroMinWidth
        spacing={0}
      >
        <SetPersonStatus People={people} SetStatusClick={this.statusClick}/>
      </Grid>
    );
  }
}

export default SetStatus;
