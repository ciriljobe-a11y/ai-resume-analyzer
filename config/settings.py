"""Application settings and configuration."""
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration."""

    # Environment
    debug: bool = False
    environment: str = "development"

    # AI Provider
    ai_provider: str = "openai"
    ai_api_key: Optional[str] = None
    ai_model: str = "gpt-4"
    ai_base_url: str = "https://api.openai.com/v1"
    ai_timeout: int = 30

    # File handling
    max_file_size_mb: int = 10
    supported_resume_formats: list[str] = ["pdf", "docx", "txt"]
    supported_job_formats: list[str] = ["txt"]

    # Database
    database_path: str = "data/resume_analyzer.db"

    # Temporary files
    temp_upload_dir: str = "temp_uploads"
    delete_temp_files_after_analysis: bool = True

    # Scoring weights (must sum to 100)
    scoring_weights: dict[str, float] = {
        "keyword_match": 30.0,
        "required_skills_coverage": 20.0,
        "experience_relevance": 15.0,
        "resume_structure": 10.0,
        "job_title_alignment": 10.0,
        "education_certification_alignment": 5.0,
        "skills_section_quality": 5.0,
        "ats_formatting_compatibility": 5.0,
    }

    # Resume sections to detect
    resume_sections: dict[str, list[str]] = {
        "contact": ["contact", "contact information", "contact details"],
        "summary": ["summary", "professional summary", "executive summary", "overview"],
        "objective": ["objective", "career objective"],
        "skills": ["skills", "technical skills", "core skills", "competencies"],
        "technical_skills": ["technical skills", "technical competencies"],
        "soft_skills": ["soft skills", "interpersonal skills"],
        "experience": [
            "experience",
            "professional experience",
            "work experience",
            "employment history",
        ],
        "education": ["education", "educational background"],
        "projects": ["projects", "portfolio", "notable projects"],
        "certifications": ["certifications", "licenses", "certifications and licenses"],
        "achievements": ["achievements", "awards", "accomplishments"],
        "awards": ["awards", "honors"],
        "publications": ["publications", "research"],
        "languages": ["languages", "language skills"],
        "volunteer": ["volunteer", "volunteer experience", "volunteering"],
        "interests": ["interests", "hobbies", "additional interests"],
    }

    # Common abbreviations and their full forms
    abbreviations: dict[str, str] = {
        "ms": "microsoft",
        "sql": "sql",
        "ai": "artificial intelligence",
        "ml": "machine learning",
        "nlp": "natural language processing",
        "etl": "extract transform load",
        "crm": "customer relationship management",
        "hr": "human resources",
        "devops": "devops",
        "ci/cd": "continuous integration continuous deployment",
        "ux": "user experience",
        "ui": "user interface",
        "api": "application programming interface",
        "db": "database",
        "qa": "quality assurance",
    }

    # Technology aliases
    technology_aliases: dict[str, list[str]] = {
        "python": ["python3", "py"],
        "javascript": ["js", "nodejs", "node"],
        "typescript": ["ts"],
        "java": ["jvm"],
        "c#": ["csharp", "c-sharp"],
        "sql": ["sql server", "mysql", "postgresql", "oracle"],
        "excel": ["ms excel", "microsoft excel"],
        "word": ["ms word", "microsoft word"],
        "powerpoint": ["ppt", "ms powerpoint", "microsoft powerpoint"],
        "aws": ["amazon web services"],
        "gcp": ["google cloud platform", "google cloud"],
        "azure": ["microsoft azure"],
    }

    # ATS risk keywords
    ats_risk_keywords: dict[str, list[str]] = {
        "table": ["table", "tabular"],
        "image": ["image", "graphic", "picture", "icon"],
        "textbox": ["text box", "textbox"],
        "column": ["column", "columns", "multi-column"],
        "header": ["header", "footer"],
    }

    class Config:
        """Pydantic config."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()
