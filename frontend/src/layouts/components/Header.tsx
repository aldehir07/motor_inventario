import {
  AppBar,
  Toolbar,
  Typography,
} from "@mui/material";

function Header() {
  return (
    <AppBar
      position="static"
      color="inherit"
      elevation={0}
      sx={{
        borderBottom: 1,
        borderColor: "divider",
      }}
    >
      <Toolbar>
        <Typography
          variant="h6"
          sx= {{ fontWeight:"bold" }}
        >
          Dashboard
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Header;