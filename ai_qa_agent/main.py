import argparse
from dotenv import load_dotenv
from answerer import generate_answer
from crawler import crawl_help_site
from embedder import embed_chunks, save_index
from parser import extract_clean_chunks
from retriever import get_relevant_chunks

load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help="Help center base URL")
    parser.add_argument('--question', required=True, help="User question")
    args = parser.parse_args()

    print("📡 Crawling...")
    html = crawl_help_site(args.url)

    print("🧼 Extracting and chunking...")
    chunks = extract_clean_chunks(html)

    print("📈 Embedding...")
    index, metadata = embed_chunks(chunks)
    save_index(index, metadata)

    print("🔎 Retrieving context...")
    relevant_chunks = get_relevant_chunks(args.question, index, metadata)

    print("💬 Generating answer...")
    answer = generate_answer(args.question, relevant_chunks)
    print("\n✅ Answer:\n", answer)

if __name__ == "__main__":
    main()
