from typing import Any, Optional, Dict, List, Set

from llm_friendly.aws import table_parser


def to_llm_output(textract_response: dict[str, Any]) -> str:
    blocks = textract_response.get('Blocks', [])
    analyze_document_text = ""
    blocks_to_ignore = set()

    for item in blocks:
        if item['BlockType'] == 'TABLE':
            blocks_to_ignore.update(_get_children_ids_recursively(blocks, item['Id']))

    for item in blocks:
        if item['BlockType'] == 'TABLE':
            analyze_document_text += table_parser.get_table_as_csv(blocks, item) + '\n'

        already_analyzed_as_table = _is_id_in_set_or_children(blocks, item['Id'], blocks_to_ignore)

        if item['BlockType'] == 'LINE' and not already_analyzed_as_table:
            analyze_document_text += item['Text'] + '\n'

    return analyze_document_text


def _get_children_ids_recursively(data: List[Dict[str, Any]], target_id: str) -> Set[str]:
    ids: Set[str] = set()
    index = _find_element_index(data, target_id)

    if index is not None:
        children_ids = []

        for rel in data[index].get('Relationships', []):
            if rel['Type'] == 'CHILD':
                children_ids.extend(rel['Ids'])

        for child_id in children_ids:
            ids.add(child_id)
            ids.update(_get_children_ids_recursively(data, child_id))

    return ids


def _is_id_in_set_or_children(data, target_id, id_set):
    index = _find_element_index(data, target_id)
    if index is not None:
        if data[index]['Id'] in id_set:
            return True
        children_ids = []
        for rel in data[index].get('Relationships', []):
            if rel['Type'] == 'CHILD':
                children_ids.extend(rel['Ids'])
        for child_id in children_ids:
            if _is_id_in_set_or_children(data, child_id, id_set):
                return True
    return False


def _find_element_index(data, target_id) -> Optional[int]:
    for i, elem in enumerate(data):
        if elem['Id'] == target_id:
            return i
    return None
