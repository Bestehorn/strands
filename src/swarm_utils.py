"""
Utility functions for cleaning and formatting swarm output.

This module provides functions to clean up swarm analysis results by removing
control characters, ANSI escape sequences, and formatting the output for
better human readability.
"""

import json
import re
from typing import Dict, List, Any, Union


def clean_swarm_text(text: str) -> str:
    """
    Clean individual text entries by removing control characters and formatting.
    
    Args:
        text: The text string to clean
        
    Returns:
        Cleaned text string
    """
    if not isinstance(text, str):
        return text
    
    # Remove ANSI color codes (both actual and escaped)
    text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    text = re.sub(r'\\u001b\[[0-9;]*m', '', text)
    
    # Replace box-drawing characters with ASCII equivalents
    box_chars = {
        # Direct Unicode characters
        '╭': '+', '╮': '+', '╰': '+', '╯': '+',
        '─': '-', '│': '|', '├': '+', '└': '+',
        '┤': '+', '┬': '+', '┴': '+', '┼': '+',
        '═': '=', '╔': '+', '╗': '+', '╚': '+',
        '╝': '+', '║': '|', '╠': '+', '╣': '+',
        '╦': '+', '╩': '+', '╬': '+',
        # Unicode escape sequences
        '\u256d': '+', '\u256e': '+', '\u2570': '+', '\u256f': '+',
        '\u2500': '-', '\u2502': '|', '\u251c': '+', '\u2514': '+',
        '\u2524': '+', '\u252c': '+', '\u2534': '+', '\u253c': '+',
        '\u2550': '=', '\u2551': '|', '\u2552': '+', '\u2553': '+',
        '\u2554': '+', '\u2555': '+', '\u2556': '+', '\u2557': '+',
        '\u2558': '+', '\u2559': '+', '\u255a': '+', '\u255b': '+',
        '\u255c': '+', '\u255d': '+', '\u255e': '+', '\u255f': '+',
        '\u2560': '+', '\u2561': '+', '\u2562': '+', '\u2563': '+',
        '\u2564': '+', '\u2565': '+', '\u2566': '+', '\u2567': '+',
        '\u2568': '+', '\u2569': '+', '\u256a': '+', '\u256b': '+',
        '\u256c': '+',
    }
    
    for old_char, new_char in box_chars.items():
        text = text.replace(old_char, new_char)
    
    return text


