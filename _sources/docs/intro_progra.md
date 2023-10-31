# Programación

```{epigraph}
“Se suele decir que una persona no entiende algo de verdad hasta que puede explicárselo a otro. En realidad,
no lo entiende de verdad hasta que puede explicárselo a un computador.”

-- Donald Knuth
```

Si tuvieramos que resumir el propósito de la programación en una frase, ésta debería ser:

```{epigraph}
que el computador haga el trabajo por nosotros.
```

Los computadores son buenos para hacer tareas rutinarias. Idealmente, cualquier problema tedioso y repetitivo debería ser resuelto por un computador, y los seres humanos sólo deberíamos encargarnos de los problemas realmente interesantes: los que requieren creatividad, pensamiento crítico y subjetividad.

La **programación** es el proceso de transformar un método para resolver problemas en uno que pueda ser entendido por el computador.

## Algoritmos

```{epigraph}
“La informática se trata de computadores tanto como la astronomía se trata de telescopios.”

-- Edsger Dijkstra
```

Al diseñar un programa, el desafío principal es crear y describir un procedimiento que esté completamente bien definido, que no tenga ambigüedades, y que efectivamente resuelva el problema.

Así es como la programación no es tanto sobre computadores, sino sobre resolver problemas de manera estructurada. El objeto de estudio de la programación no son los programas, sino los algoritmos.

Un **algoritmo** es un procedimiento bien definido para resolver un problema. Todo el mundo conoce y utiliza algoritmos a diario, incluso sin darse cuenta:

**a) Una receta**

Una receta de cocina es un algoritmo; si bien podríamos cuestionar que algunos pasos son ambiguos (¿cuánto es «una pizca de sal»? ¿qué significa «agregar a gusto»?), en general las instrucciones están lo suficientemente bien definidas para que uno las pueda seguir sin problemas.

La entrada de una receta son los ingredientes y algunos datos como: ¿para cuántas personas se cocinará? El proceso es la serie de pasos para manipular los ingredientes. La salida es el plato terminado.

En principio, si una receta está suficientemente bien explicada, podría permitir preparar un plato a alguien que no sepa nada de cocina.

**b) Método de multiplicar**

El método para multiplicar números a mano que aprendimos en el colegio es un algoritmo. Dado cualquier par de números enteros, si seguimos paso a paso el procedimiento siempre obtendremos el producto:

La entrada del algoritmo de multiplicación son los dos factores. El proceso es la secuencia de pasos en que los dígitos van siendo multiplicados las reservas van siendo sumadas, y los productos intermedios son finalmente sumados. La salida del algoritmo es el producto obtenido.


### Componentes de un algoritmo

Conceptualmente, un algoritmo tiene tres componentes:

* **entrada**: son los datos sobre los que el algoritmo opera;
* **proceso**: son los pasos que hay que seguir, utilizando la entrada;
* **salida**: es el resultado que entrega el algoritmo.

El proceso es una secuencia de sentencias, que debe ser realizada en orden. El proceso también puede tener ciclos (grupos de sentencias que son ejecutadas varias veces) y condicionales (grupos de sentencias que sólo son ejecutadas bajo ciertas condiciones).

### Cómo describir un algoritmo
Consideremos un ejemplo sencillo: un algoritmo para resolver ecuaciones cuadráticas.

Una ecuación cuadrática es una ecuación de la forma $ax^2+bx+c=0$, donde $a, b$ y $c$ son datos dados, con $a\neq0$, y $x$ es la incógnita cuyo valor que se desea determinar.

Por ejemplo, $2x^2−5x+2=0$ es una ecuación cuadrática con $a=2$, $b=−5$ y $c=2$. Sus soluciones son $x_1=1/2$ y $x_2=2$, como se puede comprobar fácilmente al reemplazar estos valores en la ecuación. El problema es cómo obtener estos valores en primer lugar.

El problema computacional de resolver una ecuación cuadrática puede ser planteado así:

```{epigraph}
Dados $a, b$ y $c$, entontrar los valores reales de $x$ que satisfacen $ax^2+bx+c=0$.
```

La entrada del algoritmo, pues, son los valores $a, b$ y $c$, y la salida son las raíces reales $x$ (que pueden ser cero, una o dos) de la ecuación. En un programa computacional, los valores de $a, b$ y $c$ deberían ser ingresados usando el teclado, y las soluciones $x$ deberían ser mostradas a continuación en la pantalla.

Al estudiar álgebra aprendemos un algoritmo para resolver este problema. Es lo suficientemente detallado para que pueda usarlo cualquier persona, incluso sin saber qué es una ecuación cuadrática, o para que lo pueda hacer un computador. A continuación veremos algunas maneras de describir el procedimiento.

**Lenguaje natural**

Durante el proceso mental de diseñar un algoritmo, es común pensar y describir los pasos en la misma manera en que hablamos a diario. Por ejemplo:

```{epigraph}
Teniendo los valores de $a, b$ y $c$, calcular el discriminante $D=b^2−4ac$. Si es discriminante es negativo, entonces la ecuación no tiene soluciones reales. Si es discriminante es igual a cero, entonces la ecuación tiene una única solución real, que es $x=−b/2a$. Si el discriminante es positivo, entonces la ecuación tiene dos soluciones reales, que son $x_1=(−b−\sqrt{D})/2a$ y $x_2=(−b+\sqrt{D})/2a$.
```

Esta manera de expresar un algoritmo no es ideal, ya que el lenguaje natural es:

* **impreciso**: puede tener ambigüedades;
* **no universal**: personas distintas describirán el proceso de maneras distintas; y
* **no estructurado**: la descripción no está expresada en función de componentes simples.

Aún así, es posible identificar los pasos del algoritmo. Por ejemplo, hay que evaluar la expresión $b^2−4ac$, y ponerle el nombre $D$ a su resultado. Esto se llama asignación, y es un tipo de instrucción que aparece en casi todos los algoritmos. Después de eso, el algoritmo puede usar el nombre $D$ para referirse al valor calculado.

**Diagrama de flujo**
Un diagrama de flujo es una representación gráfica de un algoritmo. Los pasos son representados por varios tipos de bloques, y el flujo de ejecución es indicado por flechas que conectan los bloques:


```{figure} https://raw.githubusercontent.com/fralfaro/python_intro/main/docs/images/flujo.png
---
scale: 50%
align: center
name: fig11
---
Diagrama de flujo
```

El inicio y el final del algoritmo son representados con bloques circulares. El algoritmo siempre debe ser capaz llegar desde uno hasta el otro, sin importar por qué camino lo hace. Un algoritmo no puede «quedarse pegado» en la mitad.

La entrada y la salida de datos son representadas con romboides, que en la figura de arriba están pintados de verde.

Los diamantes representan condiciones en las que el algoritmo sigue uno de dos caminos. que están etiquetados con sí o no, dependiendo si la condición es verdadera o falsa.

También puede haber ciclos, representados por flechas que regresan a bloques anteriores. En este ejemplo, no hay ciclos.

Otras sentencias van dentro de rectángulos, que en la figura están pintados de azul. En este ejemplo, las sentencias son asignaciones, representadas en la forma `nombre = valor`.

Los diagramas de flujo no son usados en la práctica para programar, pero son útiles para ilustrar cómo funcionan algoritmos sencillos.

**Pseudocódigo**

El pseudocódigo es una descripción estructurada de un algoritmo basada en ciertas convenciones notacionales. Si bien es muy parecido al código que finalmente se escribirá en el computador, el pseudocódigo está pensado para ser leído por humanos.

Una manera de escribir el algoritmo para la ecuación cuadrática en pseudocódigo es la siguiente:

```{epigraph}
leer a
leer b
leer c

discriminante = b² - 4ac

si discriminante < 0:
    escribir 'La ecuación no tiene soluciones reales'

o si no, si discriminante = 0:
    x = -b / 2a
    escribir 'La solución única es', x

o si no:
    x1 = (-b - √discriminante) / 2a
    x2 = (-b + √discriminante) / 2a
    escribir 'Las dos soluciones reales son:'
    escribir x1
    escribir x2
```

Las líneas que comienzan con `leer` y `escribir` denotan, respectivamente, la entrada y la salida del programa. Los diferentes casos son representados usando sentencias `si` y o `si no`. Las asignaciones siguen la misma notación que en el caso de los diagramas de flujo.

La notación de pseudocódigo es bien liberal. Uno puede mezclar notación de matemáticas con frases en español, siempre que quede absolutamente claro para el lector qué representa cada una de las líneas del algoritmo.

**Código**

El producto final de la programación siempre debe ser código que pueda ser ejecutado en el computador. Esto requiere describir los algoritmos en un lenguaje de programación. Los lenguajes de programación definen un conjunto limitado de conceptos básicos, en función de los cuales uno puede expresar cualquier algoritmo.

En esta asignatura, usaremos el lenguaje de programación [Python](https://www.python.org/) para escribir nuestros programas.

El código en Python para resolver la ecuación cuadrática es el siguiente:

```python
a = float(raw_input('Ingrese a: '))
b = float(raw_input('Ingrese b: '))
c = float(raw_input('Ingrese c: '))

discriminante = b ** 2 - 4 * a * c
if discriminante < 0:
    print 'La ecuacion no tiene soluciones reales'
elif discriminante == 0:
    x = -b / (2 * a)
    print 'La solucion unica es x =', x
else:
    x1 = (-b - (discriminante ** 0.5)) / (2 * a)
    x2 = (-b + (discriminante ** 0.5)) / (2 * a)
    print 'Las dos soluciones reales son:'
    print 'x1 =', x1
    print 'x2 =', x2

raw_input()
```

A partir de ahora, usted aprenderá a entender, escribir y ejecutar códigos como éste.

## Referencias

* [Programación - USM](http://progra.usm.cl/apunte/materia/index.html)
