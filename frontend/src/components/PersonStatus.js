import React, { useCallback, useState } from "react";
import { Grid, Paper, Button } from "@material-ui/core";

export const PersonStatus = ({ person: defaultPerson }) => {
  const [person, setPerson] = useState(defaultPerson);
  const { name, status } = person;

  const setStatus = useCallback(
    newStatus => {
      setPerson({
        ...person,
        status: newStatus
      });
      // Call API
    },
    [name, status]
  );

  return (
    <Grid container item xs spacing={3} justify="center" alignItems="center">
      <Grid item>
        <Paper>Name is: {name}</Paper>
        <Paper>Home status is: {status}</Paper>
      </Grid>
      <Grid item>
        <Button
          variant={status === "home" ? "contained" : "outlined"}
          color="primary"
          onClick={() => setStatus("home")}
        >
          Home
        </Button>
      </Grid>

      <Grid item>
        <Button
          variant={status === "not_home" ? "contained" : "outlined"}
          color="primary"
          onClick={() => setStatus("not_home")}
        >
          Not Home
        </Button>
      </Grid>

      <Grid item>
        <Button
          variant={status === "home_with_extra" ? "contained" : "outlined"}
          color="primary"
          onClick={() => setStatus("home_with_extra")}
        >
          Home + 1
        </Button>
      </Grid>
    </Grid>
  );
};
