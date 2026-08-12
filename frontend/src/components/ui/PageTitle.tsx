import { Typography } from "@mui/material";

interface PageTitleProps {
  title: string;
  description?: string;
}

export function PageTitle({
  title,
  description,
}: PageTitleProps) {
  return (
    <div>
      <Typography
        variant="h4"
        component="h1"
        sx={{ fontWeight: 600 }}
        gutterBottom
      >
        {title}
      </Typography>

      {description && (
        <Typography
          variant="body1"
          color="text.secondary"
        >
          {description}
        </Typography>
      )}
    </div>
  );
}