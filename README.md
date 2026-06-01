# 🤖 MetaGPT Web Application

A containerized web application built with MetaGPT, Gradio, and multiple AI providers (OpenAI, Google Generative AI).

## 📋 Features

- 🚀 Multi-agent framework powered by MetaGPT
- 🎨 Beautiful web interface using Gradio
- 🔌 Integration with OpenAI and Google Generative AI
- 🐳 Docker & Docker Compose ready
- ⚡ Redis cache support
- 📊 Logging and monitoring
- 🔒 Environment-based configuration

## 📦 Prerequisites

- Docker & Docker Compose (recommended)
- Python 3.11+ (for local development)
- API Keys:
  - OpenAI API Key (from https://platform.openai.com)
  - Google Generative AI API Key (from https://makersuite.google.com)

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

1. **Clone or navigate to the repository**
   ```bash
   cd Meta-GPT
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```

3. **Add your API keys to `.env`**
   ```bash
   nano .env
   # or use your preferred editor
   ```
   Fill in:
   - `OPENAI_API_KEY=sk-...`
   - `GOOGLE_API_KEY=...`

4. **Start the application**
   ```bash
   docker-compose up --build
   ```

5. **Access the web interface**
   - Open your browser and go to: `http://localhost:7860`

6. **Stop the application**
   ```bash
   docker-compose down
   ```

### Option 2: Local Development

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create and configure environment file**
   ```bash
   cp .env.example .env
   ```
   Add your API keys to `.env`

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the interface**
   - Open your browser and go to: `http://localhost:7860`

## 📁 Project Structure

```
Meta-GPT/
├── app.py                 # Main application file
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── logs/                # Application logs (created at runtime)
├── workspace/           # Working directory (created at runtime)
└── config/              # MetaGPT configuration (created at runtime)
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_key_here
PYTHONUNBUFFERED=1
LOG_LEVEL=INFO
```

### Services (Docker Compose)

- **metagpt**: Main application (Port 7860)
- **redis**: Cache service (Port 6379)

## 📝 API Keys Setup

### OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy and paste it in your `.env` file

### Google Generative AI API Key

1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy and paste it in your `.env` file

## 🔍 Troubleshooting

### Port Already in Use

If port 7860 is already in use, modify `docker-compose.yml`:
```yaml
ports:
  - "8080:7860"  # Access via localhost:8080
```

### API Keys Not Working

- Verify keys are correctly set in `.env`
- Check that keys have necessary permissions
- Restart the containers: `docker-compose restart`

### Permission Denied (Linux/Mac)

Run with sudo:
```bash
sudo docker-compose up
```

### Check Logs

View application logs:
```bash
docker-compose logs -f metagpt
```

## 🛠️ Development

### Adding New Features

1. Modify `app.py`
2. Update `requirements.txt` if adding new dependencies
3. Rebuild: `docker-compose up --build`

### Running Tests

```bash
python -m pytest tests/
```

## 📚 Documentation

- [MetaGPT GitHub](https://github.com/FoundationAgents/MetaGPT)
- [Gradio Documentation](https://www.gradio.app/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Google Generative AI Documentation](https://ai.google.dev/docs)

## 📄 License

This project is provided as-is. Ensure you comply with the licenses of:
- MetaGPT
- Gradio
- OpenAI and Google's terms of service

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review logs in `logs/app.log`
3. Check the main repository issues

## 🎯 Next Steps

- [ ] Configure API keys in `.env`
- [ ] Start with Docker Compose: `docker-compose up --build`
- [ ] Access the web interface at `http://localhost:7860`
- [ ] Test with sample prompts
- [ ] Customize `app.py` for your needs

---

**Status**: Ready for deployment ✅

Happy coding! 🚀
