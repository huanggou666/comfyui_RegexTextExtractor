# Regex Text Extractor Node for ComfyUI

This custom node for ComfyUI allows you to extract text using regular expressions from input text.

## Features

- Extract text using custom regular expressions
- Select which match to return using an index
- Default pattern for extracting image dimensions (e.g., "600x1064")
- Error handling for invalid patterns or out-of-range indices

## Usage

1. Connect a text input to the "text" input
2. Optionally modify the regex pattern (default is `(\d+)x(\d+)` for image dimensions)
3. Set the match index (1-based) to select which match to return
4. The node will output the matched text

## Example

For the input text:
```
参考图像处理成功，尺寸: 600x1064
图像转换为张量成功, 形状: torch.Size([1, 1024, 1024, 3])
```

Using the default pattern `(\d+)x(\d+)`:
- Match index 1 will return: "600x1064"
- Match index 2 will return: "1024x1024"

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory
2. Restart ComfyUI

## Requirements

No additional requirements needed. Uses Python's built-in `re` module. 