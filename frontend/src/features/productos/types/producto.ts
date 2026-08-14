export interface Producto {
  id: number;
  codigo: string;
  sku: string;
  nombre: string;
  descripcion: string | null;
  precio_compra_actual: number;
  precio_venta_actual: number;
  stock_minimo: number;
  stock_maximo: number;
  activo: boolean;
}