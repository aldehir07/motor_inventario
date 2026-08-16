import {
  AppBar,
  IconButton,
  Toolbar,
  Typography,
} from "@mui/material";

import MenuIcon from "@mui/icons-material/Menu";
import { useLocation } from "react-router-dom";

interface HeaderProps {
  onMenuClick: () => void;
}

const pageTitles: Record<string, string> = {
  "/": "Dashboard",
  "/productos": "Productos",
  "/inventario": "Inventario",
  "/compras": "Compras",
  "/ventas": "Ventas",
  "/analytics": "Analytics",
  "/ml": "Machine Learning",
};

function Header({
  onMenuClick,
}: HeaderProps) {
  const location = useLocation();

  const title =
    pageTitles[location.pathname] ??
    "Motor Inteligente";

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
        <IconButton
          edge="start"
          color="inherit"
          aria-label="abrir menú"
          onClick={onMenuClick}
          sx={{
            mr: 2,
            display: {
              xs: "inline-flex",
              md: "none",
            },
          }}
        >
          <MenuIcon />
        </IconButton>

        <Typography
          variant="h6"
          sx={{
            fontWeight: "bold",
          }}
        >
          {title}
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Header;