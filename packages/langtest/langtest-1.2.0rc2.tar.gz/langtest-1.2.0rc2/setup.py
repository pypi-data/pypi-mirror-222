# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['langtest',
 'langtest.augmentation',
 'langtest.datahandler',
 'langtest.modelhandler',
 'langtest.pipelines',
 'langtest.pipelines.transformers',
 'langtest.pipelines.utils',
 'langtest.pipelines.utils.data_helpers',
 'langtest.transform',
 'langtest.utils',
 'langtest.utils.custom_types']

package_data = \
{'': ['*'],
 'langtest': ['data/*',
              'data/BBQ/*',
              'data/BoolQ/*',
              'data/HellaSwag/*',
              'data/MMLU/*',
              'data/NQ-open/*',
              'data/NarrativeQA/*',
              'data/OpenBookQA/*',
              'data/Translation/*',
              'data/TruthfulQA/*',
              'data/Xsum/*',
              'data/config/*',
              'data/conll/*',
              'data/imdb/*',
              'data/quac/*',
              'data/textcat_imdb/*',
              'data/textcat_imdb/textcat/*',
              'data/textcat_imdb/vocab/*',
              'data/toxicity/*']}

install_requires = \
['jsonlines>=3.1.0,<4.0.0',
 'nest-asyncio>=1.5.0,<2.0.0',
 'pandas>=2.0.3,<3.0.0',
 'pydantic==1.10.6',
 'pyyaml>=6.0,<7.0',
 'tqdm>=4.65.0,<5.0.0',
 'typing-extensions<4.6.0']

extras_require = \
{'ai21': ['langchain>=0.0.200,<0.0.201', 'ai21>=1.1.0,<2.0.0'],
 'cohere': ['langchain>=0.0.200,<0.0.201', 'cohere>=4.10.0,<5.0.0'],
 'evaluate': ['rouge-score>=0.1.2,<0.2.0',
              'evaluate>=0.4.0,<0.5.0',
              'seqeval>1.2.0'],
 'huggingface-hub': ['langchain>=0.0.200,<0.0.201', 'huggingface_hub>0.16.0'],
 'johnsnowlabs': ['johnsnowlabs==4.3.5'],
 'langchain': ['langchain>=0.0.200,<0.0.201'],
 'metaflow': ['metaflow>=2.9.0'],
 'mlflow': ['mlflow>=2.5.0,<3.0.0'],
 'openai': ['langchain>=0.0.200,<0.0.201', 'openai>0.27.0'],
 'spacy': ['spacy>=3.0.0'],
 'transformers': ['transformers<4.31.0',
                  'torch>=2.0.1,<3.0.0',
                  'accelerate<0.21.0']}

