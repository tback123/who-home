import React from "react";
import { Grid, Paper, Button } from "@material-ui/core";

const SetPersonStatus = ({ People, SetStatusClick }) => {
  return (
    <>
      {People.map((people, key) => (
        <Grid
          container
          item
          xs
          spacing={3}
          justify="center"
          alignItems="center"
          key={key}
        >
          <Grid item>
            <Paper>Name is: {people.name}</Paper>
            <Paper>Home status is: {people.home_status}</Paper>
          </Grid>
          <Grid item>
            <Button
              variant={
                  people.home_status === "home" ?
                  "contained" :
                  "outlined"
                }
              color="primary"
              onClick={() => SetStatusClick(people.name, "home")}
            >
              Home
            </Button>
          </Grid>

          <Grid item>
            <Button
              variant={
                people.home_status === "not_home" ?
                "contained" :
                "outlined"
              }
              color="primary"
              onClick={() => SetStatusClick(people.name, "not_home")}
            >
              Not Home
            </Button>
          </Grid>

          <Grid item>
            <Button
              variant={
                people.home_status === "home_with_extra" ?
                "contained" :
                "outlined"
              }
              color="primary"
              onClick={() => SetStatusClick(people.name, "home_with_extra")}
            >
              Home + 1
            </Button>
          </Grid>
        </Grid>
      ))}
    </>
  );
};

export default SetPersonStatus;
