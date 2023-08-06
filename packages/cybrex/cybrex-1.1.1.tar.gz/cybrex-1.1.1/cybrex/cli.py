import json
import logging
import sys
import textwrap

import fire
from termcolor import colored

from .cybrex_ai import CybrexAI


def create_snippet(document, metadata):
    return metadata['doi'] + ': ' + document


class CybrexCli:
    def __init__(self):
        self.cybrex = CybrexAI()

    async def add_all_documents(self):
        async with self.cybrex as cybrex:
            async for document in cybrex.geck.get_summa_client().documents('nexus_science'):
                document = json.loads(document)
                await self.cybrex.add_documents([document])

    async def dump_texts(self, query: str, output_path: str, n_summa_documents: int = 100):
        """
        Store STC text chunks in ZIP archive

        :param query: query to STC
        :param output_path: where to store result
        :param n_summa_documents: the number of documents to extract
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Q', 'green')}: {query}")
            await cybrex.dump_texts(
                query=query,
                output_path=output_path,
                n_summa_documents=n_summa_documents
            )

    async def import_texts(self, input_path: str):
        """
        Import binary file with embeddings

        :param input_path:
        """
        async with self.cybrex as cybrex:
            await cybrex.import_texts(
                input_path=input_path,
            )

    async def chat_doc(self, field: str, value: str, question: str, n_results: int = 7):
        """
        Ask a question about content of document identified by DOI.

        :param field: name of the field in document used for selection
        :param value: value of the field in document used for selection
        :param question: Text question to the document
        :param n_results: the number of documents to extract from Chroma
            more means more tokens to use and more precision in answer
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Document', 'green')}: {field}:{value}")
            print(f"{colored('Q', 'green')}: {question}")
            response = await cybrex.chat_document(field, value, question, n_results)
            print(f"{colored('A', 'green')}: {response}")

    async def chat_sci(self, question: str, n_results: int = 7, n_summa_documents: int = 9):
        """
        Ask a question about content of document identified by DOI.

        :param question: Text question to the document
        :param n_results: the number of documents to extract from Chroma
            more means more tokens to use and more precision in answer
        :param n_summa_documents: the number of documents to extract from Chroma
            more means more tokens to use and more precision in answer
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Q', 'green')}: {question}")
            response = await cybrex.chat_science(
                question=question,
                n_results=n_results,
                n_summa_documents=n_summa_documents,
            )
            print(f"{colored('A', 'green')}: {response['result'].strip()}")
            snippets = [create_snippet(source_document.page_content, source_document.metadata) for source_document in response['source_documents']]
            sources = textwrap.indent('\n'.join(snippets), ' - ')
            print(f"{colored('Sources', 'green')}:\n{sources}")

    async def sum_doc(self, field: str, value: str):
        """
        Summarization of the document

        :param field: name of the field in document used for selection
        :param value: value of the field in document used for selection
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Document', 'green')}: {field}:{value}")
            response = await cybrex.summarize_document(field, value)
            print(f"{colored('Summarization', 'green')}: {response}")

    async def semantic_search(self, query: str, n_results: int = 7, n_summa_documents: int = 9):
        """
        Ask a question about content of document identified by DOI.

        :param query: query to STC
        :param n_results: number of pieces to return
        :param n_summa_documents: the number of documents to extract from Chroma
            more means more tokens to use and more precision in answer
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Q', 'green')}: {query}")
            response = await cybrex.semantic_search(
                query=query,
                n_results=n_results,
                n_summa_documents=n_summa_documents
            )
            snippets = [
                ' - ' + create_snippet(document, metadata)
                for (document, metadata) in zip(response['documents'][0], response['metadatas'][0])
            ]
            sources = '\n'.join(snippets)
            print(f"{colored('Sources', 'green')}:\n{sources}")


async def cybrex_cli(debug: bool = False):
    """
    :param debug: add debugging output
    :return:
    """
    logging.basicConfig(stream=sys.stdout, level=logging.INFO if debug else logging.ERROR)
    cybrex_ai = CybrexCli()
    return {
        'add-all-documents': cybrex_ai.add_all_documents,
        'chat-doc': cybrex_ai.chat_doc,
        'chat-sci': cybrex_ai.chat_sci,
        'dump-texts': cybrex_ai.dump_texts,
        'import-texts': cybrex_ai.import_texts,
        'semantic-search': cybrex_ai.semantic_search,
        'sum-doc': cybrex_ai.sum_doc,
    }


def main():
    fire.Fire(cybrex_cli, name='cybrex')


if __name__ == '__main__':
    main()
