FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git curl npm nodejs build-essential && rm -rf /var/lib/apt/lists/*

RUN npm install -g pnpm @mermaid-js/mermaid-cli

RUN git clone https://github.com/FoundationAgents/MetaGPT.git . || true

RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir gradio openai google-generativeai pydantic pyyaml loguru

RUN mkdir -p ~/.metagpt

EXPOSE 7860

CMD ["python", "app.py"]