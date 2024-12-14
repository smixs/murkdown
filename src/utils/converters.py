"""
File conversion utilities for MarkItDown Web
"""
from pathlib import Path
from typing import Optional, Dict, Any, Union
from dataclasses import dataclass
from markitdown import MarkItDown

# Constants
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
SUPPORTED_FORMATS = {
    'pdf': 'application/pdf',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'txt': 'text/plain',
    'html': 'text/html',
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'mp3': 'audio/mpeg',
    'wav': 'audio/wav',
}

@dataclass
class ConversionResult:
    """Data class for conversion results"""
    success: bool
    content: Optional[str] = None
    title: Optional[str] = None
    error: Optional[str] = None
    original_file: Optional[str] = None
    output_file: Optional[str] = None

class MarkdownConverter:
    """Class for handling markdown conversions"""
    
    def __init__(self):
        """Initialize the converter"""
        self._converter = MarkItDown()
    
    def validate_file(self, file_path: Union[str, Path]) -> tuple[bool, Optional[str]]:
        """
        Validate file before conversion
        
        Args:
            file_path: Path to the file
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        file_path = Path(file_path)
        
        # Check existence
        if not file_path.exists():
            return False, f"File '{file_path}' does not exist"
        
        # Check size
        if file_path.stat().st_size > MAX_FILE_SIZE:
            return False, f"File size exceeds {MAX_FILE_SIZE/1024/1024}MB limit"
        
        # Check format
        if file_path.suffix.lower()[1:] not in SUPPORTED_FORMATS:
            return False, f"Unsupported file format: {file_path.suffix}"
        
        return True, None
    
    def convert_file(self, file_path: Union[str, Path], **options) -> ConversionResult:
        """
        Convert file to markdown
        
        Args:
            file_path: Path to the input file
            **options: Additional conversion options
            
        Returns:
            ConversionResult object
        """
        file_path = Path(file_path)
        
        # Validate file
        is_valid, error = self.validate_file(file_path)
        if not is_valid:
            return ConversionResult(
                success=False,
                error=error,
                original_file=str(file_path)
            )
        
        try:
            # Convert file
            result = self._converter.convert_local(str(file_path))
            
            # Create output filename
            output_file = file_path.with_suffix('.md')
            
            # Save result
            output_file.write_text(result.text_content)
            
            return ConversionResult(
                success=True,
                content=result.text_content,
                title=result.title,
                original_file=str(file_path),
                output_file=str(output_file)
            )
            
        except Exception as e:
            return ConversionResult(
                success=False,
                error=str(e),
                original_file=str(file_path)
            )
    
    @staticmethod
    def get_supported_formats() -> Dict[str, str]:
        """Get dictionary of supported file formats"""
        return SUPPORTED_FORMATS.copy()