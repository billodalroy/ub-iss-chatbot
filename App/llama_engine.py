from llama_index import StorageContext, load_index_from_storage, ServiceContext
from llama_index.llms import OpenAI, TogetherLLM


# Uses OpenAI gpt-3.5-turbo as the LLM
def get_query_engine():
    storage_context = StorageContext.from_defaults(persist_dir="./App/storage")
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=256)

    # configure service context
    service_context = ServiceContext.from_defaults(llm=llm)
    index = load_index_from_storage(storage_context=storage_context,
                                    service_context=service_context)
    query_engine = index.as_query_engine()
    return query_engine


def completion_to_prompt(completion: str) -> str:
    return f"<s>[INST] Strictly Keep the answer short and to the point.\n \
        {completion} [/INST] </s>\n"


# Uses Mistral-7B-instruct -- via API from together.ai
def get_together_query_engine():
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    generative_model = 'mistralai/Mistral-7B-Instruct-v0.2'
    llm = TogetherLLM(
            generative_model,
            temperature=0.8,
            max_tokens=512,
            top_p=0.7,
            top_k=50,
            is_chat_model=False,
            completion_to_prompt=completion_to_prompt
        )
    service_context = ServiceContext.from_defaults(llm=llm)
    index = load_index_from_storage(
       storage_context=storage_context,
       service_context=service_context)
    query_engine = index.as_query_engine(similarity_top_k=5)
    return query_engine