def clean_swarm_output(json_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Clean up swarm output JSON by removing control characters and formatting.
    
    Args:
        json_data: List of dictionaries containing swarm output
        
    Returns:
        Cleaned list of dictionaries
    """
    cleaned_data = []
    
    for item in json_data:
        if isinstance(item, dict) and 'text' in item:
            cleaned_item = item.copy()
            cleaned_item['text'] = clean_swarm_text(item['text'])
            cleaned_data.append(cleaned_item)
        else:
            cleaned_data.append(item)
    
    return cleaned_data


def extract_swarm_content(json_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Extract only the meaningful content from swarm output.
    
    Args:
        json_data: List of dictionaries containing swarm output
        
    Returns:
        Dictionary with extracted content organized by type
    """
    content_sections = {
        'swarm_status': None,
        'agent_responses': [],
        'metrics': [],
        'collective_knowledge': []
    }
    
    for item in json_data:
        if isinstance(item, dict) and 'text' in item:
            text = item['text']
            
            # Extract swarm status
            if 'Swarm Status' in text:
                content_sections['swarm_status'] = clean_swarm_text(text)
            
            # Extract agent responses
            elif re.search(r'Agent agent_\d+.*Response:', text):
                # Parse the response content
                agent_match = re.search(r'Agent (agent_\d+)', text)
                agent_id = agent_match.group(1) if agent_match else 'unknown'
                
                response_start = text.find('Response:') + 9
                response_end = text.find('\n\nMetrics:') if '\n\nMetrics:' in text else len(text)
                response_text = text[response_start:response_end].strip()
                
                content_sections['agent_responses'].append({
                    'agent_id': agent_id,
                    'response': clean_swarm_text(response_text)
                })
            
            # Extract metrics
            elif re.search(r'Agent agent_\d+.*Metrics:', text):
                agent_match = re.search(r'Agent (agent_\d+)', text)
                agent_id = agent_match.group(1) if agent_match else 'unknown'
                
                metrics_start = text.find('Metrics:') + 8
                metrics_text = text[metrics_start:].strip()
                
                content_sections['metrics'].append({
                    'agent_id': agent_id,
                    'metrics': clean_swarm_text(metrics_text)
                })
            
            # Extract collective knowledge
            elif 'Collective Knowledge:' in text:
                # This section contains the JSON array of knowledge items
                knowledge_start = text.find('[')
                if knowledge_start != -1:
                    try:
                        knowledge_data = json.loads(text[knowledge_start:])
                        # Clean the content in knowledge data
                        for item in knowledge_data:
                            if 'content' in item:
                                item['content'] = clean_swarm_text(item['content'])
                        content_sections['collective_knowledge'] = knowledge_data
                    except:
                        pass
    
    return content_sections


def format_swarm_summary(extracted_content: Dict[str, Any], max_response_length: int = 500) -> str:
    """
    Format extracted swarm content into a readable summary.
    
    Args:
        extracted_content: Dictionary with extracted content
        max_response_length: Maximum length of response text to display
        
    Returns:
        Formatted summary string
    """
    summary = []
    
    summary.append("SWARM ANALYSIS SUMMARY")
    summary.append("=" * 60)
    
    if extracted_content['swarm_status']:
        summary.append("\nSWARM STATUS:")
        summary.append("-" * 40)
        summary.append(extracted_content['swarm_status'])
    
    if extracted_content['agent_responses']:
        summary.append("\nAGENT RESPONSES:")
        summary.append("-" * 40)
        
        for response in extracted_content['agent_responses']:
            summary.append(f"\n{response['agent_id']}:")
            response_text = response['response']
            if len(response_text) > max_response_length:
                summary.append(response_text[:max_response_length] + "...")
            else:
                summary.append(response_text)
    
    if extracted_content['metrics']:
        summary.append("\n\nPERFORMANCE METRICS:")
        summary.append("-" * 40)
        
        for metric in extracted_content['metrics']:
            summary.append(f"\n{metric['agent_id']}:")
            summary.append(metric['metrics'])
    
    return "\n".join(summary)


def save_cleaned_swarm_output(json_data: Union[List[Dict[str, Any]], str], 
                             output_file: str = 'cleaned_swarm_output.json',
                             format_output: bool = True) -> None:
    """
    Save cleaned swarm output to a file.
    
    Args:
        json_data: Swarm output data (list of dicts or JSON string)
        output_file: Path to output file
        format_output: Whether to format the output with indentation
    """
    # Parse JSON string if needed
    if isinstance(json_data, str):
        parsed_data = json.loads(json_data)
    else:
        parsed_data = json_data
    
    # Clean the data
    cleaned_data = clean_swarm_output(parsed_data)
    
    # Save to file
    with open(output_file, 'w', encoding='utf-8') as f:
        if format_output:
            json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
        else:
            json.dump(cleaned_data, f, ensure_ascii=False)


def display_swarm_analysis(swarm_result: Dict[str, Any], verbose: bool = True) -> Dict[str, Any]:
    """
    Display swarm analysis results in a clean, readable format.
    
    Args:
        swarm_result: The raw swarm result dictionary
        verbose: Whether to display full output or just summary
        
    Returns:
        Dictionary with cleaned and extracted content
    """
    # Handle the content key which contains the JSON data
    if isinstance(swarm_result.get('content'), list):
        json_data = swarm_result['content']
    elif isinstance(swarm_result.get('content'), str):
        # Try to parse as JSON
        try:
            json_data = json.loads(swarm_result['content'])
        except:
            # If not JSON, wrap in a list
            json_data = [{'text': swarm_result['content']}]
    else:
        json_data = []
    
    # Clean the data
    cleaned_data = clean_swarm_output(json_data)
    
    # Extract meaningful content
    extracted_content = extract_swarm_content(cleaned_data)
    
    # Display the summary
    if verbose:
        print(format_swarm_summary(extracted_content))
    
    return {
        'cleaned_data': cleaned_data,
        'extracted_content': extracted_content
    }
