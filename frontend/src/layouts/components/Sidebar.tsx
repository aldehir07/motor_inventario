import {
  Box,
  Divider,
  Drawer,
  List,
  ListItemButton,
  ListItemText,
  Typography,
} from "@mui/material";
import { NavLink } from "react-router-dom";

interface SidebarProps {
  mobileOpen: boolean;
  onMobileClose: () => void;
}

const drawerWidth = 240;

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

function SidebarContent({
  onMobileClose,
}: {
  onMobileClose?: () => void;
}) {
  return (
    <>
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
            onClick={onMobileClose}
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
    </>
  );
}

function Sidebar({
  mobileOpen,
  onMobileClose,
}: SidebarProps) {
  return (
    <>
      {/* Desktop */}
      <Box
        component="aside"
        sx={{
          display: {
            xs: "none",
            md: "block",
          },
          width: drawerWidth,
          flexShrink: 0,
        }}
      >
        <Box
          sx={{
            width: drawerWidth,
            minHeight: "100vh",
            borderRight: 1,
            borderColor: "divider",
            bgcolor: "background.paper",
          }}
        >
          <SidebarContent />
        </Box>
      </Box>

      {/* Mobile */}
      <Drawer
        variant="temporary"
        open={mobileOpen}
        onClose={onMobileClose}
        ModalProps={{
          keepMounted: true,
        }}
        sx={{
          display: {
            xs: "block",
            md: "none",
          },
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
      >
        <SidebarContent
          onMobileClose={onMobileClose}
        />
      </Drawer>
    </>
  );
}

export default Sidebar;