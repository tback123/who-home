import React from "react";
import { Container, Typography, Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

import LoginForm from "../components/LoginForm";

const useStyles = makeStyles(theme => ({
  alignItemsAndJustifyContent: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
  },
  titlePane: {
    display: "flex",
    alignItems: "center",
  }
}));

const LoginPage = () => {

  const classes = useStyles();

  return (
    <Container className={classes.alignItemsAndJustifyContent}>
      <Grid container direction="column" alignContent="center" spacing={1}>

        <Grid item className={classes.titlePane}>
          <Typography variant="h4" gutterBottom color="primary">Who's Home</Typography>
        </Grid>

        <Grid item>
            <LoginForm/>
        </Grid>

      </Grid>
    </Container>
  );
};

export default LoginPage;
