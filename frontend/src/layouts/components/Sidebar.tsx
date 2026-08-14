import {
  Box,
  Divider,
  List,
  ListItemButton,
  ListItemText,
  Typography,
} from "@mui/material";
import { NavLink } from "react-router-dom";

const menuItems = [
  {
    label: "Dashboard",
    path: "/",
  },
  {
    label: "Productos",
    path: "/productos",
  },
  {
    label: "Inventario",
    path: "/inventario",
  },
  {
    label: "Compras",
    path: "/compras",
  },
  {
    label: "Ventas",
    path: "/ventas",
  },
  {
    label: "Analytics",
    path: "/analytics",
  },
  {
    label: "Machine Learning",
    path: "/ml",
  },
];

function Sidebar() {
  return (
    <Box
      component="aside"
      sx={{
        width: 240,
        flexShrink: 0,
        borderRight: 1,
        borderColor: "divider",
        bgcolor: "background.paper",
      }}
    >
      <Box sx={{ p: 2 }}>
        <Typography
          variant="h6"
            sx={{ fontWeight: "bold" }}
        >
          Motor Inteligente
        </Typography>

        <Typography
          variant="body2"
          color="text.secondary"
        >
          Inventarios
        </Typography>
      </Box>

      <Divider />

      <List>
        {menuItems.map((item) => (
          <ListItemButton
            key={item.path}
            component={NavLink}
            to={item.path}
            sx={{
              "&.active": {
                backgroundColor: "action.selected",
                color: "primary.main",
                fontWeight: 600,
              },
            }}
          >
            <ListItemText primary={item.label} />
          </ListItemButton>
        ))}
      </List>
    </Box>
  );
}

export default Sidebar;