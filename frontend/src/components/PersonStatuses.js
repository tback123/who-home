import React from "react";
import { Grid } from "@material-ui/core";
import { PersonStatus } from "./PersonStatus";

const PersonStatuses = ({ people }) => {
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
      {people.map((person, key) => (
        <PersonStatus person={person} key={key} />
      ))}
    </Grid>
  );
};

export default PersonStatuses;
