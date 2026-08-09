# ResumeAI - AI Resume Analyzer

A production-ready Python application that uses AI to analyze resumes against job descriptions, providing ATS compatibility scoring, keyword matching, and actionable improvement recommendations.

## Features

- **Resume Upload & Parsing**: Support for PDF, DOCX, and TXT formats
- **Job Description Analysis**: Extract and categorize job requirements
- **ATS Compatibility Scoring**: Transparent, explainable scoring system (not claimed to be exact)
- **Intelligent Keyword Matching**: Handle abbreviations, aliases, and variations
- **Skill Analysis**: Categorized technical and soft skills matching
- **Experience Relevance Analysis**: Evaluate job title and responsibility alignment
- **Resume Quality Audit**: Structure, formatting, and ATS risk detection
- **AI-Powered Recommendations**: Prioritized, actionable improvement suggestions
- **Resume Rewriter**: Improve wording while preserving factual accuracy
- **Multi-Format Export**: PDF reports, Excel sheets, and improved DOCX resumes
- **Analysis History**: Local SQLite storage of previous analyses
- **Privacy-First**: Local processing, no permanent storage of uploaded files
- **Professional SaaS UI**: Clean, modern, accessible Streamlit interface

## Quick Start

### Windows Setup

```bash
git clone https://github.com/ciriljobe-a11y/ai-resume-analyzer.git
cd ai-resume-analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

### macOS/Linux Setup

```bash
git clone https://github.com/ciriljobe-a11y/ai-resume-analyzer.git
cd ai-resume-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## Environment Variables

Create `.env` file:

```
AI_PROVIDER=openai
AI_API_KEY=your_api_key_here
AI_MODEL=gpt-4
AI_BASE_URL=https://api.openai.com/v1
MAX_FILE_SIZE_MB=10
DEBUG=false
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Privacy](docs/PRIVACY.md)
- [Security](docs/SECURITY.md)
- [Development](docs/DEVELOPMENT.md)

## Testing

```bash
pytest -v
```

## License

MIT License