setup_kwargs = {
    'name': 'langtest',
    'version': '1.2.0rc2',
    'description': 'John Snow Labs provides a library for delivering safe & effective NLP models.',
    'long_description': '# LangTest: Deliver Safe & Effective Language Models\n\n<p align="center">\n    <a href="https://github.com/JohnSnowLabs/langtest/actions" alt="build">\n        <img src="https://github.com/JohnSnowLabs/langtest/workflows/build/badge.svg" /></a>\n    <a href="https://github.com/JohnSnowLabs/langtest/releases" alt="Current Release Version">\n        <img src="https://img.shields.io/github/v/release/JohnSnowLabs/langtest.svg?style=flat-square&logo=github" /></a>\n    <a href="https://github.com/JohnSnowLabs/langtest/blob/master/LICENSE" alt="License">\n        <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" /></a>\n    <a href="https://pypi.org/project/langtest/" alt="PyPi downloads">\n        <img src="https://static.pepy.tech/personalized-badge/langtest?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads" /></a>\n</p>\n\n\n<p align="center">\n  <a href="#project\'s-website">Project\'s Website</a> •\n  <a href="#key-features">Key Features</a> •\n  <a href="#how-to-use">How To Use</a> •\n  <a href="#community-support">Community Support</a> •\n  <a href="#contributing">Contributing</a> •\n  <a href="#mission">Mission</a> •\n  <a href="#license">License</a>\n</p>\n\n![screenshot](https://raw.githubusercontent.com/JohnSnowLabs/langtest/gh-pages/docs/assets/images/langtest/langtest_flow_graphic.jpeg)\n\n## Project\'s Website\n\nTake a look at our official page for user documentation and examples: [langtest.org](http://langtest.org/) \n\n## Key Features\n\n- Generate and execute more than 50 distinct types of tests only with 1 line of code\n- Test all aspects of model quality: robustness, bias, representation, fairness and accuracy.\u200b\n- Automatically augment training data based on test results (for select models)\u200b\n- Support for popular NLP frameworks for NER, Translation and Text-Classifcation: Spark NLP, Hugging Face & Transformers.\n- Support for testing LLMS ( OpenAI, Cohere, AI21, Hugging Face Inference API and Azure-OpenAI LLMs) for question answering, toxicity and summarization task. \n\n## How To Use\n\n```python\n# Install langtest\n!pip install langtest transformers==4.28.1\n\n# Import and create a Harness object\nfrom langtest import Harness\nh = Harness(task=\'ner\', model=\'dslim/bert-base-NER\', hub=\'huggingface\')\n\n# Generate test cases, run them and view a report\nh.generate().run().report()\n```\n\n> **Note**\n> For more extended examples of usage and documentation, head over to [langtest.org](https://www.langtest.org)\n\n## Community Support\n\n- [Slack](https://www.johnsnowlabs.com/slack-redirect/) For live discussion with the LangTest community, join the `#langtest` channel\n- [GitHub](https://github.com/JohnSnowLabs/langtest/tree/main) For bug reports, feature requests, and contributions\n- [Discussions](https://github.com/JohnSnowLabs/langtest/discussions) To engage with other community members, share ideas, and show off how you use LangTest!\n\n## Mission\n\nWhile there is a lot of talk about the need to train AI models that are safe, robust, and fair - few tools have been made available to data scientists to meet these goals. As a result, the front line of NLP models in production systems reflects a sorry state of affairs. \n\nWe propose here an early stage open-source community project that aims to fill this gap, and would love for you to join us on this mission. We aim to build on the foundation laid by previous research such as [Ribeiro et al. (2020)](https://arxiv.org/abs/2005.04118), [Song et al. (2020)](https://arxiv.org/abs/2004.00053), [Parrish et al. (2021)](https://arxiv.org/abs/2110.08193), [van Aken et al. (2021)](https://arxiv.org/abs/2111.15512) and many others. \n\n[John Snow Labs](www.johnsnowlabs.com) has a full development team allocated to the project and is committed to improving the library for years, as we do with other open-source libraries. Expect frequent releases with new test types, tasks, languages, and platforms to be added regularly. We look forward to working together to make safe, reliable, and responsible NLP an everyday reality. \n\n## Comparing Benchmark Datasets: Use Cases and Evaluations\n\nLangtest comes with different datasets to test your models, covering a wide range of use cases and evaluation scenarios.\n\n| Dataset       | Use Case                                                                                           | Notebook                                                                                                                                             |\n|---------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|\n| [**BoolQ**](https://aclanthology.org/N19-1300/)    | Evaluate the ability of your model to answer boolean questions (yes/no) based on a given passage or context.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/BoolQ_dataset.ipynb)   |\n| [**NQ-open**](https://aclanthology.org/Q19-1026/)   | Evaluate the ability of your model to answer open-ended questions based on a given passage or context.  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/NQ_open_dataset.ipynb)   |\n| [**TruthfulQA**](https://aclanthology.org/2022.acl-long.229/) | Evaluate the model\'s capability to answer questions accurately and truthfully based on the provided information.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/TruthfulQA_dataset.ipynb)   |\n| [**MMLU**](https://arxiv.org/abs/2009.03300)      | Evaluate language understanding models\' performance in different domains. It covers 57 subjects across STEM, the humanities, the social sciences, and more.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/mmlu_dataset.ipynb)   |\n| [**NarrativeQA**](https://aclanthology.org/Q18-1023/) | Evaluate your model\'s ability to comprehend and answer questions about long and complex narratives, such as stories or articles.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/NarrativeQA_Question_Answering.ipynb)   |\n| [**HellaSwag**](https://aclanthology.org/P19-1472/) | Evaluate your model\'s ability in completions of sentences.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/HellaSwag_Question_Answering.ipynb)   |\n| [**Quac**](https://aclanthology.org/D18-1241/)      | Evaluate your model\'s ability to answer questions given a conversational context, focusing on dialogue-based question-answering.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/quac_dataset.ipynb)   |\n| [**OpenBookQA**](https://allenai.org/data/open-book-qa)| Evaluate your model\'s ability to answer questions that require complex reasoning and inference based on general knowledge, similar to an "open-book" exam.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/quac_dataset.ipynb)   |\n| [**BBQ**](https://arxiv.org/abs/2110.08193)       | Evaluate how your model responds to questions in the presence of social biases against protected classes across various social dimensions. Assess biases in model outputs with both under-informative and adequately informative contexts, aiming to promote fair and unbiased question-answering models.   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/BBQ_dataset.ipynb)   |\n|[**XSum**](https://aclanthology.org/D18-1206/) | Evaluate your model\'s ability to generate concise and informative summaries for long articles with the XSum dataset. It consists of articles and corresponding one-sentence summaries, offering a valuable benchmark for text summarization models. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/XSum_dataset.ipynb)|\n|[**Real Toxicity Prompts**](https://aclanthology.org/2020.findings-emnlp.301/) | Evaluate your model\'s accuracy in recognizing and handling toxic language with the Real Toxicity Prompts dataset. It contains real-world prompts from online platforms, ensuring robustness in NLP models to maintain safe environments. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/OpenAI_QA_Testing_Notebook.ipynb)\n\n> **Note**\n> For usage and documentation, head over to [langtest.org](https://langtest.org/docs/pages/docs/data#question-answering)\n\n## Contributing\n\nWe welcome all sorts of contributions:\n\n- Ideas\n- Feedback\n- Documentation\n- Bug reports\n- Development and testing\n\nFeel free to clone the repo and submit pull-requests! You can also contribute by simply opening an issue or discussion in this repo.\n\n## Contributors\n\nWe would like to acknowledge all contributors of this open-source community project. \n\n<a href="https://github.com/johnsnowlabs/langtest/graphs/contributors">\n  <img src="https://contrib.rocks/image?repo=johnsnowlabs/langtest" />\n</a>\n\n## License\n\nLangTest is released under the [Apache License 2.0](https://github.com/JohnSnowLabs/langtest/blob/main/LICENSE), which guarantees commercial use, modification, distribution, patent use, private use and sets limitations on trademark use, liability and warranty.\n\n',
    'author': 'John Snow Labs',
    'author_email': 'support@johnsnowlabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.langtest.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
