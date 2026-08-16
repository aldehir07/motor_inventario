import { useState } from "react";
import { Box } from "@mui/material";
import { Outlet } from "react-router-dom";

import Header from "./components/Header";
import Sidebar from "./components/Sidebar";

function MainLayout() {
  const [mobileOpen, setMobileOpen] =
    useState(false);

  const handleMobileMenuOpen = () => {
    setMobileOpen(true);
  };

  const handleMobileMenuClose = () => {
    setMobileOpen(false);
  };

  return (
    <Box
      sx={{
        display: "flex",
        minHeight: "100vh",
        bgcolor: "background.default",
      }}
    >
      <Sidebar
        mobileOpen={mobileOpen}
        onMobileClose={handleMobileMenuClose}
      />

      <Box
        sx={{
          flexGrow: 1,
          display: "flex",
          flexDirection: "column",
          minWidth: 0,
        }}
      >
        <Header
          onMenuClick={handleMobileMenuOpen}
        />

        <Box
          component="main"
          sx={{
            flexGrow: 1,
            p: {
              xs: 2,
              sm: 3,
            },
          }}
        >
          <Outlet />
        </Box>
      </Box>
    </Box>
  );
}

export default MainLayout;