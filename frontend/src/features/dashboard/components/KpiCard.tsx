import {
  Card,
  CardContent,
  Typography,
  Box,
} from "@mui/material";
import type { ReactNode } from "react";

interface KpiCardProps {
  title: string;
  value: string | number;
  description?: string;
  icon?: ReactNode;
}

function KpiCard({
  title,
  value,
  description,
  icon,
}: KpiCardProps) {
  return (
    <Card
      elevation={0}
      sx={{
        height: "100%",
        border: 1,
        borderColor: "divider",
        borderRadius: 2,
      }}
    >
      <CardContent>
        <Box
          sx={{
            display: "flex",
            alignItems: "flex-start",
            justifyContent: "space-between",
            mb: 2,
          }}
        >
          <Typography
            variant="body2"
            color="text.secondary"
            sx= {{fontWeight:"500"}}
          >
            {title}
          </Typography>

          {icon && (
            <Box
              sx={{
                color: "primary.main",
                display: "flex",
              }}
            >
              {icon}
            </Box>
          )}
        </Box>

        <Typography
          variant="h4"
          sx= {{fontWeight:"700"}}
        >
          {value}
        </Typography>

        {description && (
          <Typography
            variant="body2"
            color="text.secondary"
            sx={{ mt: 1 }}
          >
            {description}
          </Typography>
        )}
      </CardContent>
    </Card>
  );
}

export default KpiCard;