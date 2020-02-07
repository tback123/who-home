import React from "react";
import { Grid } from "@material-ui/core";
import Navbar from "../components/Navbar";
import PersonStatuses from "../components/PersonStatuses";
import people from "../data/people";

const MainPage = () => {
  return (
    <>
      <Grid
        container
        direction="column"
        justify="flex-start"
        spacing={0}
        style={{ overflowX: "hidden", overflowY: "hidden" }}
      >
        <Navbar />
        <PersonStatuses people={people} />
      </Grid>
    </>
  );
};

export default MainPage;
