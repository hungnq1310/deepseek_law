# DeepSeek Law Project

## Project Structure

```
deepseek_law/
│
├── docker/              # Docker configuration files
├── notebooks/          # Jupyter notebooks
│   └── test.ipynb     # Test notebook
├── src/               # Source code
├── tests/             # Test files
├── .env              # Environment variables
├── docker-compose.yml # Docker compose configuration
└── README.md         # This file
```

## Installation

### Local Environment Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

### Docker Setup

1. Make sure Docker and Docker Compose are installed on your system
2. Build and run the containers:
```bash
docker-compose up -d
```

## Running test.ipynb

1. Start Jupyter server:
```bash
jupyter notebook
```

2. Navigate to `notebooks/test.ipynb`

3. Ensure all dependencies are installed in your environment

4. Run all cells in the notebook:
    - Click "Kernel" -> "Restart & Run All"
    - Or use Shift + Enter to run cells individually

## Docker Compose Usage

1. Start services:
```bash
docker-compose up -d
```

2. View logs:
```bash
docker-compose logs -f
```

3. Stop services:
```bash
docker-compose down
```

4. Rebuild containers:
```bash
docker-compose up -d --build
```


## Additional Notes

- Make sure PORTS specified in docker-compose.yml are available
- Check Docker logs if services fail to start
- Refer to individual service documentation for troubleshooting
