# FilterCam - Monitor de Câmera IP em Tempo Real

Uma aplicação web moderna e elegante para monitoramento de câmeras IP em tempo real com filtros avançados, interface minimalista inspirada no Notion e arquitetura preparada para integrações futuras com Inteligência Artificial.

## 🎯 Características

- **Stream em Tempo Real**: Detecção automática de endpoints de câmeras IP
- **Canvas HTML5**: Renderização de vídeo sem bibliotecas externas
- **Filtros Avançados**: 15+ filtros de processamento de imagem em tempo real
- **Controles Intuitivos**: Zoom, pan, rotação, snapshot, modo tela cheia
- **Interface Responsiva**: Suporte completo para desktop, tablet e mobile
- **Modo Claro/Escuro**: Tema nativo com variáveis CSS
- **Painel de Informações**: Dados em tempo real da câmera e stream
- **Arquitetura Modular**: SOLID, Clean Code, ES6 Modules
- **Pronta para IA**: Estrutura preparada para futuras integrações com YOLO, OCR, Face Detection

## 📋 Pré-requisitos

- Python 3.12+
- pip
- Navegador moderno (Chrome, Firefox, Safari, Edge)
- Câmera IP acessível na rede local

## 🚀 Instalação e Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/luizniz/filter_cam.git
cd filter_cam
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

```bash
cp .env.example .env
# Editar .env com o endereço IP da câmera
```

### 5. Executar a aplicação

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📁 Estrutura do Projeto

```
filter_cam/
├── app.py                          # Ponto de entrada da aplicação
├── config.py                       # Configurações da aplicação
├── requirements.txt                # Dependências Python
├── .env.example                    # Exemplo de variáveis de ambiente
│
├── app/                            # Módulo principal da aplicação
│   ├── __init__.py
│   ├── models/                     # Camada de dados
│   │   ├── __init__.py
│   │   ├── camera.py              # Modelo da câmera
│   │   └── stream.py              # Gerenciador do stream
│   │
│   ├── services/                   # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── camera_service.py      # Serviço de câmera
│   │   └── stream_service.py      # Serviço de stream
│   │
│   ├── routes/                     # Blueprints Flask
│   │   ├── __init__.py
│   │   ├── camera_routes.py       # Rotas de câmera
│   │   └── api_routes.py          # Rotas de API
│   │
│   ├── utils/                      # Utilitários
│   │   ├── __init__.py
│   │   ├── logger.py              # Sistema de logs
│   │   ├── validators.py          # Validadores
│   │   └── decorators.py          # Decoradores customizados
│   │
│   └── templates/                  # Templates HTML
│       ├── index.html             # Página principal
│       └── base.html              # Template base
│
├── static/                         # Arquivos estáticos
│   ├── css/                        # Estilos CSS
│   │   ├── main.css               # Estilos principais
│   │   ├── theme.css              # Sistema de temas
│   │   ├── canvas.css             # Estilos do canvas
│   │   ├── sidebar.css            # Estilos da barra lateral
│   │   └── responsive.css         # Estilos responsivos
│   │
│   └── js/                         # JavaScript modular
│       ├── main.js                # Ponto de entrada
│       ├── app.js                 # Aplicação principal
│       │
│       ├── modules/               # Módulos principais
│       │   ├── camera.js          # Gerenciador de câmera
│       │   ├── canvas.js          # Renderizador de canvas
│       │   ├── controls.js        # Controles da interface
│       │   ├── sidebar.js         # Barra lateral
│       │   └── api.js             # Cliente de API
│       │
│       ├── filters/               # Sistema de filtros
│       │   ├── filterManager.js   # Gerenciador de filtros
│       │   ├── baseFilter.js      # Classe base de filtros
│       │   ├── grayscale.js       # Filtro escala de cinza
│       │   ├── negative.js        # Filtro negativo
│       │   ├── brightness.js      # Filtro brilho
│       │   ├── contrast.js        # Filtro contraste
│       │   ├── sharpen.js         # Filtro nitidez
│       │   ├── blur.js            # Filtro desfoque Gaussian
│       │   ├── emboss.js          # Filtro relevo
│       │   ├── sobel.js           # Filtro Sobel
│       │   ├── laplacian.js       # Filtro Laplacian
│       │   ├── canny.js           # Filtro Canny
│       │   ├── threshold.js       # Filtro limiarização
│       │   ├── posterize.js       # Filtro posterização
│       │   ├── pixelate.js        # Filtro pixelização
│       │   ├── sepia.js           # Filtro sépia
│       │   └── motionDetect.js    # Detecção de movimento
│       │
│       └── utils/                 # Utilitários JavaScript
│           ├── imageProcessing.js # Processamento de imagem
│           ├── eventBus.js        # Sistema de eventos
│           ├── logger.js          # Sistema de logs
│           └── config.js          # Configurações do frontend
│
└── docs/                          # Documentação
    ├── ARCHITECTURE.md            # Documentação de arquitetura
    ├── API.md                     # Documentação de API
    └── FILTERS.md                 # Documentação de filtros
```

## 🔧 Tecnologias Utilizadas

### Backend
- **Python 3.12+**: Linguagem principal
- **Flask**: Framework web
- **Requests**: Cliente HTTP para detecção de stream

### Frontend
- **HTML5**: Estrutura semântica
- **CSS3**: Estilos modulares com variáveis CSS
- **JavaScript ES6+**: Módulos, arrow functions, async/await
- **Canvas API**: Renderização de vídeo

### Design
- **Inspiração**: Notion - Minimalismo, espaço em branco, tipografia limpa
- **Tema**: Claro/Escuro nativo
- **Responsividade**: Mobile-first, mobile/tablet/desktop

## 📚 Documentação

Para mais informações, consulte:
- [Arquitetura do Projeto](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Sistema de Filtros](docs/FILTERS.md)

## 🎨 Filtros Disponíveis

- ⬜ Escala de Cinza
- ⚫ Negativo
- ☀️ Brilho
- 🎨 Contraste
- ✨ Nitidez (Sharpen)
- 🌫️ Desfoque Gaussian (Blur)
- 🎭 Relevo (Emboss)
- 📐 Sobel
- 📊 Laplacian
- 🔍 Canny
- ⚪ Limiarização (Threshold)
- 🎞️ Posterização
- 🔲 Pixelização
- 🟤 Sépia
- 👁️ Detecção de Movimento

## 🚀 Controles

| Ação | Controle |
|------|----------|
| Play/Pausa | Clique na imagem ou botão de play |
| Modo Tela Cheia | F ou botão fullscreen |
| Zoom | Scroll do mouse |
| Pan (Mover) | Arrastar com mouse |
| Rotação | Controlador na barra lateral |
| Espelho H/V | Botões na barra lateral |
| Snapshot | Botão câmera na barra lateral |
| Reconexão | Botão reconectar |

## 🔐 Segurança

- Validação de todos os inputs
- Tratamento de erros robusto
- CORS configurado apropriadamente
- Variáveis sensíveis em `.env`

## 🤖 Preparação para IA

A arquitetura está preparada para futuras integrações:

- **YOLO**: Detecção de objetos
- **Tesseract/EasyOCR**: Reconhecimento de texto
- **Face Detection**: Reconhecimento facial
- **MediaPipe**: Detecção de pose e hand tracking
- **Segmentação**: Segmentação de imagens
- **Rastreamento**: Tracking de pessoas
- **Análise Inteligente**: Processamento avançado de vídeo

## 📝 Licença

MIT

## 👤 Autor

luizniz

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests.
