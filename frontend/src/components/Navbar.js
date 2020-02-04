import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  IconButton,
  Grid
} from "@material-ui/core";
import Menu from "@material-ui/icons/Menu";
import { Link } from "react-router-dom";

const useStyles = makeStyles(theme => ({
  root: {
    // flexGrow: 1
  },
  menuButton: {
    marginRight: theme.spacing(2)
  },
  title: {
    flexGrow: 1
  }
}));

const Navbar = () => {
  const classes = useStyles();

  return (
    <Grid item className={classes.root} >
      <AppBar position="static">
        <Toolbar>
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            className={classes.menuButton}
          >
            <Menu />
          </IconButton>
          <Typography variant="h6" className={classes.title}>
            Who's Home
          </Typography>
          <Link color="inherit" to="/login" style={{ textDecoration: 'none' }}>
            <Button color='secondary' >Login</Button>
          </Link>
        </Toolbar>
      </AppBar>
    </Grid>
  );
};

export default Navbar;
