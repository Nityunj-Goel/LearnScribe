from langchain.document_loaders import YoutubeLoader
from langchain.indexes import VectorstoreIndexCreator


def load_and_vectorize(youtube_url_id):
    loader = YoutubeLoader.from_youtube_url(youtube_url_id, add_video_info=False)
    docs = loader.load()
    index = VectorstoreIndexCreator()
    return index.from_documents(docs)


def chatbot_response(query, index):
    # return index.query(query)
    return query
