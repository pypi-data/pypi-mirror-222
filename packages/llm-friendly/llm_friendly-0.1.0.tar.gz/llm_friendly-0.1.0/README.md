# llm-friendly

`llm-friendly` converts API responses to LLM-friendly text.

```mermaid
flowchart LR
    APIResponse["API Response \n or \n JSON body"]
    LLMFriendly["llm-friendly"]
    LLM["Large-Language Model \n (e.g. OpenAI or Llama 2"]
    
    APIResponse -- JSON --> LLMFriendly -- string --> LLM
```

## Currently Supported Source APIs

 - Amazon Web Services (AWS)
   - Textract

[//]: # ( - Azure AI)

[//]: # (   - Vision)

[//]: # ( - Google Cloud Platform &#40;GCP&#41;)

[//]: # (   - Vision)

## Installation

```shell
pip install git+https://github.com/GovTechSG/llm-friendly.git
```

## Usage

```python
from llm_friendly.aws import textract

textract_response = {...}
text_content = textract.to_llm_output(textract_response)
print(text_content)
```

## Tests

```shell
pytest
```