import { Box, Button, Card, CardContent, Stack } from "@mui/material";

import { PageTitle } from "./components/ui/PageTitle";

function App() {
  return (
    <Box sx={{ p: 4 }}>
      <Stack spacing={3}>
        <PageTitle
          title="Motor Inteligente para Inventarios"
          description="Sistema de gestión, análisis y predicción de inventario."
        />

        <Card>
          <CardContent>
            <PageTitle
              title="Sistema funcionando"
              description="Material UI está correctamente configurado."
            />

            <Box sx={{ mt: 3 }}>
              <Button variant="contained">
                Continuar
              </Button>
            </Box>
          </CardContent>
        </Card>
      </Stack>
    </Box>
  );
}

export default App;