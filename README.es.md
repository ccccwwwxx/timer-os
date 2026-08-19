<!-- i18n-version: 2026-08-19.1 -->
# Timer OS · 时代系统

**Idiomas:** [English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · Español

> El pasado puede recuperarse. El presente puede percibirse. El futuro puede programarse.

**Timer OS (时代系统)** es un sistema operativo experimental centrado en **tiempo, atención, contexto, cognición y acción**, en lugar de aplicaciones y archivos.

El nombre 时代系统 no se refiere solo a medir el tiempo. Describe un sistema capaz de organizar la historia, comprender el estado presente y programar la cognición y la acción futuras a lo largo de un flujo temporal continuo.

El proyecto parte de una premisa simple: si el espacio físico es un recurso escaso, entonces **la atención humana es el recurso escaso del tiempo**. Por ello, una IA personal útil debe hacer más que responder preguntas. Debe comprender contexto de forma continua, conservar historia valiosa, mantener estado cognitivo y decidir cuándo la atención humana es realmente necesaria.

Timer OS no está limitado a humanos. La misma arquitectura puede dar soporte a agentes corporizados y robots de larga duración que necesiten percepción continua, conciencia de posición, mantenimiento de un modelo de sí mismos, planificación cognitiva y planificación de acciones.

## Arquitectura

Timer OS se organiza en cuatro capas conceptuales:

- **Body** — la interfaz física con el mundo real. Para humanos, la primera referencia es un auricular separado junto con un estuche de carga inteligente. En robots corporizados, Body puede incluir cámaras, micrófonos, IMU, sistemas de posicionamiento, sensores de fuerza/par, codificadores articulares, motores y otras interfaces físicas de entrada/salida.
- **External Brain** — subsistema cognitivo y de memoria que transforma experiencia continua en contexto utilizable.
- **YIdui** — subsistema cognitivo central dentro del External Brain, responsable de mantener conocimiento, estado cognitivo y actualizaciones del self-model respaldadas por evidencia a lo largo del tiempo.
- **Timer OS Scheduler** — coordina tiempo, atención, cognición y acciones basándose en historia, estado actual e intención futura.

El teléfono se trata deliberadamente como una **superficie de visualización y control**, no como el centro del sistema.

```text
Mundo real
   ↓
Body (percepción / posición / ejecución edge / buffer / conectividad)
   ↓
Timer Event Stream
   ↓
External Brain
   └── YIdui (estado cognitivo / memoria / actualización del self-model)
   ↓
Timer Scheduler
   ↓
Acciones / asignación futura de atención o movimiento
```

## Planificación cognitiva

A medida que el manejo de contexto por parte de los modelos se convierte en infraestructura, Timer OS trata la **planificación cognitiva** como un problema de sistema de nivel superior:

- qué debe percibirse con alta frecuencia;
- qué historia debe recuperarse ahora;
- qué modelo o profundidad de razonamiento utilizar;
- cuándo los conflictos cognitivos o de política deben provocar una reevaluación;
- cuándo ejecutar una acción;
- cuándo está justificado interrumpir a una persona;
- en sistemas corporizados, qué cambios de sensores, posición o estado del motor deben tener prioridad sobre el plan actual.

Esto separa el control físico en tiempo real de la evolución cognitiva más lenta. Los bucles de control críticos para la seguridad permanecen deterministas y acotados, mientras que las estrategias de nivel superior pueden evaluarse, compararse y actualizarse con el tiempo.

## Conciencia de posición

En sistemas corporizados, la posición es un flujo de estado continuo, no una única coordenada GPS. Timer OS puede combinar posición global, posicionamiento interior/local, postura y orientación corporal, posición de articulaciones o extremidades, posición relativa respecto a personas y objetos, trayectoria de movimiento y confianza en la estimación actual.

De este modo, la posición histórica, la postura presente y el destino previsto pueden participar en la planificación cognitiva y de acciones futuras.

## Self-model corporizado

Para agentes corporizados, Timer OS explora un **self-model** persistente que no se configura una sola vez por humanos, sino que puede revisarse continuamente a partir de evidencia del mundo real.

Un self-model puede incluir:

- estructura corporal y estado físico actual;
- límites de capacidad calibrados y observados;
- competencias aprendidas y modos de fallo;
- versiones activas de modelo o estrategia;
- incertidumbre sobre lo que el agente puede o no hacer de forma segura.

Las observaciones nuevas no deberían sobrescribir inmediatamente las creencias anteriores. Modelos o estrategias competidoras pueden coexistir, acumular evidencia, ser probados y finalmente conservarse, sustituirse o condicionarse a distintos entornos.

## Primer principio de producto: entrada antes que interrupción

Timer OS comienza resolviendo un problema unidireccional:

**Realidad → Body → cognición en la nube → flujo temporal persistente**

El primer objetivo no es construir un asistente que hable constantemente. Es construir un sistema capaz de reconstruir de forma fiable las partes de mayor valor del día de una persona con una interacción mínima.

Solo después de demostrar la fiabilidad de la entrada debe Timer OS decidir **si interrumpir, cuándo hacerlo y de qué manera**.

El mismo orden se aplica a sistemas corporizados: primero captura y reconstrucción fiable del estado; después, activación progresiva de planificación autónoma de nivel superior y estrategias autoactualizables.

## Qué se publica en este repositorio

Este repositorio contiene intencionadamente solo el **esqueleto público** de Timer OS:

- vocabulario y límites de arquitectura;
- contrato mínimo de eventos para un flujo temporal continuo;
- interfaces abstractas para Body, Brain, Scheduler y proveedores de modelos;
- una interfaz de referencia para DeepSeek;
- conceptos de alto nivel sobre agentes corporizados, conciencia de posición y self-model;
- ejemplos mínimos de conexión entre componentes.

El objetivo es hacer que la arquitectura pueda debatirse e interoperar sin exponer implementaciones propietarias.

## Qué NO es open source

Los siguientes componentes permanecen deliberadamente privados:

- diseño de hardware y firmware de Body;
- enrutamiento de audio y cadena de grabación continua;
- implementación de reconocimiento de hablante/huella vocal;
- algoritmos de fusión de posición y localización;
- planificación en tiempo real de sensores y motores;
- lógica de decisión edge y estrategia de buffer local;
- algoritmos de actualización de estado cognitivo y self-model de YIdui;
- mecanismos de conflicto y actualización de conocimiento, modelos y políticas;
- lógica de evolución y validación de estrategias;
- estrategia de planificación de atención/interrupciones;
- orquestación de nube de producción, prompts, scoring y lógica de políticas;
- conjuntos de datos propietarios, datos de usuario y datos de evaluación.

Las interfaces públicas pueden describir cómo se conectan estos componentes, pero no cómo funcionan internamente.

## DeepSeek

El esqueleto público es neutral respecto al proveedor de modelos. `DeepSeek` se incluye como primer proveedor/etiqueta de referencia para experimentos de razonamiento en la nube.

No se almacenan API Keys en este repositorio. El módulo público solo define la interfaz y el límite de ejemplo.

GitHub Topics sugeridos:

`timer-os` `external-brain` `personal-ai` `agent` `deepseek` `edge-ai` `wearable-ai` `embodied-ai` `robotics` `context-engineering`

## Estado

El proyecto se encuentra en una fase temprana de arquitectura / esqueleto. Las interfaces pueden cambiar.

## Mantenimiento sincronizado de idiomas

Las cinco versiones lingüísticas comparten un único número de versión documental. Cada cambio público de arquitectura debe actualizar las cinco versiones y aumentar la versión de `docs/i18n/version.txt`. CI comprueba la coherencia de versiones para evitar que las traducciones diverjan silenciosamente.

## Contribuciones

Se aceptan contribuciones a interfaces públicas, contratos de eventos, documentación, experimentos de interoperabilidad y adaptadores no propietarios. Las implementaciones privadas de los subsistemas centrales quedan fuera del alcance de este repositorio público.

## Licencia

MIT License. Consulte [LICENSE](LICENSE).
