# 🍃 Té Matcha Ceremony - Landing Page Premium

Una landing page de alto impacto diseñada para la venta de Té Matcha de grado ceremonial, optimizada para conversión y con una estética minimalista y profesional.

## ✨ Características Principales

- 🎨 **Diseño Premium**: Paleta de colores unificada (#4A6741) y tipografía elegante.
- 📱 **100% Responsivo**: Adaptado para móviles, tablets y escritorio.
- 🍵 **Sección de Recetas**: Galería interactiva con modal (lightbox) para ver preparaciones.
- 💬 **Integración con WhatsApp**: Botón flotante y botones de llamada a la acción (CTA) vinculados directamente para pedidos.
- ⚡ **Performance**: Construido con React + Vite para una carga instantánea.
- 🌊 **Transiciones Suaves**: Divisor de onda (SVG) y animaciones sutiles con Framer Motion.

## 🚀 Guía de Despliegue (Production)

Esta aplicación es estática, lo que permite desplegarla gratis en minutos.

### Opción 1: Vercel (Recomendado)

1. Crea una cuenta en [Vercel](https://vercel.com/).
2. Haz clic en **"Add New"** > **"Project"**.
3. Importa tu repositorio `te_matcha` desde GitHub.
4. En **Framework Preset**, selecciona **Vite**.
5. Haz clic en **"Deploy"**.
   - *Vercel detectará automáticamente `npm run build` y la carpeta `dist`.*

### Opción 2: Netlify

1. Ve a [Netlify](https://www.netlify.com/).
2. Haz clic en **"Add new site"** > **"Import an existing project"**.
3. Conecta tu GitHub y elige el repositorio.
4. Asegúrate que el **Build command** sea `npm run build` y el **Publish directory** sea `dist`.
5. Haz clic en **"Deploy site"**.

### Opción 3: Despliegue Manual (Build)

Si prefieres subir los archivos manualmente por FTP o a otro hosting:

```bash
# 1. Instalar dependencias
npm install

# 2. Generar carpeta de producción
npm run build
```

Esto generará una carpeta **/dist** con archivos HTML, CSS y JS optimizados lista para ser subida a cualquier servidor web.

## 🛠️ Configuración Local

Si deseas trabajar en el proyecto localmente:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/yeiconcr1/te_matcha.git
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Inicia el servidor de desarrollo:
   ```bash
   npm run dev
   ```

## ✒️ Créditos

Proyecto desarrollado por [yeiconcr1](https://github.com/yeiconcr1). Calidad Ceremonial Garantizada.
