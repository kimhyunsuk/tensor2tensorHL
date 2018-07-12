import re
import pandas as pd

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry

@registry.register_problem
class MyProblem2(text_problems.Text2TextProblem):

  @property
  def approx_vocab_size(self):
    return 2**13  # ~8k

  @property
  def is_generate_per_split(self):
    # generate_data will shard the data into TRAIN and EVAL for us.
    return False

  @property
  def dataset_splits(self):
    """Splits of data to produce and number of output shards for each."""
    # 10% evaluation data
    return [{
        "split": problem.DatasetSplit.TRAIN,
        "shards": 9,
    }, {
        "split": problem.DatasetSplit.EVAL,
        "shards": 1,
    }]

  def generate_samples(self, data_dir, tmp_dir, dataset_split):
    #filename = 'c:\\temp\\tsv.txt'
    filename = 'tsv.txt'
    df = pd.read_csv(filename, delimiter='\t')
    for key, row in df.iterrows():
        q, a = row['question'], row['answer']
        if not q or not a:
            continue

        if type(q) == float:
            q = 'nan'
        if type(a) == float:
            a = q
        yield {
            'inputs': q.strip(),
            'targets': a.strip()
        }
