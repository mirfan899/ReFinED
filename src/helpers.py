import os
import time
from doc_preprocessing.dataclasses import Span
from refined.processor import Refined

refined = Refined.from_pretrained(model_name='wikipedia_model',
                                  entity_set='wikipedia',
                                  data_dir=os.path.join(os.path.expanduser('~'), '.cache/refined/'),
                                  download_files=True,
                                  debug=False,
                                  use_precomputed_descriptions=True,
                                  requires_redirects_and_disambig=True)


def get_refined(text):
    ents = refined.process_text(text)
    response = []
    for ent in ents:
        response.append({"text": ent.text, "entity_id": ent.pred_entity_id, "mention_type": ent.coarse_mention_type})
    return response
