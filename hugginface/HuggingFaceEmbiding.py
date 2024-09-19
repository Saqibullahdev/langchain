import asyncio
from langchain_huggingface import HuggingFaceEndpointEmbeddings

model = "hkunlp/instructor-xl"
hf = HuggingFaceEndpointEmbeddings(
    model=model,
    task="feature-extraction",
    huggingfacehub_api_token="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",
)

print("HuggingFace Embeddings connected")
listofsentences = ["I am a sentence for which I would like to get its embedding"]

async def getEmbedding(listofsentences):
    return await hf.aembed_documents(listofsentences)

async def main():
    embeddings = await getEmbedding(listofsentences)
    print(embeddings)

# Run the async main function
asyncio.run(main())
