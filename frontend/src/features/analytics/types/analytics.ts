export interface DashboardResumen {
    productos: number;
    productos_activos: number;
    stock_bajo: number;
    sin_stock: number;
    valor_inventario: number;
    compras: number;
    ventas: number;
}

export interface VentaPorMes {
    anio: number;
    mes: number;
    total: number;
}

export interface CompraPorMes {
    anio: number;
    mes: number;
    total: number;
}

export interface RotacionInventario {
  producto_id: number;
  codigo: string;
  nombre: string;
  stock_actual: number;
  vendidos: number;
  rotacion: number;
}

export interface ABCProducto {
  producto_id: number;
  codigo: string;
  nombre: string;
  valor: number;
  clasificacion: string;
}