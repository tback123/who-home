import { createMuiTheme } from "@material-ui/core/styles";
import {
  indigo,
  yellow
} from "@material-ui/core/colors"

export default createMuiTheme({
  palette: {
    primary: indigo,
    secondary: yellow,
  },
  typography: {
    fontFamily: [
      "-apple-system",
      "BlinkMacSystemFont",
      '"Segoe UI"',
      "Roboto",
      '"Helvetica Neue"',
      "Arial",
      "sans-serif",
      '"Apple Color Emoji"',
      '"Segoe UI Emoji"',
      '"Segoe UI Symbol"'
    ].join(",")
  },
});
