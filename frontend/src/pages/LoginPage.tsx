import { useState, type FormEvent } from "react";

import {
  Alert,
  Box,
  Button,
  CircularProgress,
  TextField,
  Typography,
} from "@mui/material";
import { AxiosError } from "axios";
import { useNavigate } from "react-router-dom";

import { useAuth } from "../features/auth/hooks/useAuth";
import type { ApiError } from "../types/api";

function LoginPage() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [enviando, setEnviando] = useState(false);

  async function handleSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    setEnviando(true);
    setError(null);

    try {
      await login({ email, password });
      navigate("/");
    } catch (err) {
      setError(extraerMensajeError(err));
    } finally {
      setEnviando(false);
    }
  }

  return (
    <Box
      sx={{
        maxWidth: 400,
        mx: "auto",
        mt: 8,
        p: 3,
      }}
    >
      <Typography variant="h4" gutterBottom>
        Iniciar sesión
      </Typography>

      <Typography color="text.secondary" sx={{ mb: 3 }}>
        Acceso al sistema.
      </Typography>

      <Box component="form" onSubmit={handleSubmit}>
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        <TextField
          label="Email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          fullWidth
          margin="normal"
          required
          autoFocus
        />

        <TextField
          label="Contraseña"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          fullWidth
          margin="normal"
          required
        />

        <Button
          type="submit"
          variant="contained"
          fullWidth
          sx={{ mt: 2 }}
          disabled={enviando}
        >
          {enviando ? (
            <CircularProgress size={24} />
          ) : (
            "Ingresar"
          )}
        </Button>
      </Box>
    </Box>
  );
}

function extraerMensajeError(err: unknown): string {
  if (err instanceof AxiosError) {
    const data = err.response?.data as ApiError | undefined;

    if (data?.message) {
      return data.message;
    }
  }

  return "No se pudo iniciar sesión.";
}

export default LoginPage;