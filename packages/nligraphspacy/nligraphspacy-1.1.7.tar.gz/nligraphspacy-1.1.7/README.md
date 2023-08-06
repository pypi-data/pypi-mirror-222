# NLIGraphSpacy
Knowledge graph using NLP Spacy

## Installation

```python
pip install nligraphspacy
```

## Implementation

```python
from nligraphspacy import NLIGRAPH
nligraph = NLIGRAPH.RelationEntityExtract("She worked in the city of London")
nligraph.process_text()
# ('She', 'worked', 'London')

nligraph.get_seperate_entities()
# [{'text': 'A', 'label': ''},
# {'text': 'DAG', 'label': 'SOURCE-NODE'},
# {'text': 'is', 'label': ''},
# {'text': 'used', 'label': 'EDGE'},
# {'text': 'for', 'label': ''},
# {'text': 'organizing', 'label': ''},
# {'text': 'tasks', 'label': 'TARGET-NODE'}]
```
