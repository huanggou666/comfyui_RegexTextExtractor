import re

class RegexTextExtractor:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "pattern": ("STRING", {"default": r"(\d+)x(\d+)"}),
                "match_index": ("INT", {"default": 1, "min": 1, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "extract_text"
    CATEGORY = "text"

    def extract_text(self, text, pattern, match_index):
        try:
            # Find all matches
            matches = re.findall(pattern, text)
            
            if not matches:
                return ("",)
            
            # Convert match_index to 0-based index
            index = match_index - 1
            
            # Check if the requested index exists
            if index >= len(matches):
                return ("",)
            
            # Get the matched text
            match = matches[index]
            
            # If the pattern has groups, join them with 'x'
            if isinstance(match, tuple):
                return (f"{match[0]}x{match[1]}",)
            else:
                return (match,)
                
        except Exception as e:
            print(f"Error in RegexTextExtractor: {str(e)}")
            return ("",)

NODE_CLASS_MAPPINGS = {
    "RegexTextExtractor": RegexTextExtractor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RegexTextExtractor": "Regex Text Extractor"
} 