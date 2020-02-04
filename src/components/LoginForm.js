import React from "react";
import { Button, Grid, TextField } from "@material-ui/core";
import { Link } from "react-router-dom";

const LoginForm = () => {
  return (
    <>
      <Grid container direction="column" spacing={1} alignContent="center">
        <Grid item>
          <TextField label="Username" variant="outlined" />
        </Grid>
        <Grid item>
          <TextField label="Password" variant="outlined" />
        </Grid>
        <Grid item>
          <Grid container direction="row-reverse" alignContent="flex-end">
            <Grid item>
              <Link to="/home" style={{ textDecoration: 'none' }}>
                <Button variant="contained" color="primary">
                  Login
                </Button>
              </Link>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </>
  );
};

export default LoginForm;
