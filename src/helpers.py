import os
import time
from doc_preprocessing.dataclasses import Span
from refined.processor import Refined
from nltk.tokenize import word_tokenize
refined = Refined.from_pretrained(model_name='wikipedia_model',
                                  entity_set='wikipedia',
                                  data_dir=os.path.join(os.path.expanduser('~'), '.cache/refined/'),
                                  download_files=True,
                                  debug=False,
                                  use_precomputed_descriptions=True,
                                  requires_redirects_and_disambig=True)


def get_refined(text):
    tokens = word_tokenize(text)
    indexes = []
    for index, token in enumerate(tokens):
        indexes.append({"word": token, "index": index})
    ents = refined.process_text(text)
    response = []
    for ent in ents:
        index = []
        for o in indexes:
            if o["word"] in ent.text:
                index.append(o["index"])
        response.append({"text": ent.text, "entity_id": ent.pred_entity_id, "mention_type": ent.coarse_mention_type, "idx": index})
    return response
