# Coffee Machine Project

## Objetivo

Implementar un simulador de mAquina de cafE funcional en Python que gestione recursos, procese transacciones y permita operaciones administrativas. El proyecto demuestra programación orientada a procedimientos con validaciOn de datos, gestión de estados y manejo de errores.

## Requerimientos

### Técnicos
- Python 3.x
- Módulos: `random`, `sys`, `io`, `unittest.mock`
- No requiere dependencias externas

### Funcionales
- Gestión de recursos: agua, leche, granos, vasos
- Menú de café: espresso ($4), latte ($7), cappuccino ($6)
- Sistema de pagos con cambio automático
- Operaciones administrativas con contraseña
- Validación de entrada y manejo de errores
- LImites maximos de recursos

## Estructura del Proyecto

```
Coffee-Machine/
-> main.py                      # Interfaz de usuario y menú principal
-> coffee_machine.py            # Lógica central de la máquina
-> machine_operations.py        # Operaciones auxiliares y validación
-> test_coffee_machine.py       # Tests fijos predefinidos
-> test_random_coffee_machine.py # Tests aleatorios variables
-> README.md                    # Documentación
```

## Funcionalidades

1. **Visualizar estado** - Recursos disponibles y dinero
2. **Rellenar máquina** - Añadir recursos con validación de límites
3. **Comprar café** - Selección, pago y preparación automática
4. **Depositar dinero** - Función administrativa
5. **Retirar dinero** - Con contraseña y opción de caridad
6. **Validación completa** - Recursos suficientes y pagos válidos

## Uso

### Ejecución Principal
```bash
python main.py
```

### Tests Aleatorios
```bash
python test_random_coffee_machine.py
```

## Ejemplo de Ejecución de Tests Aleatorios

### 6 Casos de Uso Ejecutados:

**Caso 1: Rellenar MAquina**
- Estado inicial: 87g beans, 2 cups, 856ml water, 332ml milk
- Inputs aleatorios: +24g beans, +636ml water, +407ml milk, +8 cups
- Resultado: 111g beans, 10 cups, 1492ml water, 739ml milk

**Caso 2: Compra Exitosa**
- Selección aleatoria: Cappuccino ($6)
- Pago: $6 (exacto)
- Resultado: Café entregado, recursos descontados, +$6 en máquina

**Caso 3: Recursos Insuficientes**
- Estado crítico: 28g beans, 0 cups, 139ml water, 127ml milk
- Intento: Latte (requiere 350ml water, 20g beans)
- Resultado: "One, or more, ingredients are missing" - sin cambios

**Caso 4: Pago Insuficiente**
- Selección: Cappuccino ($6)
- Pago insuficiente: $2
- Resultado: "Insufficient payment. Money returned" - sin cambios

**Caso 5: Operaciones Admin**
- Estado inicial: $57
- DepOsito aleatorio: +$48 = $105 total
- Retiro aleatorio: $12 a caridad
- Resultado: $93 final

**Caso 6: Estado Aleatorio**
- GeneraciOn aleatoria: 124g beans, 2 cups, 1203ml water, 777ml milk, $74
- Muestra variabilidad en condiciones iniciales

## CaracterIsticas TEcnicas

- **ValidaciOn robusta** de entradas numEricas
- **GestiOn de estados** consistente
- **LImites mAximos** respetados automAticamente
- **Manejo de errores** sin crashes
- **Tests exhaustivos** con casos edge
- **Aleatoriedad real** usando timestamps

## ContraseNa Administrativa

Password por defecto: `1234`