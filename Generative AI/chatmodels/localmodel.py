from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="devlocalhost/hi-tinylama-gguf-16bit",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=10,
        do_sample=False,
        repetition_penalty=1.1,
    ),
)

chat_model = ChatHuggingFace(llm=llm)
result = chat_model.invoke("what is the meaning of life?")
print(result.content)
