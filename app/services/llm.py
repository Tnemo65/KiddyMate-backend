import google.generativeai as genai
from typing import Optional
from app.config import settings

_client_initialized: bool = False

def _ensure_client() -> None:
    global _client_initialized
    if _client_initialized:
        return
    if not settings.GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured")
    genai.configure(api_key=settings.GEMINI_API_KEY)
    _client_initialized = True

def generate_gemini_response(prompt: str, system_instruction: Optional[str] = None) -> str:
    """
    Generate a response from Gemini using a safe default model.
    """
    _ensure_client()
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction or "You are a friendly Vietnamese assistant for kids. Keep responses short and supportive."
    )
    result = model.generate_content(prompt)
    text = ""
    if hasattr(result, "text") and result.text:
        text = result.text.strip()
    elif hasattr(result, "candidates") and result.candidates:
        parts = getattr(result.candidates[0], "content", None)
        if parts and hasattr(parts, "parts") and parts.parts:
            text = "".join(getattr(p, "text", "") for p in parts.parts).strip()
    return text or "Xin lỗi, mình chưa nghĩ ra câu trả lời. Bạn thử hỏi lại nhé!"

