import React from "react";
import { Grid } from "@material-ui/core";
import Navbar from "../components/Navbar";
import SetStatus from "../components/SetStatus";

const MainPage = () => {
  return (
    <>
      <Grid
        container
        direction="column"
        justify="flex-start"
        spacing={0}
        style={{overflowX: "hidden", overflowY: "hidden"}}
      >
          <Navbar />
          <SetStatus />
      </Grid>
    </>
  );
};

export default MainPage;
