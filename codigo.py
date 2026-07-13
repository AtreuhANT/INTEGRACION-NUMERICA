import sys
from typing import List, Tuple

class NumericalIntegration:
    """
    Clase utilitaria para métodos de integración numérica.
    Diseñada para procesar datos de sensores (volumen y presión) y calcular 
    el trabajo termodinámico mediante cuadraturas de Newton-Cotes.
    """

    @staticmethod
    def trapezoidal_rule(x: List[float], y: List[float]) -> float:
        """
        Calcula la integral usando la Regla del Trapecio Compuesta.
        """
        try:
            if len(x) != len(y) or len(x) < 2:
                raise ValueError("Los arrays 'x' e 'y' deben tener la misma longitud y al menos 2 elementos.")
            
            n = len(x) - 1
            h = (x[-1] - x[0]) / n
            
            integral = y[0] + y[-1]
            for i in range(1, n):
                integral += 2 * y[i]
                
            return (h / 2) * integral
            
        except Exception as e:
            print(f"[Error Crítico en trapezoidal_rule]: {str(e)}")
            sys.exit(1)

    @staticmethod
    def simpson_13_rule(x: List[float], y: List[float]) -> float:
        """
        Calcula la integral usando la Regla de Simpson 1/3 Compuesta.
        Requiere un número par de subintervalos (n).
        """
        try:
            n = len(x) - 1
            if len(x) != len(y):
                raise ValueError("Los arrays 'x' e 'y' deben tener la misma longitud.")
            if n % 2 != 0:
                raise ValueError("La regla de Simpson 1/3 requiere un número par de subintervalos (n).")
                
            h = (x[-1] - x[0]) / n
            
            integral = y[0] + y[-1]
            for i in range(1, n):
                if i % 2 == 0:
                    integral += 2 * y[i]
                else:
                    integral += 4 * y[i]
                    
            return (h / 3) * integral
            
        except Exception as e:
            print(f"[Error Crítico en simpson_13_rule]: {str(e)}")
            sys.exit(1)

    @staticmethod
    def simpson_38_rule(x: List[float], y: List[float]) -> float:
        """
        Calcula la integral usando la Regla de Simpson 3/8 Compuesta.
        Requiere que el número de subintervalos (n) sea múltiplo de 3.
        """
        try:
            n = len(x) - 1
            if len(x) != len(y):
                raise ValueError("Los arrays 'x' e 'y' deben tener la misma longitud.")
            if n % 3 != 0:
                raise ValueError("La regla de Simpson 3/8 requiere que 'n' sea múltiplo de 3.")
                
            h = (x[-1] - x[0]) / n
            
            integral = y[0] + y[-1]
            for i in range(1, n):
                if i % 3 == 0:
                    integral += 2 * y[i]
                else:
                    integral += 3 * y[i]
                    
            return (3 * h / 8) * integral
            
        except Exception as e:
            print(f"[Error Crítico en simpson_38_rule]: {str(e)}")
            sys.exit(1)

def print_formal_table(results: List[Tuple[str, float, float]]) -> None:
    """
    Imprime los resultados en el formato tabular formal solicitado.
    """
    try:
        print("\n" + "="*65)
        print(f"{'MÉTODO':<18} | {'VALOR APROXIMADO':<18} | {'ERROR RELATIVO %':<18}")
        print("-" * 65)
        
        for method, value, error in results:
            if error is None:
                error_str = "0.0000 % (Ref)"
            else:
                error_str = f"{error:.4f} %"
                
            print(f"{method:<18} | {value:<18.4f} | {error_str:<18}")
        
        print("="*65 + "\n")
    except Exception as e:
        print(f"[Error al imprimir tabla]: {str(e)}")

def main():
    # 1. Ingesta de datos del problema
    try:
        V = [1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4]
        P = [300.2, 242.1, 201.5, 169.8, 151, 134.3, 120.8, 107.9, 99.1, 93.4, 86.2, 79.5, 75.1]
    except Exception as e:
        print(f"Error en la inicialización de los datos: {e}")
        sys.exit(1)

    # 2. Ejecución de las integrales numéricas
    val_trapezoid = NumericalIntegration.trapezoidal_rule(V, P)
    val_simp_13 = NumericalIntegration.simpson_13_rule(V, P)
    val_simp_38 = NumericalIntegration.simpson_38_rule(V, P)

    # 3. Cálculo de Error Relativo 
    # Decisión Arquitectónica: Usaremos Simpson 1/3 como valor de referencia 
    # al carecer de una función analítica exacta para W.
    exact_ref = val_simp_13
    
    def calc_rel_error(approx_val: float, true_val: float) -> float:
        return abs((true_val - approx_val) / true_val) * 100

    err_trapezoid = calc_rel_error(val_trapezoid, exact_ref)
    err_simp_38 = calc_rel_error(val_simp_38, exact_ref)

    # 4. Formateo de Resultados
    results_data = [
        ("Trapecio", val_trapezoid, err_trapezoid),
        ("Simpson 1/3", val_simp_13, None), # Referencia
        ("Simpson 3/8", val_simp_38, err_simp_38)
    ]

    print_formal_table(results_data)

if __name__ == "__main__":
    main()
